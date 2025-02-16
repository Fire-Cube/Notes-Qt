# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QWidget)
import ui_generated.settings_dialog_resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(572, 749)
        Dialog.setStyleSheet(u"/* QDialog */\n"
"QDialog {\n"
"	background-color: rgb(253, 253, 253);\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
"	border: 1px solid gainsboro;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-color: rgb(198, 198, 198);\n"
"}\n"
"\n"
"/* QComboBox */\n"
"QComboBox {\n"
"	background-color: white;\n"
"	border: 1px solid gainsboro;\n"
"    border-radius: 3px;\n"
"	selection-color: black;\n"
"}\n"
"\n"
"QListView{\n"
"	border: 1px solid rgb(198, 198, 198);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border-color: rgb(198, 198, 198);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/theme/ComboBox.png);\n"
"}\n"
"\n"
"QAbstractItemView::corner {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"/* QCheckBox */\n"
"QCheckBox::indicator {\n"
"	border: 1px solid gainsboro;\n"
"	border-radius: 3px;\n"
"    widt"
                        "h: 22px;\n"
"    height: 22px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border-color: rgb(198, 198, 198);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/ui/CheckBox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"	image: url(:ui/CheckBoxPressed.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	image: url(:/ui/CheckBoxPressed.png);\n"
"}\n"
"\n"
"QCheckBox {\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	padding: 5px;\n"
"}")
        self.language_combobox = QComboBox(Dialog)
        self.language_combobox.addItem("")
        self.language_combobox.addItem("")
        self.language_combobox.setObjectName(u"language_combobox")
        self.language_combobox.setGeometry(QRect(40, 50, 69, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 91, 16))
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 129, 471, 391))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.background1_button = QPushButton(self.gridLayoutWidget)
        self.background1_button.setObjectName(u"background1_button")
        self.background1_button.setMaximumSize(QSize(162, 108))
        self.background1_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/backgrounds/1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.background1_button.setIcon(icon)
        self.background1_button.setIconSize(QSize(131, 100))
        self.background1_button.setFlat(True)

        self.gridLayout.addWidget(self.background1_button, 0, 0, 1, 1)

        self.background5_button = QPushButton(self.gridLayoutWidget)
        self.background5_button.setObjectName(u"background5_button")
        self.background5_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/backgrounds/5.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.background5_button.setIcon(icon1)
        self.background5_button.setIconSize(QSize(131, 100))
        self.background5_button.setFlat(True)

        self.gridLayout.addWidget(self.background5_button, 1, 1, 1, 1)

        self.background2_button = QPushButton(self.gridLayoutWidget)
        self.background2_button.setObjectName(u"background2_button")
        self.background2_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/backgrounds/2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.background2_button.setIcon(icon2)
        self.background2_button.setIconSize(QSize(131, 100))
        self.background2_button.setFlat(True)

        self.gridLayout.addWidget(self.background2_button, 0, 1, 1, 1)

        self.background3_button = QPushButton(self.gridLayoutWidget)
        self.background3_button.setObjectName(u"background3_button")
        self.background3_button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/backgrounds/3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.background3_button.setIcon(icon3)
        self.background3_button.setIconSize(QSize(131, 100))
        self.background3_button.setFlat(True)

        self.gridLayout.addWidget(self.background3_button, 0, 2, 1, 1)

        self.background4_button = QPushButton(self.gridLayoutWidget)
        self.background4_button.setObjectName(u"background4_button")
        self.background4_button.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/backgrounds/4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.background4_button.setIcon(icon4)
        self.background4_button.setIconSize(QSize(131, 100))
        self.background4_button.setFlat(True)

        self.gridLayout.addWidget(self.background4_button, 1, 0, 1, 1)

        self.background6_button = QPushButton(self.gridLayoutWidget)
        self.background6_button.setObjectName(u"background6_button")
        self.background6_button.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/backgrounds/6.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.background6_button.setIcon(icon5)
        self.background6_button.setIconSize(QSize(131, 100))
        self.background6_button.setFlat(True)

        self.gridLayout.addWidget(self.background6_button, 1, 2, 1, 1)

        self.background7_button = QPushButton(self.gridLayoutWidget)
        self.background7_button.setObjectName(u"background7_button")
        self.background7_button.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/backgrounds/7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.background7_button.setIcon(icon6)
        self.background7_button.setIconSize(QSize(131, 100))
        self.background7_button.setFlat(True)

        self.gridLayout.addWidget(self.background7_button, 2, 0, 1, 1)

        self.background8_button = QPushButton(self.gridLayoutWidget)
        self.background8_button.setObjectName(u"background8_button")
        self.background8_button.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/backgrounds/8.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.background8_button.setIcon(icon7)
        self.background8_button.setIconSize(QSize(131, 100))
        self.background8_button.setFlat(True)

        self.gridLayout.addWidget(self.background8_button, 2, 1, 1, 1)

        self.background9_button = QPushButton(self.gridLayoutWidget)
        self.background9_button.setObjectName(u"background9_button")
        self.background9_button.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/backgrounds/9.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.background9_button.setIcon(icon8)
        self.background9_button.setIconSize(QSize(131, 100))
        self.background9_button.setFlat(True)

        self.gridLayout.addWidget(self.background9_button, 2, 2, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 91, 121, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 560, 101, 16))
        self.apply_image_button = QPushButton(Dialog)
        self.apply_image_button.setObjectName(u"apply_image_button")
        self.apply_image_button.setGeometry(QRect(20, 520, 75, 24))
        self.apply_color_button = QPushButton(Dialog)
        self.apply_color_button.setObjectName(u"apply_color_button")
        self.apply_color_button.setGeometry(QRect(20, 650, 75, 24))
        self.acryl_checkbox = QCheckBox(Dialog)
        self.acryl_checkbox.setObjectName(u"acryl_checkbox")
        self.acryl_checkbox.setGeometry(QRect(90, 598, 76, 31))
        self.color_button = QPushButton(Dialog)
        self.color_button.setObjectName(u"color_button")
        self.color_button.setGeometry(QRect(30, 590, 45, 45))
        self.color_button.setStyleSheet(u"border-radius: 22px; background-color: white;")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(107, 577, 37, 24))
        font = QFont()
        font.setPointSize(7)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: gray; border: solid; border-radius: 2px; border-color: gray; border-width: 1px; margin: 5px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.language_combobox.setItemText(0, QCoreApplication.translate("Dialog", u"English", None))
        self.language_combobox.setItemText(1, QCoreApplication.translate("Dialog", u"German", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Language", None))
        self.background1_button.setText("")
        self.background5_button.setText("")
        self.background2_button.setText("")
        self.background3_button.setText("")
        self.background4_button.setText("")
        self.background6_button.setText("")
        self.background7_button.setText("")
        self.background8_button.setText("")
        self.background9_button.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Background Images", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Background Color", None))
        self.apply_image_button.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.apply_color_button.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.acryl_checkbox.setText(QCoreApplication.translate("Dialog", u"Acryl", None))
        self.color_button.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Beta", None))
    # retranslateUi

