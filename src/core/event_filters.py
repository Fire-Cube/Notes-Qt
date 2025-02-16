from PySide6.QtCore import QObject, QEvent, QRect
from PySide6.QtWidgets import QMainWindow

from shiboken6 import isValid

from constants import *

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

        return False
    

class GlobalEventFilter(QObject):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent


    def eventFilter(self, object, event: QEvent):
        if event.type() == QEvent.MouseButtonPress:
            global_position = event.globalPosition().toPoint()
            view_rect = self.parent.ui.paint_graphicsview.rect()
            view_top_left_global = self.parent.ui.paint_graphicsview.mapToGlobal(view_rect.topLeft())
            view_rect_global = QRect(view_top_left_global, view_rect.size())
            if not view_rect_global.contains(global_position):
                if self.parent.paint_tab_resizer_rubber_band is not None:
                    if isValid(self.parent.paint_tab_resizer_rubber_band):
                        self.parent.paint_tab_resizer_rubber_band.hide()
                        self.parent.paint_tab_is_resizing = False

        return super().eventFilter(self.parent, event)