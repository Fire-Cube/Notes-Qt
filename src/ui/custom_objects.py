from typing import Callable

from PySide6.QtCore import QMargins, QModelIndex
from PySide6.QtGui import QPainter, QPainterPath, QPen, QBrush, QFont, QStandardItem
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QLineEdit

from constants import *

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