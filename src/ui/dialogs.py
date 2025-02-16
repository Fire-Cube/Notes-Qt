from typing import Callable
from functools import partial

from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

from ui_generated.SettingsDialog import Ui_Dialog as UI_SettingsDialog
from ui_generated.AskTagDialog import Ui_Dialog as UI_AskTagDialog

from storage_generated.settings import Settings

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

