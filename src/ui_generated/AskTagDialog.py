# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AskTagDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import ui_generated.ask_tag_dialog_resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(411, 192)
        icon = QIcon()
        icon.addFile(u":/ui/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"/* QPushButton */\n"
"QPushButton {\n"
"	border: 1px solid gainsboro;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:focus, QPushButton:hover {\n"
"	border-color: rgb(198, 198, 198);\n"
"}\n"
"\n"
"/* QLineEdit */\n"
"QLineEdit {\n"
"	border: 1px solid gainsboro;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QLineEdit:focus, QLineEdit:hover {\n"
"	border-color: rgb(198, 198, 198);\n"
"}\n"
"\n"
"QObject {\n"
"	background-color: white;\n"
"	color: black;\n"
"}\n"
"\n"
"/* QComboBox */\n"
"QComboBox {\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"	border: 1px solid gainsboro;\n"
"    border-radius: 3px;\n"
"	selection-color: black;\n"
"}\n"
"\n"
"QComboBox:focus, QComboBox:hover {\n"
"	border-color: rgb(198, 198, 198);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-radius: 3px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/ui/ComboBox.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border: 1px solid gainsboro;\n"
"    border-radius: 3px;\n"
"	"
                        "background-color: rgb(240, 240, 240);\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 301, 16))
        self.tag_name_entry = QLineEdit(Dialog)
        self.tag_name_entry.setObjectName(u"tag_name_entry")
        self.tag_name_entry.setGeometry(QRect(10, 30, 381, 22))
        self.create_button = QPushButton(Dialog)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setGeometry(QRect(10, 60, 75, 24))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 301, 16))
        self.create_select_button = QPushButton(Dialog)
        self.create_select_button.setObjectName(u"create_select_button")
        self.create_select_button.setGeometry(QRect(100, 60, 91, 24))
        self.tag_combobox = QComboBox(Dialog)
        self.tag_combobox.setObjectName(u"tag_combobox")
        self.tag_combobox.setGeometry(QRect(10, 130, 121, 22))
        self.add_button = QPushButton(Dialog)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(10, 160, 75, 24))
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 100, 380, 1))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Tags", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Create new tag", None))
        self.create_button.setText(QCoreApplication.translate("Dialog", u"create", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Select tag", None))
        self.create_select_button.setText(QCoreApplication.translate("Dialog", u"create + select", None))
        self.add_button.setText(QCoreApplication.translate("Dialog", u"add", None))
    # retranslateUi

