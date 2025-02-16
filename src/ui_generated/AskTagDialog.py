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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(411, 101)
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
"/* QDialog */\n"
"QDialog {\n"
"	background-color: white;\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 301, 16))
        self.tag_name_entry = QLineEdit(Dialog)
        self.tag_name_entry.setObjectName(u"tag_name_entry")
        self.tag_name_entry.setGeometry(QRect(10, 30, 381, 22))
        self.submit_button = QPushButton(Dialog)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(10, 60, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Please enter a name for the new tag", None))
        self.submit_button.setText(QCoreApplication.translate("Dialog", u"add", None))
    # retranslateUi

