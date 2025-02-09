from PySide6.QtCore import Signal, QRect
from PySide6.QtGui import QFontDatabase, QColor, Qt, QPen
from PySide6.QtWidgets import QComboBox, QGraphicsRectItem


class FontComboBox(QComboBox):
    currentFontChanged = Signal(str)

    def __init__(self, *args) -> None:
        super(FontComboBox, self).__init__(*args)
        fontFamilies = QFontDatabase.families()
        for family in fontFamilies:
            self.addItem(family)

        self.currentTextChanged.connect(lambda: self.currentFontChanged.emit(self.currentText()))


    def currentFont(self) -> str:
        return self.currentText()


    def setCurrentFont(self, family_name: str) -> None:
        self.setCurrentIndex(self.findText(family_name))


class CustomRubberBand(QGraphicsRectItem):
    def __init__(self, parent=None) -> None:
        super().__init__(0, 0, 0, 0, parent)

        self.setPen(QPen(QColor("blue"), 1, Qt.DashLine))
        self.setBrush(QColor(0, 0, 255, 50))
        self.hide()

    def setGeometry(self, rect: QRect) -> None:
        self.setRect(rect)
