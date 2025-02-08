# compile output
# nuitka-project: --verbose
# nuitka-project: --show-progress
# nuitka-project: --verbose-output=../build/verbose.log
# nuitka-project: --output-dir=../build
# nuitka-project: --report=../build/report.xml

# compile settings
# nuitka-project: --onefile
# nuitka-project: --lto=yes
# nuitka-project: --jobs=24
# nuitka-project: --plugin-enable=pyside6
# nuitka-project: --prefer-source-code
# nuitka-project: --follow-stdlib
# nuitka-project: --include-module=importlib._abc

# exe settings
# nuitka-project: --windows-icon-from-ico=designer/resources/icon.ico
# nuitka-project: --windows-company-name="Ben Fässler"
# nuitka-project: --windows-product-name=Notes
# nuitka-project: --windows-file-version=1.0

import os
import sys

os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"

if "profile" in sys.argv:
    import cProfile

from copy import copy, deepcopy
from functools import partial
from pathlib import Path
from re import fullmatch

from typing import Callable

import dictdiffer

from PySide6.QtCore import SIGNAL, QEvent, QMargins, QModelIndex, QObject, QPoint, QPointF, QRect, QRectF, Qt, QTranslator, QSize
from PySide6.QtGui import QBrush, QColor, QFont, QFontMetrics, QImage, QMouseEvent, QPainter, QPainterPath, QPen, QPixmap, QPolygon, QStandardItem, QStandardItemModel, QTextDocument
from PySide6.QtSvg import QSvgGenerator
from PySide6.QtWidgets import QApplication, QColorDialog, QDialog, QFileDialog, QGraphicsScene, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QScrollArea, QSizePolicy, QStyledItemDelegate, QStyleOptionViewItem, QVBoxLayout, QWidget, QGraphicsPixmapItem, QGraphicsEllipseItem, QGraphicsPolygonItem, QGraphicsPathItem, QGraphicsRectItem, QRubberBand

from tendo.singleton import SingleInstance, SingleInstanceException

from BlurWindow.blurWindow import blur

from constants import *
from random_id import IDGenerator
from special_logging import LOG_HIERARCHICAL_VIEW_UPDATES, LOG_CHOOSEN_COLOR, LOG_PROFILING, LOG_UNDO_ACTION, LOG_FATAL_ERROR, log

from storage.helpers import delete_data, prepare_first_run, check_if_data_is_valid
from storage.images import Registry, get_hash_from_image, get_image, import_image
from storage.paint import create_new_paint, delete_paint, load_paint, save_paint
from storage.painting_nodes import EllipseNode, ImageNode, LineNode, PolygonNode, PointNode, RectangleNode
from storage.templates import ENTRY_TEMPLATE
from storage_generated.entries import load_entries
from storage_generated.settings import Settings, load_settings

from shared import get_actual_time

from ui_generated.AskTagDialog import Ui_Dialog as UI_AskTagDialog
from ui_generated.MainWindow import Ui_MainWindow
from ui_generated.SettingsDialog import Ui_Dialog as UI_SettingsDialog

ID_GENERATOR = IDGenerator()


class MainWindowEventFilter(QObject):
    def eventFilter(self, widget: QMainWindow, event: QEvent) -> False:  # sourcery skip: merge-nested-ifs
        if event.type() == KEY_RELEASE_EVENT:
            if event.key() in [UP_KEY, DOWN_KEY]:
                widget.hierarchical_view_on_treeview_selection_changed()

            if event.key() == SHIFT_KEY:
                widget.if_shift_pressed = False

        if event.type() == KEY_PRESS_EVENT:
            if event.key() == SHIFT_KEY and not widget.if_shift_pressed:
                widget.if_shift_pressed = True

            if event.key() == RETURN_KEY and widget.settings.get_active_tab() == 2 and widget.entries.get_activated_paint_mode(widget.iid) == "polygon":
                widget.paint_tab_finish_polygon()


class GlobalEventFilter(QObject):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent

    def eventFilter(self, object, event: QEvent):
        if event.type() == QEvent.MouseButtonPress:
            global_pos = event.globalPos()
            view_rect = self.parent.ui.paint_graphicsview.rect()
            view_top_left_global = self.parent.ui.paint_graphicsview.mapToGlobal(view_rect.topLeft())
            view_rect_global = QRect(view_top_left_global, view_rect.size())
            if not view_rect_global.contains(global_pos):
                if self.parent.paint_tab_resizer_rubber_band is not None:
                    self.parent.paint_tab_resizer_rubber_band.hide()
                    self.parent.paint_tab_is_resizing = False

        return super().eventFilter(self.parent, event)


class StyledItemDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()

        path.addRoundedRect(option.rect - QMargins(1, 1, 1, 1), 5, 5) 

        painter.fillPath(path, index.data(BACKGROUND_ROLE))

        painter.setPen(QPen(QBrush("black"), 2))

        painter.setFont(QFont("Segoe UI", 9, QFont.Normal))

        rect = option.rect
        rect.setX(rect.x() + 5)
    
        painter.drawText(rect, index.data(DISPLAY_ROLE))

        painter.setPen(QPen(QBrush("black"), 2))

        if index.data(SELECTION_ROLE):
            painter.drawPath(path)


    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setFrame(True)
        editor.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid gainsboro;
                border-radius: 3px;
            }"""
        )
        return editor


class StandardItem(QStandardItem):
    def __init__(self, update_text_function: Callable[[str, str], None], *args) -> None:
        super().__init__(*args)
        self.update_text_function = update_text_function


    def setData(self, value: str, role: int) -> None:
        if role == EDIT_ROLE: # if item directly edited by user on UI
            self.update_text_function(QStandardItem.data(self, ID_ROLE), value)

        QStandardItem.setData(self, value, role) # do what normally happens


class AskTagDialog(QDialog):
    def __init__(self):
        super(AskTagDialog, self).__init__()

        self.ui = UI_AskTagDialog()
        self.ui.setupUi(self)

        self.ui.tag_name_entry.textChanged.connect(self.on_tag_name_changed)
        self.ui.submit_button.clicked.connect(self.close)
        self.tag_name = ""

        self.show()
        self.exec()

    def on_tag_name_changed(self) -> None:
        self.tag_name = self.ui.tag_name_entry.text()
        

class SettingsDialog(QDialog):
    def __init__(self, settings: Settings, on_color_button_clicked: Callable, set_color_button_color: Callable) -> None:
        super(SettingsDialog, self).__init__()

        self.settings = settings

        self.set_color_button_color = set_color_button_color

        self.ui = UI_SettingsDialog()
        self.ui.setupUi(self)

        self.ui.background1_button.clicked.connect(partial(self.background_button_function, 1))
        self.ui.background2_button.clicked.connect(partial(self.background_button_function, 2))
        self.ui.background3_button.clicked.connect(partial(self.background_button_function, 3))
        self.ui.background4_button.clicked.connect(partial(self.background_button_function, 4))
        self.ui.background5_button.clicked.connect(partial(self.background_button_function, 5))
        self.ui.background6_button.clicked.connect(partial(self.background_button_function, 6))
        self.ui.background7_button.clicked.connect(partial(self.background_button_function, 7))
        self.ui.background8_button.clicked.connect(partial(self.background_button_function, 8))
        self.ui.background9_button.clicked.connect(partial(self.background_button_function, 9))

        self.enable_background_button(self.settings.get_background_image())

        self.ui.language_combobox.currentIndexChanged.connect(self.language_combobox_function)
        self.ui.language_combobox.setCurrentText("German" if self.settings.get_language() == "de" else "English")

        self.ui.color_button.clicked.connect(partial(on_color_button_clicked, self.ui.color_button, self.color_function, True))
        self.color_function(QColor(self.settings.get_background_color()))

        self.ui.acryl_checkbox.stateChanged.connect(partial(self.acryl_checkbox_function))
        self.ui.acryl_checkbox.setChecked(self.settings.get_background_acryl())

        self.ui.apply_color_button.clicked.connect(partial(self.settings.set_background_mode, "color"))
        self.ui.apply_image_button.clicked.connect(partial(self.settings.set_background_mode, "image"))

        self.ui.language_combobox.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.ui.language_combobox.view().window().setAttribute(Qt.WA_TranslucentBackground)

        self.show()
        self.exec()


    def color_function(self, color):
        self.settings.set_background_color(color.name(QColor.NameFormat.HexArgb))
        self.set_color_button_color(self.ui.color_button, color.name(QColor.NameFormat.HexArgb))


    def acryl_checkbox_function(self, value):
        self.settings.set_background_acryl(Qt.CheckState(value) == Qt.Checked)


    def language_combobox_function(self, value):
        self.settings.set_language("de" if value == 1 else "en")


    def background_button_function(self, background):
        self.disable_background_button(self.settings.get_background_image())
        self.enable_background_button(background)
        self.settings.set_background_image(background)


    def disable_background_button(self, background):
        getattr(self.ui, f"background{background}_button").setStyleSheet("""background-color: "white";""")
        

    def enable_background_button(self, background):
        getattr(self.ui, f"background{background}_button").setStyleSheet("""background-color: rgb(155, 240, 11);""")


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication) -> None:
        super(MainWindow, self).__init__()
        self.app = app

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # initialyze UI

        self.load_entries() # load entries

        self.entries.on_save = self.on_save # set method to update modification time

        self.settings = load_settings() # load settings

        self.iid = self.settings.get_active_entry() # load last opened id

        self.translator = QTranslator(self.app) # create translator object

        self.update_language() # initially translate the window

        self.image_registry = Registry()
        self.paint_data = {}
        self.last_paint_data = {}

        self.selected_item = None
        self.selected_item_start_position = QPoint()
        self.selected_item_relative_to_mouse_position = QPoint()

        # set all variables that will be used later
        # not required, but helps to keep things clear
        self.actual_text_bg_color = "#ffffff"
        self.actual_text_fg_color = "#ffffff"
        self.actual_text_font_size = 0

        self.if_shift_pressed = False

        self.empty_mode = False

        self.paint_tab_only_pressed = False # True if only pressed and not moved on paint_graphicsscene
        self.paint_tab_is_polygon_unfinished = None  # bool or None: True if a polygon has been started but not yet finished.
        self.paint_tab_start_coordinates = None        # QPoint or tuple: Starting coordinates of a drawing operation.
        self.paint_tab_last_coordinates = None         # QPoint or tuple: The last known coordinates during the drawing operation.
        self.paint_tab_actual_object_id = None         # str or int: Unique ID of the currently active object.
        self.paint_tab_actual_item = None              # QGraphicsItem: The currently placed drawing item in the scene.
        self.paint_tab_history = []                    # list: History of changes (e.g., for undo functionality).
        self.paint_tab_resizer_rubber_band_start_position = None  # QPoint: The starting position of the resizer overlay.
        self.paint_tab_is_resizing = False             # bool: True if a resizing operation is active, otherwise False.

        self.paint_tab_resizer_rubber_band = QRubberBand(QRubberBand.Rectangle, self.ui.paint_graphicsview)

        self.paint_tab_image_rect = None              # QRect: The original image rectangle in scene coordinates.
        self.paint_tab_resize_offset = None           # QPoint: The offset between the mouse position and the grabbed corner (in scene coordinates).
        self.paint_tab_original_pixmap = None         # QPixmap: The original image used for scaling.
        self.paint_tab_grabbed_corner = None          # tuple: The grabbed corner (e.g., (x, y) in scene coordinates) when a handle is hit.
        self.paint_tab_anchor = None                  # QPoint: The fixed, opposite corner (anchor) to the grabbed handle.
        self.paint_tab_initial_size = None            # QSize: The original image size at the start of resizing.
        self.paint_tab_initial_aspect = 1.0           # float: The original aspect ratio (width / height).
        self.paint_tab_move_start_pos = None          # QPoint: The starting position of a move operation (in scene coordinates).
        self.selected_item_relative_to_mouse_position = None  # QPoint: The offset between the mouse position and the image position in move mode.
        
        self.dont_update_text = False
        self.dont_save_expanded_status = False

        self.setAttribute(Qt.WA_TranslucentBackground)
        blur(self.winId())
        
        # Main Tab Manager
        self.ui.MainTabManager.currentChanged.connect(self.on_tab_change)

        # Hierarchical View
        self.hierarchical_view_model = QStandardItemModel()
        self.hierarchical_view_model.intern = {}

        self.ui.HierarchicalView.setModel(self.hierarchical_view_model)
        self.ui.HierarchicalView.setItemDelegate(StyledItemDelegate())

        self.ui.HierarchicalView.clicked.connect(self.on_treeview_clicked)
        self.ui.HierarchicalView.expanded.connect(self.hierarchical_view_on_treeview_item_expanded)
        self.ui.HierarchicalView.collapsed.connect(self.hierarchical_view_on_treeview_item_collapsed)

        self.ui.HierarchicalView.horizontalScrollBar().sliderMoved.connect(self.hierarchical_view_save_scrollbar_values)

        self.ui.HierarchicalView.verticalScrollBar().sliderMoved.connect(self.hierarchical_view_save_scrollbar_values)

        # General Tab
        self.ui.insert_entry_button.clicked.connect(self.general_tab_on_insert_entry_button_clicked)
        self.ui.delete_entry_button.clicked.connect(self.general_tab_on_delete_entry_button_clicked)
        self.ui.name_color_button.clicked.connect(partial(self.on_color_button_clicked, self.ui.name_color_button, self.general_tab_name_color_function))

        self.ui.name_entry.textChanged.connect(self.general_tab_on_name_text_edited)

        self.ui.insert_tag_button.clicked.connect(self.general_tab_on_insert_tag_clicked)

        self.tags_scroll_area = QScrollArea(self.ui.general_tab)
        self.tags_scroll_area.setGeometry(
            QRect(
                10,
                130,
                850,
                71
            )
        )

        self.tags_scroll_area.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }

            QScrollArea {
                background-color: rgba(255, 255, 255, 50);
                border-width: 0px;
                border-radius: 6px;
            }
        """)

        self.tags_layout = QHBoxLayout(self.tags_scroll_area)
        self.tags_layout.setAlignment(Qt.AlignLeft)

        # Text Tab
        self.ui.text_entry.textChanged.connect(self.text_tab_on_text_edited)
        self.ui.text_entry.selectionChanged.connect(self.text_tab_on_text_selection_changed)
 
        self.ui.text_tab_bold_button.clicked.connect(partial(self.text_tab_on_text_formatted, "bold"))
        self.ui.text_tab_italic_button.clicked.connect(partial(self.text_tab_on_text_formatted, "italic"))
        self.ui.text_tab_underline_button.clicked.connect(partial(self.text_tab_on_text_formatted, "underline"))
        self.ui.text_tab_overstrike_button.clicked.connect(partial(self.text_tab_on_text_formatted, "overstrike"))

        self.ui.text_tab_background_color_button.clicked.connect(partial(self.on_color_button_clicked, self.ui.text_tab_background_color_button, self.text_tab_background_color_function))
        self.ui.text_tab_foreground_color_button.clicked.connect(partial(self.on_color_button_clicked, self.ui.text_tab_foreground_color_button, self.text_tab_foreground_color_function))

        self.ui.text_tab_font_combobox.currentFontChanged.connect(self.on_text_font_changed)
        self.ui.text_tab_font_combobox.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.ui.text_tab_font_combobox.view().window().setAttribute(Qt.WA_TranslucentBackground)

        self.ui.text_tab_size_spinbox.valueChanged.connect(self.on_text_spinbox_value_changed)

        self.ui.search_mode_combobox.currentTextChanged.connect(self.search_tab_update_search)

        self.ui.regex_checkbox.stateChanged.connect(self.search_tab_update_search)

        # Paint Tab
        self.ui.paint_tab_clear_button.clicked.connect(self.paint_tab_on_clear_button_clicked)

        self.ui.paint_tab_enable_selector_button.clicked.connect(partial(self.paint_tab_enable_paint_mode, self.ui.paint_tab_enable_selector_button, "selector"))
        self.ui.paint_tab_enable_pen_button.clicked.connect(partial(self.paint_tab_enable_paint_mode, self.ui.paint_tab_enable_pen_button, "pen"))
        self.ui.paint_tab_enable_eraser_button.clicked.connect(partial(self.paint_tab_enable_paint_mode, self.ui.paint_tab_enable_eraser_button, "eraser"))
        self.ui.paint_tab_enable_rectangle_button.clicked.connect(partial(self.paint_tab_enable_paint_mode, self.ui.paint_tab_enable_rectangle_button, "rectangle"))
        self.ui.paint_tab_enable_ellipse_button.clicked.connect(partial(self.paint_tab_enable_paint_mode, self.ui.paint_tab_enable_ellipse_button, "ellipse"))
        self.ui.paint_tab_enable_polygon_button.clicked.connect(partial(self.paint_tab_enable_paint_mode, self.ui.paint_tab_enable_polygon_button, "polygon"))
        self.ui.paint_tab_enable_image_button.clicked.connect(partial(self.paint_tab_enable_paint_mode, self.ui.paint_tab_enable_image_button, "image"))

        self.ui.paint_tab_line_settings_color_button.clicked.connect(partial(self.on_color_button_clicked, self.ui.paint_tab_line_settings_color_button, self.paint_tab_line_settings_color_function, True))
        self.ui.paint_tab_line_settings_one_click_line_checkbutton.stateChanged.connect(self.paint_tab_on_one_click_line_mode_changed)

        self.ui.paint_tab_shape_settings_fill_color_button.clicked.connect(partial(self.on_color_button_clicked, self.ui.paint_tab_shape_settings_fill_color_button, self.paint_tab_shape_settings_fill_color_function, True))
        self.ui.paint_tab_shape_settings_outline_color_button.clicked.connect(partial(self.on_color_button_clicked, self.ui.paint_tab_shape_settings_outline_color_button, self.paint_tab_shape_settings_outline_color_function, True))

        self.ui.paint_tab_line_settings_size_spinbox.valueChanged.connect(self.paint_tab_on_line_size_changed)
        self.ui.paint_tab_shape_settings_outline_size_spinbox.valueChanged.connect(self.paint_tab_on_outline_size_changed)
        self.ui.paint_tab_eraser_settings_size_spinbox.valueChanged.connect(self.paint_tab_on_eraser_size_changed)
        self.ui.paint_tab_export_button.clicked.connect(self.paint_tab_export)

        self.ui.paint_tab_undo_button.clicked.connect(self.paint_tab_on_undo_button_clicked)

        self.paint_graphicsscene = QGraphicsScene()
        self.ui.paint_graphicsview.setScene(self.paint_graphicsscene)

        self.ui.paint_graphicsview.mousePressEvent = self.paint_tab_on_graphicsview_pressed
        self.ui.paint_graphicsview.mouseMoveEvent = self.paint_tab_on_graphicsview_moved
        self.ui.paint_graphicsview.mouseReleaseEvent = self.paint_tab_on_graphicsview_released

        # Search Tab
        self.ui.search_scroll_area.setGeometry(
            QRect(
                10,
                50,
                911,
                681
            )
        )

        self.ui.search_scroll_area.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }

            QScrollArea {
                background-color: rgba(255, 255, 255, 50);
                border-width: 0px;
                border-radius: 6px;
            }
        """)

        self.search_layout_container = QWidget(self.ui.search_scroll_area)
        self.search_layout = QVBoxLayout(self.search_layout_container)
        self.search_layout.setAlignment(Qt.AlignLeft)

        self.ui.search_scroll_area.setWidget(self.search_layout_container)

        self.ui.search_scroll_area.setStyleSheet(SCROLL_AREA_STYLE_SHEET)
        self.ui.search_mode_combobox.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.ui.search_mode_combobox.view().window().setAttribute(Qt.WA_TranslucentBackground)

        self.ui.tags_combobox.currentTextChanged.connect(self.search_tab_update_search)
        self.ui.tags_combobox.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.ui.tags_combobox.view().window().setAttribute(Qt.WA_TranslucentBackground)


        self.ui.search_entry.textChanged.connect(self.search_tab_update_search)

        self.ui.case_sensitive_checkbox.stateChanged.connect(self.search_tab_update_search)


        # Settings Button
        self.ui.settings_button.clicked.connect(self.show_settings_dialog)

        self.eventFilter = MainWindowEventFilter(parent=self)
        self.installEventFilter(self.eventFilter)

        self.global_event_filter = GlobalEventFilter(parent=self)
        app.installEventFilter(self.global_event_filter)

        self.load_hierarchical_view()

        self.load_specific_entry(self.iid)
        self.load_search_tab()

        self.update_background()

        self.ui.MainTabManager.setCurrentIndex(self.settings.get_active_tab())


    def update_language(self) -> None:
        """
        change app language to the in the settings saved
        """ 
        if self.settings.get_language() == "de":
            self.translator.load(":/translations/main_window_de.qm") # load language file 
            self.app.installTranslator(self.translator) # install the translator to the app

        else:
            self.app.removeTranslator(self.translator)

        self.ui.retranslateUi(self) # translate all widgets


    def update_background(self) -> None:
        if self.settings.get_background_mode() == "color":
            self.ui.background_overlay.setStyleSheet(f"background-color: {self.settings.get_background_color()}")
            if self.settings.get_background_acryl():
                self.ui.blur_shield.setStyleSheet("background-color: transparent")

            else:
                self.ui.blur_shield.setStyleSheet("background-color: white")
            

        else:
            self.update_background_image()


    def update_background_image(self) -> None:
        """
        change background image to the in the settings saved
        """
        self.ui.background_overlay.setStyleSheet(f"background-image: url(:/backgrounds/{self.settings.get_background_image()}.png)")


    def load_entries(self) -> None:
        """
        update self.entries from storage
        """
        self.entries = load_entries()
        self.entries.on_save = self.on_save


    def load_entry(self) -> None:
        """
        load the entry with ID [self.iid]
        """
        self.settings.set_active_entry(self.iid)
        self.paint_tab_history = []
        self.last_paint_data = None

        with DontUpdateModificationTime(self):
            self.load_general_tab()
            self.load_text_tab()
            self.load_paint_tab()


    def load_specific_entry(self, iid) -> None:
        self.iid = iid
        self.load_entry()
        if self.entries.id_exists(iid):
            for item in self.iterate_over_treeview(self.hierarchical_view_model.invisibleRootItem()):
                if item.data(SELECTION_ROLE):
                    item.setData(False, SELECTION_ROLE)
                
            self.hierarchical_view_model.setData(self.get_model_index_by_id(iid), True, SELECTION_ROLE)

        self.ui.MainTabManager.setCurrentIndex(0)


    def load_general_tab(self) -> None:
        """
        load the entry with ID [self.iid] to General Tab
        """
        if self.entries.id_exists(self.iid):
            if self.empty_mode:
                self.empty_mode = False

                self.enable_widgets(
                    [
                        self.ui.name_entry,
                        self.ui.name_color_button,
                        self.ui.delete_entry_button,
                    ]
                )

            with DontUpdateText(self):
                self.ui.name_entry.setText(self.entries.get_name_text(self.iid))

            self.set_color_button_color(self.ui.name_color_button, self.entries.get_name_color(self.iid))

            self.ui.id_label.setText(self.iid)
            self.ui.creation_time_label.setText(self.entries.get_creation_time(self.iid))
            self.ui.modification_time_label.setText(self.entries.get_modification_time(self.iid))

            for i in reversed(range(self.tags_layout.count())): 
                self.tags_layout.itemAt(i).widget().setParent(None)

            tags = self.entries.get_tags(self.iid)
            widths = [QFontMetrics(self.ui.HierarchicalView.font()).horizontalAdvance(tag) + 20 for tag in tags]

            for i, tag, width in zip(range(len(tags)), tags, widths):
                tag_button = QPushButton()
                tag_button.setObjectName(f"tag_{tag}_{ID_GENERATOR.get_id()}")
                tag_button.setMinimumSize(
                        width,
                        24
                )
                tag_button.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
                tag_button.setText(tag)
                tag_button.setStyleSheet("""
                    QPushButton{
                        background-color: white;
                    }

                    QPushButton:hover{
                        background-color: rgba(255, 255, 255, 150);
                    }
                """)

                tag_button.clicked.connect(partial(self.general_tab_on_tag_clicked, i))

                self.tags_layout.addWidget(tag_button)

        else:
            self.empty_mode = True

            self.disable_widgets(
                [
                    self.ui.name_entry,
                    self.ui.name_color_button,
                    self.ui.delete_entry_button,
                ]
            )

            with DontUpdateText(self):
                self.ui.name_entry.setText("")

            self.set_color_button_color(self.ui.name_color_button, "white")   

            self.ui.id_label.setText("")
            self.ui.creation_time_label.setText("")
            self.ui.modification_time_label.setText("")


    def load_text_tab(self):
        """
        load the entry with ID [self.iid] to Text Tab
        """
        if self.entries.id_exists(self.iid):
            if self.empty_mode:

                self.empty_mode = False

                self.ui.text_entry.setEnabled(True)
                self.enable_widgets(
                    [
                        self.ui.text_entry,
                        self.ui.text_tab_background_color_button,
                        self.ui.text_tab_foreground_color_button,
                        self.ui.text_tab_font_combobox,
                        self.ui.text_tab_bold_button,
                        self.ui.text_tab_italic_button,
                        self.ui.text_tab_overstrike_button,
                        self.ui.text_tab_underline_button,
                        self.ui.text_tab_size_spinbox
                    ]
                )

            with DontUpdateText(self):
                self.ui.text_entry.setHtml(self.entries.get_text(self.iid))
            
            self.set_color_button_color(self.ui.text_tab_background_color_button, self.actual_text_bg_color)
            self.set_color_button_color(self.ui.text_tab_foreground_color_button, self.actual_text_fg_color)
            self.ui.text_tab_size_spinbox.setValue(self.actual_text_font_size)

        else:
            self.disable_widgets(
                [
                        self.ui.text_entry,
                        self.ui.text_tab_background_color_button,
                        self.ui.text_tab_foreground_color_button,
                        self.ui.text_tab_font_combobox,
                        self.ui.text_tab_bold_button,
                        self.ui.text_tab_italic_button,
                        self.ui.text_tab_overstrike_button,
                        self.ui.text_tab_underline_button,
                        self.ui.text_tab_size_spinbox
                ]
            )
            
            self.ui.text_entry.setHtml(EMPTY_HTML)

            self.set_color_button_color(self.ui.text_tab_background_color_button, "white")
            self.set_color_button_color(self.ui.text_tab_foreground_color_button, "white")
            
            self.ui.text_tab_size_spinbox.setValue(0)


    def load_paint_tab(self) -> None:
        if self.entries.id_exists(self.iid):
            self.paint_data = load_paint(self.iid)
            self.paint_tab_load_from_entry()

            self.ui.paint_tab_eraser_settings_size_spinbox.setValue(self.entries.get_eraser_size(self.iid))

            self.ui.paint_tab_line_settings_one_click_line_checkbutton.setChecked(self.entries.get_one_click_line_mode(self.iid))

            self.set_color_button_color(self.ui.paint_tab_line_settings_color_button, self.entries.get_line_color(self.iid))
            self.ui.paint_tab_line_settings_size_spinbox.setValue(self.entries.get_line_size(self.iid))
            
            self.set_color_button_color(self.ui.paint_tab_shape_settings_outline_color_button, self.entries.get_shape_outline_color(self.iid))
            self.set_color_button_color(self.ui.paint_tab_shape_settings_fill_color_button, self.entries.get_shape_fill_color(self.iid))
            self.ui.paint_tab_shape_settings_outline_size_spinbox.setValue(self.entries.get_shape_outline_size(self.iid))

            self.paint_tab_enable_paint_mode(self.ui.__getattribute__(f"paint_tab_enable_{self.entries.get_activated_paint_mode(self.iid)}_button"), self.entries.get_activated_paint_mode(self.iid))
            if self.empty_mode:
                self.empty_mode = False

                self.ui.text_entry.setEnabled(True)
                self.enable_widgets(
                    [
                        self.ui.paint_graphicsview,
                        self.ui.paint_tab_clear_button,
                        self.ui.paint_tab_enable_selector_button,
                        self.ui.paint_tab_enable_pen_button,
                        self.ui.paint_tab_enable_eraser_button,
                        self.ui.paint_tab_enable_rectangle_button,
                        self.ui.paint_tab_enable_ellipse_button,
                        self.ui.paint_tab_enable_polygon_button,
                        self.ui.paint_tab_enable_image_button,
                        self.ui.paint_tab_line_settings_one_click_line_checkbutton,
                        self.ui.paint_tab_line_settings_color_button,
                        self.ui.paint_tab_line_settings_size_spinbox,
                        self.ui.paint_tab_shape_settings_fill_color_button,
                        self.ui.paint_tab_shape_settings_outline_color_button,
                        self.ui.paint_tab_shape_settings_outline_size_spinbox,
                        self.ui.paint_tab_undo_button,
                        self.ui.paint_tab_export_button
                    ]
                )


        else:
            self.disable_widgets(
                [
                        self.ui.paint_graphicsview,
                        self.ui.paint_tab_clear_button,
                        self.ui.paint_tab_enable_selector_button,
                        self.ui.paint_tab_enable_pen_button,
                        self.ui.paint_tab_enable_eraser_button,
                        self.ui.paint_tab_enable_rectangle_button,
                        self.ui.paint_tab_enable_ellipse_button,
                        self.ui.paint_tab_enable_polygon_button,
                        self.ui.paint_tab_enable_image_button,
                        self.ui.paint_tab_line_settings_one_click_line_checkbutton,
                        self.ui.paint_tab_line_settings_color_button,
                        self.ui.paint_tab_line_settings_size_spinbox,
                        self.ui.paint_tab_shape_settings_fill_color_button,
                        self.ui.paint_tab_shape_settings_outline_color_button,
                        self.ui.paint_tab_shape_settings_outline_size_spinbox,
                        self.ui.paint_tab_undo_button,
                        self.ui.paint_tab_export_button
                ]
            )


    def load_search_tab(self) -> None:
        self.ui.tags_combobox.clear()
        tags = set([""])
        for entry in self.entries:
            tags.update(entry["tags"])

        self.ui.tags_combobox.addItems(tags)


    def load_hierarchical_view(self) -> None:
        """
        load the entry with ID [self.iid] to HierarchicalView
        """
        log("Reloaded hierarchical view.", LOG_HIERARCHICAL_VIEW_UPDATES)

        self.dont_save_expanded_status = True

        if self.ui.name_entry.receivers(SIGNAL("self.on_name_text_edited()")) > 0:
            self.ui.name_entry.textChanged.disconnect(self.general_tab_on_name_text_edited)

        self.hierarchical_view_model.clear()
        for entry in self.entries:
            _ = StandardItem(self.general_tab_update_name_text_function, entry["name"]["text"])

            self.hierarchical_view_model.intern[entry["id"]] = _

            parent_id = entry["parent"]
            if parent_id != "0":
                self.hierarchical_view_model.intern[parent_id].appendRow(_)

            else:
                self.hierarchical_view_model.appendRow(_)

            self.ui.HierarchicalView.setExpanded(_.index(), entry["is_open"])
            self.hierarchical_view_model.setData(_.index(), QBrush(entry["name"]["color"]), role=BACKGROUND_ROLE)
            self.hierarchical_view_model.setData(_.index(), entry["id"], role=ID_ROLE)

        self.dont_save_expanded_status = False

        # auto-resize TreeView
        self.ui.HierarchicalView.resizeColumnToContents(0)

        self.hierarchical_view_restore_scrollbar_values()


    def set_color_button_color(self, button: QPushButton, color: str) -> None:
        """
        change the color of the 'Name Color Button'
        """
        button.setStyleSheet(f"border-radius: 22px; background-color: {color};")


    def disable_widgets(self, widgets: list) -> None:
        """
        disable all given widgets
        """
        for widget in widgets:
            widget.setEnabled(False)


    def enable_widgets(self, widgets: list) -> None:
        """
        enable all given widgets
        """
        for widget in widgets:
            widget.setEnabled(True)


    def hierarchical_view_save_scrollbar_values(self) -> None:
        """
        save the actual state of the ScrollBars to the settings
        """
        self.settings.set_horizontal_scrollbar_value(self.ui.HierarchicalView.horizontalScrollBar().value())
        self.settings.set_vertical_scrollbar_value(self.ui.HierarchicalView.verticalScrollBar().value())


    def hierarchical_view_restore_scrollbar_values(self) -> None:
        """
        restore the actual state of the ScrollBars from the settings
        """
        self.ui.HierarchicalView.horizontalScrollBar().setSliderPosition(self.settings.get_horizontal_scrollbar_value())
        self.ui.HierarchicalView.verticalScrollBar().setSliderPosition(self.settings.get_vertical_scrollbar_value()) 


    def hierarchical_view_on_treeview_selection_changed(self) -> None:
        index = self.ui.HierarchicalView.selectedIndexes()[0]

        for item in self.iterate_over_treeview(self.hierarchical_view_model.invisibleRootItem()):
            item.setData(False, SELECTION_ROLE)

        self.hierarchical_view_model.itemFromIndex(index).setData(True, SELECTION_ROLE)

        self.iid = self.get_treeview_item_id_by_index(index)
        self.load_entry()
        self.hierarchical_view_restore_scrollbar_values()


    on_treeview_clicked = hierarchical_view_on_treeview_selection_changed # alias for a more appropriate name

    def hierarchical_view_on_treeview_item_expanded(self, index) -> None:
        if not self.dont_save_expanded_status:
            with DontUpdateModificationTime(self):
                self.entries.set_is_open(self.get_treeview_item_id_by_index(index), True)


    def hierarchical_view_on_treeview_item_collapsed(self, index) -> None:
        if not self.dont_save_expanded_status:
            with DontUpdateModificationTime(self):
                self.entries.set_is_open(self.get_treeview_item_id_by_index(index), False)


    def general_tab_on_insert_entry_button_clicked(self) -> None:
        new_entry = deepcopy(ENTRY_TEMPLATE)

        if self.entries.id_exists(self.iid):
            new_entry["id"] = self.get_next_free_id(self.get_used_entry_ids())

            parent_id = self.entries.get_parent(self.iid)
            new_entry["parent"] = self.iid if self.if_shift_pressed else parent_id

            if self.if_shift_pressed:
                self.entries.set_is_open(self.iid, True)
            
            new_entry["position"] = self.entries.get_position(self.iid) + 1
            for iid in self.get_children_entry(self.entries.get_parent(self.iid)):
                position = self.entries.get_position(iid)
                if position >= new_entry["position"]:
                    self.entries.set_position(iid, position + 1)

            new_entry["times"]["creation_time"], new_entry["times"]["modification_time"] = (get_actual_time(),) * 2

        self.entries.append(new_entry)
        self.entries.save()
        self.load_entries()

        self.hierarchical_view_save_scrollbar_values()
        self.load_hierarchical_view()

        create_new_paint(new_entry["id"])


    def general_tab_on_delete_entry_button_clicked(self) -> None:
        self.entries.delete_entry_recursive(self.iid)
        delete_paint(self.iid)

        self.load_entries()
        self.load_hierarchical_view()
        with DontUpdateText(self):
            self.load_entry()

    def on_color_button_clicked(self, button: QPushButton, function: Callable, transparency: bool = False) -> None:
        color_dialog = QColorDialog()

        # load all custom colors to dialog
        for i, color in enumerate(self.settings.get_color_chooser_custom_colors()):
            color_dialog.setCustomColor(i, QColor(color))

        color = button.palette().color(button.backgroundRole())
        if transparency:
            color = color_dialog.getColor(color, options=QColorDialog.ShowAlphaChannel | QColorDialog.DontUseNativeDialog)

        else:
             color = color_dialog.getColor(color, options=QColorDialog.DontUseNativeDialog)

        log(f"Choosen color {color.name(QColor.HexArgb)} by {button.objectName()}.", LOG_CHOOSEN_COLOR)

        # update color in UI
        if color.isValid(): # check if color was set
            self.set_color_button_color(button, color.name(QColor.HexArgb))
            function(color)

        # save all custom colors to settings
        colors = [color_dialog.customColor(i).name(QColor.HexArgb) for i in range(15)]
        self.settings.set_color_chooser_custom_colors(colors)


    def paint_tab_get_new_id(self) -> str | int:
        return str(
            int(max(int(key) for key in self.paint_data.keys())) + 1 if len(self.paint_data) > 0
            else 0
        )


    def paint_tab_export(self) -> None:
        if path := QFileDialog().getSaveFileName(filter="SVG (*.svg)")[0]:
            svg_generator = QSvgGenerator()
            svg_generator.setFileName(path)
            svg_generator.setSize(self.paint_graphicsscene.sceneRect().size().toSize())

            painter = QPainter()
            painter.begin(svg_generator)
            painter.setRenderHint(QPainter.Antialiasing)
            self.paint_graphicsscene.render(painter)
            painter.end()


    def paint_tab_on_clear_button_clicked(self) -> None:
        self.paint_graphicsscene.clear()
        self.image_registry.unregister_all_from_iid(self.iid, self.paint_data)

        self.paint_data = {}
        save_paint(self.iid, self.paint_data)


    def paint_tab_enable_paint_mode(self, button: QPushButton, mode: str) -> None:
        self.entries.set_activated_paint_mode(self.iid, mode)

        buttons = [
            self.ui.paint_tab_enable_selector_button,
            self.ui.paint_tab_enable_pen_button,
            self.ui.paint_tab_enable_eraser_button,
            self.ui.paint_tab_enable_rectangle_button,
            self.ui.paint_tab_enable_ellipse_button,
            self.ui.paint_tab_enable_polygon_button,
            self.ui.paint_tab_enable_image_button
        ]

        for _button in buttons:
            self.set_button_status(_button, _button.objectName()[17: -7], False)

        self.set_button_status(button, button.objectName()[17: -7], True)

        settings = {
            "selector": self.ui.empty_settings,
            "eraser": self.ui.eraser_settings,
            "pen": self.ui.line_settings,
            "rectangle": self.ui.shape_settings,
            "ellipse": self.ui.shape_settings,
            "polygon": self.ui.shape_settings,
            "image": self.ui.empty_settings,
        }

        self.ui.stackedWidget.setCurrentWidget(settings[mode])
        

    def paint_tab_on_one_click_line_mode_changed(self) -> None:
        self.entries.set_one_click_line_mode(self.iid, self.ui.paint_tab_line_settings_one_click_line_checkbutton.isChecked())


    def paint_tab_load_from_entry(self) -> None:
        self.paint_graphicsscene.clear()
        self.paint_tab_paint_line( # paint one line because a bug causes the first line to start with weird coordinates
            LineNode(
                [
                    (1, 1),
                    (2, 2),
                ],
                1,
                "white",
                True
            )
        )

        painter_functions = {
            "Line": self.paint_tab_paint_line,
            "Rectangle": self.paint_tab_paint_rectangle,
            "Ellipse": self.paint_tab_paint_ellipse,
            "Point": self.paint_tab_paint_point,
            "Polygon": self.paint_tab_paint_polygon,
            "Image": self.paint_tab_paint_image
        }

        for key, node in self.paint_data.items():
            self.paint_tab_actual_object_id = key
            painter_functions[type(node).__name__[:-4]](node)


    def paint_tab_update_history(self) -> None:
        self.paint_tab_history.append(list(dictdiffer.diff(self.last_paint_data, self.paint_data)))


    def paint_tab_on_undo_button_clicked(self) -> None:
        if self.paint_tab_history:
            action = list(self.paint_tab_history[0])[0]
            change_item = action[2][0]
            try:
                key, value = change_item[0], change_item[1]
                node_type = type(value).__name__
                node_id = key

            except Exception:
                node_type = type(change_item).__name__
                node_id = action[1]

            log(f'Undo action "{action[0]} {node_type} with ID {node_id}".', LOG_UNDO_ACTION)

            self.last_paint_data = deepcopy(self.paint_data)
            self.paint_data = dictdiffer.revert(self.paint_tab_history[-1], self.paint_data)

            del self.paint_tab_history[-1]
            save_paint(self.iid, self.paint_data)
            self.load_paint_tab()


    def paint_tab_paint_line(self, node) -> None:
        pen = QPen()

        pen.setWidth(node.size)
        pen.setColor(node.color)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)

        path = QPainterPath(QPointF(*node.coordinates[0]))
        for point in node.coordinates[1:]:
            path.quadTo(*[QPointF(*point)] * 2)

        self.paint_tab_actual_item = self.paint_graphicsscene.addPath(
            path,
            pen=pen
        )
        
        self.paint_tab_actual_item.iid = copy(self.paint_tab_actual_object_id)


    def paint_tab_paint_rectangle(self, node) -> None:
        pen = QPen()
        brush = QBrush()

        pen.setWidth(node.outline_size)
        pen.setColor(node.outline_color)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)

        brush.setStyle(Qt.SolidPattern)
        brush.setColor(QColor(node.fill_color))

        path = QPainterPath()
        path.addRoundedRect(self.paint_tab_node_to_rect(node), 1, 1)

        self.paint_tab_actual_item = self.paint_graphicsscene.addPath(
            path,
            pen=pen,
            brush=brush
        )

        self.paint_tab_actual_item.iid = copy(self.paint_tab_actual_object_id)


    def paint_tab_paint_ellipse(self, node) -> None:
        pen = QPen()
        brush = QBrush()

        pen.setWidth(node.outline_size)
        pen.setColor(QColor(node.outline_color))

        brush.setStyle(Qt.SolidPattern)
        brush.setColor(QColor(node.fill_color))

        if node.coordinates[1][1] > node.coordinates[0][1]:
            top_left, bottom_right = QPoint(*node.coordinates[1]), QPoint(*node.coordinates[0])

        else:
            top_left, bottom_right = QPoint(*node.coordinates[0]), QPoint(*node.coordinates[1])

        self.paint_tab_actual_item = self.paint_graphicsscene.addEllipse(
            QRect(
                top_left,
                bottom_right
            ),
            pen=pen,
            brush=brush
        )

        self.paint_tab_actual_item.iid = copy(self.paint_tab_actual_object_id)


    def paint_tab_paint_point(self, node) -> None:
        pen = QPen()
        brush = QBrush()

        pen.setWidth(0)
        pen.setColor(QColor(node.color))

        brush.setStyle(Qt.SolidPattern)
        brush.setColor(QColor(node.color))

        top_left, bottom_right = QPoint(*node.coordinate) - QPoint(*((node.size / 2,) * 2)), QPoint(*node.coordinate) + QPoint(*((node.size / 2,) * 2))
        self.paint_tab_actual_item = self.paint_graphicsscene.addEllipse(
            QRect(
                top_left,
                bottom_right
            ),
            pen=pen,
            brush=brush
        )

        self.paint_tab_actual_item.iid = copy(self.paint_tab_actual_object_id)


    def paint_tab_paint_polygon(self, node) -> None:
        pen = QPen()
        brush = QBrush()

        pen.setWidth(node.outline_size)
        pen.setColor(QColor(node.outline_color))
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)

        brush.setStyle(Qt.SolidPattern)
        brush.setColor(QColor(node.fill_color))

        self.paint_tab_actual_item = self.paint_graphicsscene.addPolygon(
            QPolygon([QPoint(*point) for point in node.coordinates]),
            pen=pen,
            brush=brush
        )

        self.paint_tab_actual_item.iid = copy(self.paint_tab_actual_object_id)


    def paint_tab_paint_image(self, node) -> None:
        raw, size = get_image(node.hash)
        self.paint_tab_actual_item = self.paint_graphicsscene.addPixmap(
            QPixmap.fromImage(
                QImage(
                    raw,
                    *size,
                    QImage.Format_RGBA8888
                ).scaled(*node.size, Qt.KeepAspectRatio)
            )
        )
        
        self.paint_data[self.paint_tab_actual_object_id].size = self.paint_tab_actual_item.pixmap().size().toTuple()

        self.paint_tab_actual_item.setPos(QPointF(*node.coordinate))
        self.paint_tab_actual_item.iid = copy(self.paint_tab_actual_object_id)


    def paint_tab_on_graphicsview_pressed(self, event: QMouseEvent) -> None:
        self.last_paint_data = deepcopy(self.paint_data)

        self.paint_tab_only_pressed = True
        self.paint_tab_start_coordinates = self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple()
        self.paint_tab_last_coordinates = self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toPoint()

        match self.entries.get_activated_paint_mode(self.iid):
            case "selector":
                mouse_position = self.ui.paint_graphicsview.mapToScene(*event.position().toTuple())
                self.selected_item = self.paint_graphicsscene.itemAt(*self.ui.paint_graphicsview.mapToScene(event.position().toPoint()).toTuple(), self.ui.paint_graphicsview.viewportTransform())
                if not self.selected_item is None:
                    self.selected_item_relative_to_mouse_position = self.selected_item.pos() - mouse_position
                    self.selected_item_start_position = self.selected_item.pos()

                    node = self.paint_data[self.selected_item.iid]
                
                    if isinstance(node, ImageNode):
                        image_rect = QRect(node.coordinate[0], node.coordinate[1], node.size[0], node.size[1])
                        self.paint_tab_image_rect = image_rect

                        topleft_view = self.ui.paint_graphicsview.mapFromScene(image_rect.topLeft())
                        bottomright_view = self.ui.paint_graphicsview.mapFromScene(image_rect.bottomRight())

                        view_rect = QRect(topleft_view, bottomright_view)
                        self.paint_tab_resizer_rubber_band.setGeometry(view_rect)
                        self.paint_tab_resizer_rubber_band.show()

                        scene_position = self.ui.paint_graphicsview.mapToScene(event.pos()).toPoint()

                        self.paint_tab_grabbed_corner = self.paint_tab_get_corner_from_rect_by_position(
                            scene_position.x(),
                            scene_position.y(),
                            image_rect.x(),
                            image_rect.y(),
                            image_rect.width(),
                            image_rect.height()
                        )

                        if self.paint_tab_grabbed_corner is not None:
                            self.paint_tab_is_resizing = True

                            # Determine the fixed anchor corner (opposite to the grabbed corner)
                            x0, y0 = image_rect.x(), image_rect.y()
                            w0, h0 = image_rect.width(), image_rect.height()

                            if self.paint_tab_grabbed_corner == (x0, y0):
                                self.paint_tab_anchor = QPoint(x0 + w0, y0 + h0)

                            elif self.paint_tab_grabbed_corner == (x0 + w0, y0):
                                self.paint_tab_anchor = QPoint(x0, y0 + h0)

                            elif self.paint_tab_grabbed_corner == (x0, y0 + h0):
                                self.paint_tab_anchor = QPoint(x0 + w0, y0)

                            elif self.paint_tab_grabbed_corner == (x0 + w0, y0 + h0):
                                self.paint_tab_anchor = QPoint(x0, y0)

                            else:
                                self.paint_tab_anchor = QPoint(x0, y0)

                            self.paint_tab_initial_size = QSize(w0, h0)
                            self.paint_tab_initial_aspect = w0 / h0

                            grabbed_corner_scene = QPoint(*self.paint_tab_grabbed_corner)
                            self.paint_tab_resize_offset = scene_position - grabbed_corner_scene

                            raw_image, original_size = get_image(node.hash)
                            self.paint_tab_original_pixmap = QPixmap.fromImage(QImage(raw_image, *original_size, QImage.Format_RGBA8888))

                        else:
                            self.paint_tab_is_resizing = False
                            self.paint_tab_move_start_pos = scene_position
                            self.selected_item_relative_to_mouse_position = self.selected_item.pos() - scene_position

            case "pen":
                if self.entries.get_one_click_line_mode(self.iid):
                    new_id = self.paint_tab_get_new_id()

                    self.paint_data[new_id] = PointNode(
                        self.paint_tab_start_coordinates,
                        self.entries.get_line_color(self.iid),
                        self.entries.get_line_size(self.iid),
                    )

                    self.paint_tab_actual_object_id = new_id
                    self.paint_tab_only_pressed = False

                    self.paint_tab_paint_point(self.paint_data[new_id])

            case "polygon":
                if self.paint_tab_only_pressed and not self.paint_tab_is_polygon_unfinished:
                    self.paint_tab_is_polygon_unfinished = True

                    new_id = self.paint_tab_get_new_id()

                    self.paint_data[new_id] = LineNode(
                        [
                            self.paint_tab_start_coordinates,
                            self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple()
                        ],
                        self.entries.get_shape_outline_size(self.iid),
                        self.entries.get_shape_outline_color(self.iid),
                        False,
                    )

                    self.paint_tab_actual_object_id = new_id
                    self.paint_tab_only_pressed = False

                else:
                    self.paint_data[self.paint_tab_actual_object_id].coordinates.append(self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple())
                    self.paint_graphicsscene.removeItem(self.paint_tab_actual_item)
                    
                self.paint_tab_paint_line(self.paint_data[self.paint_tab_actual_object_id])

            case "image":
                if self.paint_tab_only_pressed:
                    path = Path(QFileDialog.getOpenFileName()[0])
                    image_hash = get_hash_from_image(path)
                    if not self.image_registry.is_image_imported(path):
                        import_image(path)
                        self.image_registry.register_image(image_hash)

                    self.image_registry.register_image_usage(image_hash, self.iid)

                    self.paint_tab_actual_object_id = self.paint_tab_get_new_id()
                    self.paint_data[self.paint_tab_actual_object_id] = ImageNode(
                        self.paint_tab_start_coordinates,
                        (50, 50),
                        image_hash
                    )

                    self.paint_tab_paint_image(self.paint_data[self.paint_tab_actual_object_id])
                    save_paint(self.iid, self.paint_data)


    def paint_tab_on_graphicsview_moved(self, event: QMouseEvent) -> None:
        match self.entries.get_activated_paint_mode(self.iid):
            case "selector":
                if isinstance(self.selected_item, (QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsPolygonItem, QGraphicsPathItem, QGraphicsEllipseItem)):
                    node = self.paint_data[self.selected_item.iid]
                    if hasattr(node, "is_eraser") and node.is_eraser:
                        pass

                    else:
                        if not self.paint_tab_is_resizing:
                            mouse_position = self.ui.paint_graphicsview.mapToScene(*event.position().toTuple())
                            self.selected_item.setPos(mouse_position + self.selected_item_relative_to_mouse_position)

                            if isinstance(self.paint_data[self.selected_item.iid], ImageNode):
                                new_rect = QRect(self.selected_item.pos().toPoint(), QSize(*self.paint_data[self.selected_item.iid].size))
                                self.paint_tab_resizer_rubber_band.setGeometry(new_rect)

                    
                    if isinstance(node, ImageNode):
                        if self.paint_tab_is_resizing:
                            scene_position = self.ui.paint_graphicsview.mapToScene(event.pos()).toPoint()
                            adjusted_point = scene_position - self.paint_tab_resize_offset

                            raw_rect = QRect(self.paint_tab_anchor, adjusted_point).normalized()
                            width = raw_rect.width()
                            heigth = raw_rect.height()
                            if heigth == 0:
                                heigth = 1

                            desired_aspect = self.paint_tab_initial_aspect
                            if width / heigth > desired_aspect:
                                new_width = int(heigth * desired_aspect)
                                new_height = heigth

                            else:
                                new_width = width
                                new_height = int(width / desired_aspect) if width > 0 else 1

                            x0, y0 = self.paint_tab_image_rect.x(), self.paint_tab_image_rect.y()
                            w0, h0 = self.paint_tab_initial_size.width(), self.paint_tab_initial_size.height()

                            if self.paint_tab_anchor == QPoint(x0, y0):  # anchor top left
                                new_rect = QRect(self.paint_tab_anchor, QSize(new_width, new_height))

                            elif self.paint_tab_anchor == QPoint(x0 + w0, y0):  # anchor top right
                                new_rect = QRect(QPoint(self.paint_tab_anchor.x() - new_width, self.paint_tab_anchor.y()), QSize(new_width, new_height))

                            elif self.paint_tab_anchor == QPoint(x0, y0 + h0):  # anchor bottom left
                                new_rect = QRect(QPoint(self.paint_tab_anchor.x(), self.paint_tab_anchor.y() - new_height), QSize(new_width, new_height))

                            elif self.paint_tab_anchor == QPoint(x0 + w0, y0 + h0):  # anchor bottom right
                                new_rect = QRect(QPoint(self.paint_tab_anchor.x() - new_width, self.paint_tab_anchor.y() - new_height), QSize(new_width, new_height))

                            else:
                                new_rect = QRect(self.paint_tab_anchor, QSize(new_width, new_height))

                            new_rect = new_rect.normalized()

                            node.coordinate = (new_rect.topLeft().x(), new_rect.topLeft().y())
                            node.size = (new_rect.width(), new_rect.height())
                            
                            topleft_view = self.ui.paint_graphicsview.mapFromScene(new_rect.topLeft())
                            bottomright_view = self.ui.paint_graphicsview.mapFromScene(new_rect.bottomRight())
                            view_rect = QRect(topleft_view, bottomright_view)
                            self.paint_tab_resizer_rubber_band.setGeometry(view_rect)
                            
                            if self.paint_tab_original_pixmap and not self.paint_tab_original_pixmap.isNull():
                                scaled_pixmap = self.paint_tab_original_pixmap.scaled(new_rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

                                self.selected_item.setPixmap(scaled_pixmap)
                                self.selected_item.setPos(new_rect.topLeft())

                        else:
                            mouse_position = self.ui.paint_graphicsview.mapToScene(event.pos()).toPoint()
                            new_position = QPoint(
                                mouse_position.x() + self.selected_item_relative_to_mouse_position.x(),
                                mouse_position.y() + self.selected_item_relative_to_mouse_position.y()
                            )

                            self.selected_item.setPos(new_position)
                            node.coordinate = (new_position.x(), new_position.y())

                            topleft_view = self.ui.paint_graphicsview.mapFromScene(new_position)
                            bottomright_view = self.ui.paint_graphicsview.mapFromScene(QPoint(new_position.x() + node.size[0], new_position.y() + node.size[1]))
                            view_rect = QRect(topleft_view, bottomright_view)
                            self.paint_tab_resizer_rubber_band.setGeometry(view_rect)
                        
            case "pen":
                if not self.entries.get_one_click_line_mode(self.iid):
                    if self.paint_tab_only_pressed:
                        new_id = self.paint_tab_get_new_id()

                        self.paint_data[new_id] = LineNode(
                            [
                                self.paint_tab_start_coordinates,
                                self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple()
                            ],
                            self.entries.get_line_size(self.iid),
                            self.entries.get_line_color(self.iid),
                            False
                        )

                        self.paint_tab_actual_object_id = new_id
                        self.paint_tab_only_pressed = False

                        self.paint_tab_paint_line(self.paint_data[self.paint_tab_actual_object_id])

                    else:
                        point = self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple()

                        self.paint_data[self.paint_tab_actual_object_id].coordinates.append(point)

                        path = self.paint_tab_actual_item.path()
                        path.quadTo(*[QPointF(*point)] * 2)

                        self.paint_tab_actual_item.setPath(path)

            case "eraser":
                if self.paint_tab_only_pressed:
                    new_id = self.paint_tab_get_new_id()

                    self.paint_data[new_id] = LineNode(
                        [
                            self.paint_tab_start_coordinates,
                            self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple()
                        ],
                        self.entries.get_eraser_size(self.iid),
                        "white",
                        True
                    )

                    self.paint_tab_actual_object_id = new_id
                    self.paint_tab_only_pressed = False

                else:
                    self.paint_data[self.paint_tab_actual_object_id].coordinates.append(self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple())
                    self.paint_graphicsscene.removeItem(self.paint_tab_actual_item)

                self.paint_tab_paint_line(self.paint_data[self.paint_tab_actual_object_id])

            case "rectangle":
                if self.paint_tab_only_pressed:
                    new_id = self.paint_tab_get_new_id()

                    self.paint_data[new_id] = RectangleNode(
                        [
                            self.paint_tab_start_coordinates,
                            self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple()
                        ],
                        self.entries.get_shape_outline_size(self.iid),
                        self.entries.get_shape_outline_color(self.iid),
                        self.entries.get_shape_fill_color(self.iid)
                    )

                    self.paint_tab_actual_object_id = new_id
                    self.paint_tab_only_pressed = False

                else:
                    self.paint_data[self.paint_tab_actual_object_id].coordinates[1] = self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple()
                    self.paint_graphicsscene.removeItem(self.paint_tab_actual_item)

                self.paint_tab_paint_rectangle(self.paint_data[self.paint_tab_actual_object_id])

            case "ellipse":
                if self.paint_tab_only_pressed:
                    new_id = self.paint_tab_get_new_id()

                    self.paint_data[new_id] = EllipseNode(
                        [
                            self.paint_tab_start_coordinates,
                            self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple()
                        ],
                        self.entries.get_shape_outline_size(self.iid),
                        self.entries.get_shape_outline_color(self.iid),
                        self.entries.get_shape_fill_color(self.iid)
                    )

                    self.paint_tab_actual_object_id = new_id
                    self.paint_tab_only_pressed = False

                else:
                    self.paint_data[self.paint_tab_actual_object_id].coordinates[1] = self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toTuple()
                    self.paint_graphicsscene.removeItem(self.paint_tab_actual_item)

                self.paint_tab_paint_ellipse(self.paint_data[self.paint_tab_actual_object_id])

        self.paint_tab_last_coordinates = self.ui.paint_graphicsview.mapToScene(*event.position().toTuple()).toPoint()


    def paint_tab_on_graphicsview_released(self, event: QMouseEvent) -> None:
        self.paint_tab_last_coordinates = None

        match self.entries.get_activated_paint_mode(self.iid):
            case "pen" | "eraser" | "rectangle" | "ellipse":
                save_paint(self.iid, self.paint_data)

            case "selector":
                if not self.selected_item is None:
                    node = self.paint_data[self.selected_item.iid]
                    if isinstance(node, ImageNode):
                        node.coordinate = self.selected_item.pos().toTuple()

                    elif isinstance(node, (LineNode, RectangleNode, EllipseNode, PolygonNode)):
                        if hasattr(node, "is_eraser") and node.is_eraser:
                            pass

                        else:
                            position_difference = (self.selected_item.pos() - self.selected_item_start_position).toTuple()
                            node.coordinates = [(point[0] + position_difference[0], point[1] + position_difference[1]) for point in node.coordinates]

                    elif isinstance(node, PointNode):
                        position_difference = (self.selected_item.pos() - self.selected_item_start_position).toTuple()
                        node.coordinate = (node.coordinate[0] + position_difference[0], node.coordinate[1] + position_difference[1])
                    
                    save_paint(self.iid, self.paint_data)

        self.paint_tab_update_history()


    def paint_tab_finish_polygon(self) -> None:
        self.paint_graphicsscene.removeItem(self.paint_tab_actual_item)
        self.paint_data[self.paint_tab_actual_object_id] = PolygonNode(
            self.paint_data[self.paint_tab_actual_object_id].coordinates,
            self.entries.get_shape_outline_size(self.iid),
            self.entries.get_shape_outline_color(self.iid),
            self.entries.get_shape_fill_color(self.iid),
        )

        self.paint_tab_paint_polygon(self.paint_data[self.paint_tab_actual_object_id])

        self.paint_tab_is_polygon_unfinished = False

        save_paint(self.iid, self.paint_data)


    def paint_tab_on_eraser_size_changed(self, size) -> None:
        self.entries.set_eraser_size(self.iid, size)


    def paint_tab_on_line_size_changed(self, size) -> None:
        self.entries.set_line_size(self.iid, size)


    def paint_tab_on_outline_size_changed(self, size) -> None:
        self.entries.set_shape_outline_size(self.iid, size)


    def general_tab_name_color_function(self, color: QColor) -> None:
        self.entries.set_name_color(self.iid, color.name())

        self.load_hierarchical_view()


    def text_tab_background_color_function(self, color: QColor) -> None:
        self.actual_text_bg_color = color.name()
        self.text_tab_on_text_formatted("bg_color")


    def text_tab_foreground_color_function(self, color: QColor) -> None:
        self.actual_text_fg_color = color.name()
        self.text_tab_on_text_formatted("fg_color")


    def paint_tab_line_settings_color_function(self, color: QColor) -> None:
        self.entries.set_line_color(self.iid, color.name(QColor.HexArgb))

    
    def paint_tab_shape_settings_fill_color_function(self, color: QColor) -> None:
        self.entries.set_shape_fill_color(self.iid, color.name(QColor.HexArgb))


    def paint_tab_shape_settings_outline_color_function(self, color: QColor) -> None:
        self.entries.set_shape_outline_color(self.iid, color.name(QColor.HexArgb))


    def paint_tab_node_to_rect(self, node) -> QRectF:
        if node.coordinates[1][1] > node.coordinates[0][1]:
            top_left, bottom_right = QPoint(*node.coordinates[1]), QPoint(*node.coordinates[0])

        else:
            top_left, bottom_right = QPoint(*node.coordinates[0]), QPoint(*node.coordinates[1])

        return QRectF(top_left, bottom_right)


    def paint_tab_get_corner_from_rect_by_position(self, x: int, y: int, rx: int, ry: int, rw: int, rh: int) -> tuple | None:
        corners = [(rx, ry), (rx + rw, ry), (rx, ry + rh), (rx + rw, ry + rh)]
        for corner in corners:
            cx, cy = corner
            if abs(x - cx) <= 5 and abs(y - cy) <= 5:
                return corner
            
        return None
    

    def general_tab_on_name_text_edited(self) -> None:
        if not self.dont_update_text: # prevent recursive calls
            self.entries.set_name_text(self.iid, self.ui.name_entry.text())

            self.hierarchical_view_save_scrollbar_values()
            self.load_hierarchical_view()


    def text_tab_on_text_edited(self) -> None:
        if not self.dont_update_text:
            self.entries.set_text(self.iid, self.ui.text_entry.toHtml())


    def set_button_status(self, button: QPushButton, button_name: str, enabled: bool) -> None:
        if enabled:
            button.setStyleSheet(f"""			   
                background-color: rgb(242, 242, 242);
                icon: url(:/ui/{button_name}{"Hover" if enabled else ""}.png);
                """)

        else:
            button.setStyleSheet("background-color: white;")


    def text_tab_on_text_selection_changed(self) -> None:
        self.set_button_status(self.ui.text_tab_bold_button, "bold", not self.ui.text_entry.fontWeight() == QFont.Normal)
        self.set_button_status(self.ui.text_tab_italic_button, "italic", self.ui.text_entry.fontItalic())
        self.set_button_status(self.ui.text_tab_underline_button, "underline", self.ui.text_entry.fontUnderline())
        self.set_button_status(self.ui.text_tab_overstrike_button, "overstrike", self.ui.text_entry.currentFont().strikeOut())

        self.set_color_button_color(self.ui.text_tab_background_color_button, "white" if self.ui.text_entry.textBackgroundColor().alpha() == 0 else self.ui.text_entry.textBackgroundColor().name())
        self.set_color_button_color(self.ui.text_tab_foreground_color_button, self.ui.text_entry.textColor().name())

        self.ui.text_tab_size_spinbox.setValue(self.ui.text_entry.fontPointSize())

        self.ui.text_tab_font_combobox.setCurrentFont(self.ui.text_entry.fontFamily())


    def text_tab_on_text_formatted(self, operation: str) -> None:   
        match operation:
            case "bold":
                self.ui.text_entry.setFontWeight(QFont.Bold if self.ui.text_entry.fontWeight() == QFont.Normal else QFont.Normal)

            case "italic":
                self.ui.text_entry.setFontItalic(not self.ui.text_entry.fontItalic())

            case "underline":
                self.ui.text_entry.setFontUnderline(not self.ui.text_entry.fontUnderline())

            case "overstrike":
                font = self.ui.text_entry.currentFont()
                font.setStrikeOut(not font.strikeOut())

                self.ui.text_entry.setCurrentFont(font)
    
            case "bg_color":
                self.ui.text_entry.setTextBackgroundColor(self.actual_text_bg_color)
            
            case "fg_color":
                self.ui.text_entry.setTextColor(self.actual_text_fg_color)

            case "size":
                self.ui.text_entry.setFontPointSize(self.actual_text_font_size)

            case "font":
                self.ui.text_entry.setFontFamily(self.ui.text_tab_font_combobox.currentFont())

        self.text_tab_on_text_selection_changed()
        self.entries.set_text(self.iid, self.ui.text_entry.toHtml())
            

    def on_text_spinbox_value_changed(self) -> None:
        self.actual_text_font_size =  self.ui.text_tab_size_spinbox.value()
        self.text_tab_on_text_formatted("size")


    def on_text_font_changed(self) -> None:
        if not self.dont_update_text:
            self.text_tab_on_text_formatted("font")


    def on_tab_change(self) -> None:
        self.settings.set_active_tab(self.ui.MainTabManager.currentIndex())


    def general_tab_on_tag_clicked(self, index: int) -> None:
        tags = self.entries.get_tags(self.iid)
        tags.pop(index)
        self.entries.set_tags(self.iid, tags)

        self.load_entries()
        self.load_general_tab()
        self.load_search_tab()
        

    def general_tab_on_insert_tag_clicked(self) -> None:
        self.entries.set_tags(self.iid, self.entries.get_tags(self.iid) + [AskTagDialog().tag_name])
        self.load_general_tab()
        self.load_search_tab()

        
    def general_tab_update_name_text_function(self, iid: str, text: str) -> None:
        self.entries.set_name_text(iid, text)

        self.hierarchical_view_save_scrollbar_values()
        self.load_hierarchical_view()

        self.load_general_tab()


    def on_save(self) -> None:
        self.entries.set_modification_time(self.iid, get_actual_time())


    def show_settings_dialog(self):
        SettingsDialog(self.settings, self.on_color_button_clicked, self.set_color_button_color)
        self.update_background()
        self.update_language()
        self.load_entry()


    def search_tab_update_search(self) -> None:
        names = [entry["name"]["text"] for entry in self.entries]
        ids = [entry["id"] for entry in self.entries]

        texts = []
        for entry in self.entries:
            document = QTextDocument()
            document.setHtml(entry["text"])
            texts.append(document.toPlainText())

        to_search = zip(names, texts, ids)
        results = []

        for name, text, iid in to_search:
            if self.ui.search_mode_combobox.currentText() == "name":
                data = name

            elif self.ui.search_mode_combobox.currentText() == "text":
                data = text

            else:
                data = name + text

            if self.ui.regex_checkbox.isChecked():
                if fullmatch(self.ui.search_entry.text().upper() if not self.ui.case_sensitive_checkbox.isChecked() else self.ui.search_entry.text(), data.upper() if not self.ui.case_sensitive_checkbox.isChecked() else data):
                    results.append((name, text, iid))

            else:
                if (self.ui.search_entry.text().upper() in data.upper()) if not self.ui.case_sensitive_checkbox.isChecked() else (self.ui.search_entry.text() in data):
                    results.append((name, text, iid))

        old_results = results
        results = []
        if self.ui.tags_combobox.currentText() != "":
            for result in old_results:
                if self.ui.tags_combobox.currentText() in self.entries.get_tags(result[2]):
                    results.append(result)

        else:
            results = old_results

        
        for i in reversed(range(self.search_layout.count())): 
            self.search_layout.itemAt(i).widget().setParent(None)

        for result in results:
            name, text, iid = result

            result_button = QPushButton()
            result_button.setObjectName(f"result_{iid}_{ID_GENERATOR.get_id()}")
            result_button.setText(f"Name: {name}\nText: {text}\nID: {iid}")
            result_button.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
            result_button.setStyleSheet("""
                QPushButton{
                    background-color: white;
                    text-align: left;
                    padding: 5px;
                }

                QPushButton:hover{
                    background-color: rgba(255, 255, 255, 150);
                }
            """)

            result_button.clicked.connect(partial(self.load_specific_entry, iid))

            self.search_layout.addWidget(result_button)


    def iterate_over_treeview(self, parent: QStandardItem) -> QStandardItem:
        def recurse(parent: QStandardItem):
            for row in range(parent.rowCount()):
                for column in range(parent.columnCount()):
                    child = parent.child(row, column)
                    yield child

                    if child.hasChildren():
                        yield from recurse(child)

        if parent is not None:
            yield from recurse(parent)


    def get_model_index_by_id(self, iid: str) -> QModelIndex:
        for item in self.iterate_over_treeview(self.hierarchical_view_model.invisibleRootItem()):
            if item.data(ID_ROLE) == iid:
                return item.index()


    def get_treeview_item_id_by_index(self, index: QModelIndex):
        return self.hierarchical_view_model.data(index, role=ID_ROLE)


    def get_used_entry_ids(self) -> list[str]:
        """
        return all used IDs
        """
        return sorted(entry["id"] for entry in self.entries)


    def get_first_id(self) -> str:
        """
        return the first ID
        """
        return str(min(int(iid) for iid in self.get_used_entry_ids()))


    def get_next_free_id(self, ids: list[str | int]) -> str:
        """
        return the next free ID
        """
        return 1 if not ids else str(max(int(iid) for iid in ids) + 1)


    def get_children_entry(self, parent_id: str) -> list[str]:
        """
        return the IDs of all children
        """
        return [entry["id"] for entry in self.entries if entry["parent"] == parent_id]


class DontUpdateText:
    def __init__(self, window: MainWindow) -> None:
        self.window = window


    def __enter__(self) -> None:
        self.window.dont_update_text = True


    def __exit__(self, *args) -> None:
        self.window.dont_update_text = False


class DontUpdateModificationTime:
    def __init__(self, window: MainWindow) -> None:
        self.window = window


    def __enter__(self) -> None:
        self.window.entries.on_save = lambda: False


    def __exit__(self, *args) -> None:
        self.window.entries.on_save = self.window.on_save


def main() -> None:
    # this fails if more then one instance exists
    try:
        MySingleton = SingleInstance()

    except SingleInstanceException:
        log("One instance is already running.\nExit")
        return # break the function to exit
    
    if "ddos" in sys.argv:
        delete_data()

    if not Path("data").is_dir():
        prepare_first_run()

    if not check_if_data_is_valid():
        log("data is invalid\nexit", LOG_FATAL_ERROR)
        return 

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)

    app.setFont(QFont("Segoe UI", 9, QFont.Normal))

    window = MainWindow(app)
    window.show()

    app.exec()


if __name__ == "__main__":
    if "profile" in sys.argv:
        log("Started profiling...", LOG_PROFILING)
        pr = cProfile.Profile()
        pr.enable()
        main()
        pr.disable()
        log("Profiling finished.", LOG_PROFILING)
        pr.dump_stats("stats")

    else:
        main()