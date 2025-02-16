from PySide6.QtCore import Signal, QRect
from PySide6.QtGui import QFontDatabase, QColor, Qt, QPen, QLinearGradient, QPainter
from PySide6.QtWidgets import QComboBox, QGraphicsRectItem, QWidget


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


class CustomLine(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(1)
        self.gradient_length = 20

    
    def paintEvent(self, event):
        painter = QPainter(self)
        width = self.width()
        height = self.height()
        
        gradient = QLinearGradient(0, 0, width, 0)
        
        base_color = QColor(198, 198, 198)
        
        start_stop = self.gradient_length / width if width > 0 else 0
        end_stop = (width - self.gradient_length) / width if width > 0 else 1

        gradient.setColorAt(0.0, QColor(base_color.red(), base_color.green(), base_color.blue(), 0))
        gradient.setColorAt(start_stop, QColor(base_color.red(), base_color.green(), base_color.blue(), 255))
        gradient.setColorAt(end_stop, QColor(base_color.red(), base_color.green(), base_color.blue(), 255))
        gradient.setColorAt(1.0, QColor(base_color.red(), base_color.green(), base_color.blue(), 0))
        
        y = (height - 1) // 2
        
        painter.fillRect(0, y, width, 1, gradient)