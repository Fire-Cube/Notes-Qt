from PySide6.QtCore import Signal
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QPushButton


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