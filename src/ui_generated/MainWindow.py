# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QFrame, QGraphicsView, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpinBox, QStackedWidget,
    QTabWidget, QTextEdit, QTreeView, QWidget)

from custom_widgets import FontComboBox
import ui_generated.main_window_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1237, 795)
        MainWindow.setMaximumSize(QSize(1237, 795))
        icon = QIcon()
        icon.addFile(u":/icon/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"/* QComboBox */\n"
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
"	image: url(:/theme/ComboBox.png);\n"
"}\n"
"\n"
"/* QTabWidget */\n"
"QTabWidget::pane {\n"
" 	background-color: rgba(253, 253, 253, 200);\n"
"	border-width: 0px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"	left: 5;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"	background-color: rgba(255, 255, 255, 200);\n"
"    border-width: 0px;\n"
"	padding: 10;\n"
"}\n"
"\n"
"QTabBar {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QTabBar::tab:hover "
                        "{\n"
"	border: 1px solid rgba(240, 240, 240, 50);\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
"	border: 1px solid gainsboro;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:focus, QPushButton:hover {\n"
"	border-color: rgb(198, 198, 198);\n"
"}\n"
"\n"
"/* QTreeView */\n"
"QTreeView {\n"
"	background-color: white;\n"
"	border-width: 0px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"	color: black;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"	image: url(:/theme/TreeViewOpen.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"	image: url(:/theme/TreeViewClose.png);\n"
"}\n"
"\n"
"/* QCheckBox */\n"
"QCheckBox::indicator {\n"
"	border: 1px solid rgb(198, 198, 198);\n"
"	border-radius: 3px;\n"
"    width: 22px;\n"
"    height: 22px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/theme/CheckBox.png);\n"
"}\n"
""
                        "\n"
"QCheckBox::indicator:checked:pressed {\n"
"	image: url(:/theme/CheckBoxPressed.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	image: url(:/theme/CheckBoxPressed.png);\n"
"}\n"
"\n"
"QCheckBox {\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	padding: 5px;\n"
"}\n"
"\n"
"/* QTextEdit */\n"
"QTextEdit {\n"
"	border: 1px solid gainsboro;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"/* QSpinBox */\n"
"QSpinBox {\n"
"	border: 1px solid gainsboro;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QSpinBox:focus, QSpinBox:hover {\n"
"	border-color: rgb(198, 198, 198);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"	image: url(:/theme/SpinBoxUp.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"	border: 1px solid rgb(220, 220, 220);\n"
"	border-rad"
                        "ius: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/theme/SpinBoxDown.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"/* QScrollBar Vertical */\n"
"QScrollBar:vertical {\n"
"    border: 6px solid transparent;\n"
"    margin: 14px 0px 14px 0px;\n"
"	width: 16px;\n"
"}\n"
"\n"
"QScrollBar:vertical:hover {\n"
"    border: 5px solid transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: gainsboro;\n"
"	border-radius: 2px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	image: url(:/theme/ScrollTop.png);\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"	image: url(:/theme/ScrollTopHover.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"	image: url(:/theme/ScrollTopPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	image: url(:/theme/ScrollBottom.png);\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "\n"
"QScrollBar::add-line:vertical:hover {\n"
"	image: url(:/theme/ScrollBottomHover.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"	image: url(:/theme/ScrollBottomPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"/* QScrollBar Horizontal */\n"
"QScrollBar:horizontal {\n"
"    border: 6px solid transparent;\n"
"    margin: 0px 14px 0px 14px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QScrollBar:horizontal:hover {\n"
"    border: 5px solid transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: gainsboro;\n"
"	border-radius: 2px;\n"
"	min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	image: url(:/theme/ScrollLeft.png);\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"	image: url(:/theme/ScrollLeftHover.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"	image: url(:/theme/ScrollL"
                        "eftPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	image: url(:/theme/ScrollRight.png);\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"	image: url(:/theme/ScrollRightHover.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"	image: url(:/theme/ScrollRightPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QAbstractItemView::corner {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	border: 1px solid gainsboro;\n"
"    border-radius: 3px;\n"
"	background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QToolTip {\n"
"	background-color: white;\n"
"	border-radius: 2px;\n"
"	border-color: transparent;\n"
"}")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.Europe))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.HierarchicalView = QTreeView(self.centralwidget)
        self.HierarchicalView.setObjectName(u"HierarchicalView")
        self.HierarchicalView.setGeometry(QRect(5, 7, 291, 781))
        self.HierarchicalView.setToolTipDuration(-5)
        self.HierarchicalView.setStyleSheet(u"")
        self.HierarchicalView.setFrameShadow(QFrame.Plain)
        self.HierarchicalView.setLineWidth(0)
        self.HierarchicalView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.HierarchicalView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.HierarchicalView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.HierarchicalView.setDragEnabled(False)
        self.HierarchicalView.setAlternatingRowColors(False)
        self.HierarchicalView.setIndentation(20)
        self.HierarchicalView.setAnimated(True)
        self.HierarchicalView.header().setVisible(False)
        self.HierarchicalView.header().setMinimumSectionSize(247)
        self.HierarchicalView.header().setDefaultSectionSize(247)
        self.HierarchicalView.header().setStretchLastSection(False)
        self.MainTabManager = QTabWidget(self.centralwidget)
        self.MainTabManager.setObjectName(u"MainTabManager")
        self.MainTabManager.setGeometry(QRect(300, 10, 931, 778))
        self.MainTabManager.setToolTipDuration(-5)
        self.MainTabManager.setStyleSheet(u"border-width:0px; border-radius:7px")
        self.general_tab = QWidget()
        self.general_tab.setObjectName(u"general_tab")
        self.name_entry = QLineEdit(self.general_tab)
        self.name_entry.setObjectName(u"name_entry")
        self.name_entry.setGeometry(QRect(10, 10, 751, 45))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.name_entry.setFont(font)
        self.name_entry.setToolTipDuration(-5)
        self.name_entry.setStyleSheet(u"	background-color: rgba(255, 255, 255, 150);")
        self.name_entry.setAlignment(Qt.AlignCenter)
        self.delete_entry_button = QPushButton(self.general_tab)
        self.delete_entry_button.setObjectName(u"delete_entry_button")
        self.delete_entry_button.setGeometry(QRect(820, 10, 50, 45))
        self.delete_entry_button.setToolTipDuration(-5)
        self.delete_entry_button.setAutoFillBackground(False)
        self.delete_entry_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/deleteHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon1 = QIcon()
        icon1.addFile(u":/ui/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_entry_button.setIcon(icon1)
        self.delete_entry_button.setIconSize(QSize(30, 30))
        self.insert_entry_button = QPushButton(self.general_tab)
        self.insert_entry_button.setObjectName(u"insert_entry_button")
        self.insert_entry_button.setGeometry(QRect(875, 10, 50, 45))
        self.insert_entry_button.setToolTipDuration(-5)
        self.insert_entry_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/newHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon2 = QIcon()
        icon2.addFile(u":/ui/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.insert_entry_button.setIcon(icon2)
        self.insert_entry_button.setIconSize(QSize(30, 30))
        self.name_color_button = QPushButton(self.general_tab)
        self.name_color_button.setObjectName(u"name_color_button")
        self.name_color_button.setGeometry(QRect(770, 10, 45, 45))
        self.name_color_button.setToolTipDuration(-5)
        self.name_color_button.setStyleSheet(u"border-radius: 22px; background-color: white;")
        self.name_color_button.setIconSize(QSize(30, 30))
        self.name_color_button.setCheckable(True)
        self.name_color_button.setChecked(False)
        self.label = QLabel(self.general_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 49, 16))
        self.label.setToolTipDuration(-5)
        self.label.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2 = QLabel(self.general_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 81, 16))
        self.label_2.setToolTipDuration(-5)
        self.label_2.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.general_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 101, 16))
        self.label_3.setToolTipDuration(-5)
        self.label_3.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.id_label = QLabel(self.general_tab)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(140, 60, 49, 16))
        self.id_label.setToolTipDuration(-5)
        self.id_label.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.creation_time_label = QLabel(self.general_tab)
        self.creation_time_label.setObjectName(u"creation_time_label")
        self.creation_time_label.setGeometry(QRect(140, 80, 161, 16))
        self.creation_time_label.setToolTipDuration(-5)
        self.creation_time_label.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.modification_time_label = QLabel(self.general_tab)
        self.modification_time_label.setObjectName(u"modification_time_label")
        self.modification_time_label.setGeometry(QRect(140, 100, 161, 16))
        self.modification_time_label.setToolTipDuration(-5)
        self.modification_time_label.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.insert_tag_button = QPushButton(self.general_tab)
        self.insert_tag_button.setObjectName(u"insert_tag_button")
        self.insert_tag_button.setGeometry(QRect(870, 142, 50, 45))
        self.insert_tag_button.setToolTipDuration(-5)
        self.insert_tag_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/newHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        self.insert_tag_button.setIcon(icon2)
        self.insert_tag_button.setIconSize(QSize(30, 30))
        self.MainTabManager.addTab(self.general_tab, "")
        self.text_tab = QWidget()
        self.text_tab.setObjectName(u"text_tab")
        self.text_entry = QTextEdit(self.text_tab)
        self.text_entry.setObjectName(u"text_entry")
        self.text_entry.setGeometry(QRect(7, 66, 917, 670))
        self.text_entry.setToolTipDuration(-5)
        self.text_entry.setStyleSheet(u"QFrame{	background-color: white;}\n"
"QScrollBar:vertical {\n"
"    border: 6px solid transparent;\n"
"    margin: 14px 0px 14px 0px;\n"
"	width: 16px;\n"
"}\n"
"\n"
"QScrollBar:vertical:hover {\n"
"    border: 5px solid transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: gainsboro;\n"
"	border-radius: 2px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	image: url(:/theme/ScrollTop.png);\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"	image: url(:/theme/ScrollTopHover.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"	image: url(:/theme/ScrollTopPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	image: url(:/theme/ScrollBottom.png);\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"	image: url(:/theme/ScrollBottomHover.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertic"
                        "al:pressed {\n"
"	image: url(:/theme/ScrollBottomPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"/* QScrollBar Horizontal */\n"
"QScrollBar:horizontal {\n"
"    border: 6px solid transparent;\n"
"    margin: 0px 14px 0px 14px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QScrollBar:horizontal:hover {\n"
"    border: 5px solid transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: gainsboro;\n"
"	border-radius: 2px;\n"
"	min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	image: url(:/theme/ScrollLeft.png);\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"	image: url(:/theme/ScrollLeftHover.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"	image: url(:/theme/ScrollLeftPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	image: url(:/theme/ScrollRight.png);\n"
"    subcontrol-positi"
                        "on: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"	image: url(:/theme/ScrollRightHover.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"	image: url(:/theme/ScrollRightPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QAbstractItemView::corner {\n"
"	background-color: transparent;\n"
"}")
        self.text_entry.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.text_entry.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.text_entry.setLineWrapMode(QTextEdit.NoWrap)
        self.text_entry.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.text_tab_bold_button = QPushButton(self.text_tab)
        self.text_tab_bold_button.setObjectName(u"text_tab_bold_button")
        self.text_tab_bold_button.setGeometry(QRect(10, 10, 50, 45))
        self.text_tab_bold_button.setToolTipDuration(-5)
        self.text_tab_bold_button.setStyleSheet(u"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon3 = QIcon()
        icon3.addFile(u":/ui/bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text_tab_bold_button.setIcon(icon3)
        self.text_tab_bold_button.setIconSize(QSize(30, 30))
        self.text_tab_italic_button = QPushButton(self.text_tab)
        self.text_tab_italic_button.setObjectName(u"text_tab_italic_button")
        self.text_tab_italic_button.setGeometry(QRect(65, 10, 50, 45))
        self.text_tab_italic_button.setToolTipDuration(-5)
        self.text_tab_italic_button.setStyleSheet(u"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon4 = QIcon()
        icon4.addFile(u":/ui/italic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text_tab_italic_button.setIcon(icon4)
        self.text_tab_italic_button.setIconSize(QSize(30, 30))
        self.text_tab_underline_button = QPushButton(self.text_tab)
        self.text_tab_underline_button.setObjectName(u"text_tab_underline_button")
        self.text_tab_underline_button.setGeometry(QRect(120, 10, 50, 45))
        self.text_tab_underline_button.setToolTipDuration(-5)
        self.text_tab_underline_button.setStyleSheet(u"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon5 = QIcon()
        icon5.addFile(u":/ui/underline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text_tab_underline_button.setIcon(icon5)
        self.text_tab_underline_button.setIconSize(QSize(30, 30))
        self.text_tab_overstrike_button = QPushButton(self.text_tab)
        self.text_tab_overstrike_button.setObjectName(u"text_tab_overstrike_button")
        self.text_tab_overstrike_button.setGeometry(QRect(175, 10, 50, 45))
        self.text_tab_overstrike_button.setToolTipDuration(-5)
        self.text_tab_overstrike_button.setStyleSheet(u"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon6 = QIcon()
        icon6.addFile(u":/ui/overstrike.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text_tab_overstrike_button.setIcon(icon6)
        self.text_tab_overstrike_button.setIconSize(QSize(30, 30))
        self.text_tab_foreground_color_button = QPushButton(self.text_tab)
        self.text_tab_foreground_color_button.setObjectName(u"text_tab_foreground_color_button")
        self.text_tab_foreground_color_button.setGeometry(QRect(480, 10, 45, 45))
        self.text_tab_foreground_color_button.setToolTipDuration(-5)
        self.text_tab_foreground_color_button.setStyleSheet(u"border-radius: 22px;background-color:white;")
        self.text_tab_foreground_color_button.setIconSize(QSize(30, 30))
        self.text_tab_size_spinbox = QSpinBox(self.text_tab)
        self.text_tab_size_spinbox.setObjectName(u"text_tab_size_spinbox")
        self.text_tab_size_spinbox.setGeometry(QRect(630, 17, 51, 31))
        self.text_tab_size_spinbox.setToolTipDuration(-5)
        self.text_tab_size_spinbox.setStyleSheet(u"	background-color: rgba(255, 255, 255, 150);")
        self.text_tab_size_spinbox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.text_tab_background_color_button = QPushButton(self.text_tab)
        self.text_tab_background_color_button.setObjectName(u"text_tab_background_color_button")
        self.text_tab_background_color_button.setGeometry(QRect(540, 10, 45, 45))
        self.text_tab_background_color_button.setToolTipDuration(-5)
        self.text_tab_background_color_button.setStyleSheet(u"border-radius: 22px;background-color:white;")
        self.text_tab_background_color_button.setIconSize(QSize(30, 30))
        self.text_tab_font_combobox = FontComboBox(self.text_tab)
        self.text_tab_font_combobox.setObjectName(u"text_tab_font_combobox")
        self.text_tab_font_combobox.setGeometry(QRect(270, 17, 161, 31))
        self.text_tab_font_combobox.setToolTipDuration(-5)
        self.text_tab_font_combobox.setStyleSheet(u"")
        self.MainTabManager.addTab(self.text_tab, "")
        self.paint_tab = QWidget()
        self.paint_tab.setObjectName(u"paint_tab")
        self.paint_tab_clear_button = QPushButton(self.paint_tab)
        self.paint_tab_clear_button.setObjectName(u"paint_tab_clear_button")
        self.paint_tab_clear_button.setGeometry(QRect(10, 10, 50, 45))
        self.paint_tab_clear_button.setToolTipDuration(-5)
        self.paint_tab_clear_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/deleteHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        self.paint_tab_clear_button.setIcon(icon1)
        self.paint_tab_clear_button.setIconSize(QSize(30, 30))
        self.paint_tab_enable_selector_button = QPushButton(self.paint_tab)
        self.paint_tab_enable_selector_button.setObjectName(u"paint_tab_enable_selector_button")
        self.paint_tab_enable_selector_button.setGeometry(QRect(65, 10, 50, 45))
        self.paint_tab_enable_selector_button.setToolTipDuration(-5)
        self.paint_tab_enable_selector_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/selectorHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon7 = QIcon()
        icon7.addFile(u":/ui/selector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paint_tab_enable_selector_button.setIcon(icon7)
        self.paint_tab_enable_selector_button.setIconSize(QSize(30, 30))
        self.paint_tab_enable_pen_button = QPushButton(self.paint_tab)
        self.paint_tab_enable_pen_button.setObjectName(u"paint_tab_enable_pen_button")
        self.paint_tab_enable_pen_button.setGeometry(QRect(125, 10, 50, 45))
        self.paint_tab_enable_pen_button.setToolTipDuration(-5)
        self.paint_tab_enable_pen_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/penHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon8 = QIcon()
        icon8.addFile(u":/ui/pen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paint_tab_enable_pen_button.setIcon(icon8)
        self.paint_tab_enable_pen_button.setIconSize(QSize(30, 30))
        self.paint_tab_enable_eraser_button = QPushButton(self.paint_tab)
        self.paint_tab_enable_eraser_button.setObjectName(u"paint_tab_enable_eraser_button")
        self.paint_tab_enable_eraser_button.setGeometry(QRect(180, 10, 50, 45))
        self.paint_tab_enable_eraser_button.setToolTipDuration(-5)
        self.paint_tab_enable_eraser_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/eraserHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon9 = QIcon()
        icon9.addFile(u":/ui/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paint_tab_enable_eraser_button.setIcon(icon9)
        self.paint_tab_enable_eraser_button.setIconSize(QSize(30, 30))
        self.stackedWidget = QStackedWidget(self.paint_tab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(460, 0, 341, 60))
        self.stackedWidget.setToolTipDuration(-5)
        self.stackedWidget.setStyleSheet(u"QWidget {\n"
"	background-color:  rgba( 255, 255, 255, 0);\n"
"}")
        self.empty_settings = QWidget()
        self.empty_settings.setObjectName(u"empty_settings")
        self.stackedWidget.addWidget(self.empty_settings)
        self.eraser_settings = QWidget()
        self.eraser_settings.setObjectName(u"eraser_settings")
        self.paint_tab_eraser_settings_size_spinbox = QSpinBox(self.eraser_settings)
        self.paint_tab_eraser_settings_size_spinbox.setObjectName(u"paint_tab_eraser_settings_size_spinbox")
        self.paint_tab_eraser_settings_size_spinbox.setGeometry(QRect(290, 17, 51, 31))
        self.paint_tab_eraser_settings_size_spinbox.setToolTipDuration(2)
        self.paint_tab_eraser_settings_size_spinbox.setStyleSheet(u"	background-color: rgba(255, 255, 255, 150);")
        self.paint_tab_eraser_settings_size_spinbox.setMinimum(1)
        self.paint_tab_eraser_settings_size_spinbox.setMaximum(150)
        self.stackedWidget.addWidget(self.eraser_settings)
        self.line_settings = QWidget()
        self.line_settings.setObjectName(u"line_settings")
        self.paint_tab_line_settings_size_spinbox = QSpinBox(self.line_settings)
        self.paint_tab_line_settings_size_spinbox.setObjectName(u"paint_tab_line_settings_size_spinbox")
        self.paint_tab_line_settings_size_spinbox.setGeometry(QRect(220, 17, 51, 31))
        self.paint_tab_line_settings_size_spinbox.setToolTipDuration(2)
        self.paint_tab_line_settings_size_spinbox.setStyleSheet(u"	background-color: rgba(255, 255, 255, 150);")
        self.paint_tab_line_settings_size_spinbox.setMinimum(1)
        self.paint_tab_line_settings_size_spinbox.setMaximum(150)
        self.paint_tab_line_settings_color_button = QPushButton(self.line_settings)
        self.paint_tab_line_settings_color_button.setObjectName(u"paint_tab_line_settings_color_button")
        self.paint_tab_line_settings_color_button.setGeometry(QRect(280, 10, 45, 45))
        self.paint_tab_line_settings_color_button.setToolTipDuration(2)
        self.paint_tab_line_settings_color_button.setStyleSheet(u"border-radius: 22px; background-color: white;")
        self.paint_tab_line_settings_color_button.setIconSize(QSize(30, 30))
        self.paint_tab_line_settings_one_click_line_checkbutton = QCheckBox(self.line_settings)
        self.paint_tab_line_settings_one_click_line_checkbutton.setObjectName(u"paint_tab_line_settings_one_click_line_checkbutton")
        self.paint_tab_line_settings_one_click_line_checkbutton.setGeometry(QRect(80, 17, 121, 31))
        self.paint_tab_line_settings_one_click_line_checkbutton.setToolTipDuration(-5)
        self.paint_tab_line_settings_one_click_line_checkbutton.setStyleSheet(u"	background-color: rgba(255, 255, 255, 150);")
        self.stackedWidget.addWidget(self.line_settings)
        self.shape_settings = QWidget()
        self.shape_settings.setObjectName(u"shape_settings")
        self.paint_tab_shape_settings_fill_color_button = QPushButton(self.shape_settings)
        self.paint_tab_shape_settings_fill_color_button.setObjectName(u"paint_tab_shape_settings_fill_color_button")
        self.paint_tab_shape_settings_fill_color_button.setGeometry(QRect(280, 10, 45, 45))
        self.paint_tab_shape_settings_fill_color_button.setToolTipDuration(2)
        self.paint_tab_shape_settings_fill_color_button.setStyleSheet(u"border-radius: 22px; background-color: white;")
        self.paint_tab_shape_settings_fill_color_button.setIconSize(QSize(30, 30))
        self.paint_tab_shape_settings_outline_size_spinbox = QSpinBox(self.shape_settings)
        self.paint_tab_shape_settings_outline_size_spinbox.setObjectName(u"paint_tab_shape_settings_outline_size_spinbox")
        self.paint_tab_shape_settings_outline_size_spinbox.setGeometry(QRect(150, 17, 51, 31))
        self.paint_tab_shape_settings_outline_size_spinbox.setToolTipDuration(2)
        self.paint_tab_shape_settings_outline_size_spinbox.setStyleSheet(u"	background-color: rgba(255, 255, 255, 150);")
        self.paint_tab_shape_settings_outline_size_spinbox.setMinimum(1)
        self.paint_tab_shape_settings_outline_size_spinbox.setMaximum(150)
        self.paint_tab_shape_settings_outline_color_button = QPushButton(self.shape_settings)
        self.paint_tab_shape_settings_outline_color_button.setObjectName(u"paint_tab_shape_settings_outline_color_button")
        self.paint_tab_shape_settings_outline_color_button.setGeometry(QRect(220, 10, 45, 45))
        self.paint_tab_shape_settings_outline_color_button.setToolTipDuration(2)
        self.paint_tab_shape_settings_outline_color_button.setStyleSheet(u"border-radius: 22px; background-color: white;")
        self.paint_tab_shape_settings_outline_color_button.setIconSize(QSize(30, 30))
        self.stackedWidget.addWidget(self.shape_settings)
        self.text_settings = QWidget()
        self.text_settings.setObjectName(u"text_settings")
        self.paint_tab_text_settings_overstrike_button = QPushButton(self.text_settings)
        self.paint_tab_text_settings_overstrike_button.setObjectName(u"paint_tab_text_settings_overstrike_button")
        self.paint_tab_text_settings_overstrike_button.setGeometry(QRect(170, 10, 50, 45))
        self.paint_tab_text_settings_overstrike_button.setToolTipDuration(-5)
        self.paint_tab_text_settings_overstrike_button.setStyleSheet(u"\n"
"							   QPushButton:hover {\n"
"							   background-color: rgb(242, 242, 242);\n"
"							   icon: url(:/ui/overstrikeHover.png);\n"
"							   }\n"
"\n"
"							   QPushButton {\n"
"							   background-color: white;\n"
"							   }\n"
"						   ")
        self.paint_tab_text_settings_overstrike_button.setIcon(icon6)
        self.paint_tab_text_settings_overstrike_button.setIconSize(QSize(30, 30))
        self.paint_tab_text_settings_underline_button = QPushButton(self.text_settings)
        self.paint_tab_text_settings_underline_button.setObjectName(u"paint_tab_text_settings_underline_button")
        self.paint_tab_text_settings_underline_button.setGeometry(QRect(115, 10, 50, 45))
        self.paint_tab_text_settings_underline_button.setToolTipDuration(-5)
        self.paint_tab_text_settings_underline_button.setStyleSheet(u"\n"
"							   QPushButton:hover {\n"
"							   background-color: rgb(242, 242, 242);\n"
"							   icon: url(:/ui/underlineHover.png);\n"
"							   }\n"
"\n"
"							   QPushButton {\n"
"							   background-color: white;\n"
"							   }\n"
"						   ")
        self.paint_tab_text_settings_underline_button.setIcon(icon5)
        self.paint_tab_text_settings_underline_button.setIconSize(QSize(30, 30))
        self.paint_tab_text_settings_italic_button = QPushButton(self.text_settings)
        self.paint_tab_text_settings_italic_button.setObjectName(u"paint_tab_text_settings_italic_button")
        self.paint_tab_text_settings_italic_button.setGeometry(QRect(60, 10, 50, 45))
        self.paint_tab_text_settings_italic_button.setToolTipDuration(-5)
        self.paint_tab_text_settings_italic_button.setStyleSheet(u"\n"
"							   QPushButton:hover {\n"
"							   background-color: rgb(242, 242, 242);\n"
"							   icon: url(:/ui/italicHover.png);\n"
"							   }\n"
"\n"
"							   QPushButton {\n"
"							   background-color: white;\n"
"							   }\n"
"						   ")
        self.paint_tab_text_settings_italic_button.setIcon(icon4)
        self.paint_tab_text_settings_italic_button.setIconSize(QSize(30, 30))
        self.paint_tab_text_settings_bold_button = QPushButton(self.text_settings)
        self.paint_tab_text_settings_bold_button.setObjectName(u"paint_tab_text_settings_bold_button")
        self.paint_tab_text_settings_bold_button.setGeometry(QRect(5, 10, 50, 45))
        self.paint_tab_text_settings_bold_button.setToolTipDuration(-5)
        self.paint_tab_text_settings_bold_button.setStyleSheet(u"\n"
"							   QPushButton:hover {\n"
"							   background-color: rgb(242, 242, 242);\n"
"							   icon: url(:/ui/boldHover.png);\n"
"							   }\n"
"\n"
"							   QPushButton {\n"
"							   background-color: white;\n"
"							   }\n"
"						   ")
        self.paint_tab_text_settings_bold_button.setIcon(icon3)
        self.paint_tab_text_settings_bold_button.setIconSize(QSize(30, 30))
        self.paint_tab_text_settings_font_combobox = FontComboBox(self.text_settings)
        self.paint_tab_text_settings_font_combobox.setObjectName(u"paint_tab_text_settings_font_combobox")
        self.paint_tab_text_settings_font_combobox.setGeometry(QRect(230, 17, 161, 31))
        self.paint_tab_text_settings_font_combobox.setToolTipDuration(-5)
        self.paint_tab_text_settings_font_combobox.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.text_settings)
        self.paint_tab_enable_rectangle_button = QPushButton(self.paint_tab)
        self.paint_tab_enable_rectangle_button.setObjectName(u"paint_tab_enable_rectangle_button")
        self.paint_tab_enable_rectangle_button.setGeometry(QRect(240, 10, 50, 45))
        self.paint_tab_enable_rectangle_button.setToolTipDuration(-5)
        self.paint_tab_enable_rectangle_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/rectangleHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon10 = QIcon()
        icon10.addFile(u":/ui/rectangle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paint_tab_enable_rectangle_button.setIcon(icon10)
        self.paint_tab_enable_rectangle_button.setIconSize(QSize(30, 30))
        self.paint_tab_enable_ellipse_button = QPushButton(self.paint_tab)
        self.paint_tab_enable_ellipse_button.setObjectName(u"paint_tab_enable_ellipse_button")
        self.paint_tab_enable_ellipse_button.setGeometry(QRect(295, 10, 50, 45))
        self.paint_tab_enable_ellipse_button.setToolTipDuration(-5)
        self.paint_tab_enable_ellipse_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/ellipseHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon11 = QIcon()
        icon11.addFile(u":/ui/ellipse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paint_tab_enable_ellipse_button.setIcon(icon11)
        self.paint_tab_enable_ellipse_button.setIconSize(QSize(30, 30))
        self.paint_tab_enable_polygon_button = QPushButton(self.paint_tab)
        self.paint_tab_enable_polygon_button.setObjectName(u"paint_tab_enable_polygon_button")
        self.paint_tab_enable_polygon_button.setGeometry(QRect(350, 10, 50, 45))
        self.paint_tab_enable_polygon_button.setToolTipDuration(-5)
        self.paint_tab_enable_polygon_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/polygonHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon12 = QIcon()
        icon12.addFile(u":/ui/polygon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paint_tab_enable_polygon_button.setIcon(icon12)
        self.paint_tab_enable_polygon_button.setIconSize(QSize(30, 30))
        self.paint_tab_export_button = QPushButton(self.paint_tab)
        self.paint_tab_export_button.setObjectName(u"paint_tab_export_button")
        self.paint_tab_export_button.setGeometry(QRect(870, 10, 50, 45))
        self.paint_tab_export_button.setToolTipDuration(-5)
        self.paint_tab_export_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/exportHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon13 = QIcon()
        icon13.addFile(u":/ui/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paint_tab_export_button.setIcon(icon13)
        self.paint_tab_export_button.setIconSize(QSize(30, 30))
        self.paint_tab_enable_image_button = QPushButton(self.paint_tab)
        self.paint_tab_enable_image_button.setObjectName(u"paint_tab_enable_image_button")
        self.paint_tab_enable_image_button.setGeometry(QRect(410, 10, 50, 45))
        self.paint_tab_enable_image_button.setToolTipDuration(-5)
        self.paint_tab_enable_image_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/imageHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon14 = QIcon()
        icon14.addFile(u":/ui/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paint_tab_enable_image_button.setIcon(icon14)
        self.paint_tab_enable_image_button.setIconSize(QSize(30, 30))
        self.paint_graphicsview = QGraphicsView(self.paint_tab)
        self.paint_graphicsview.setObjectName(u"paint_graphicsview")
        self.paint_graphicsview.setGeometry(QRect(7, 66, 917, 670))
        self.paint_graphicsview.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: 6px solid transparent;\n"
"    margin: 14px 0px 14px 0px;\n"
"	width: 16px;\n"
"}\n"
"\n"
"QScrollBar:vertical:hover {\n"
"    border: 5px solid transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: gray;\n"
"	border-radius: 2px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	image: url(:/theme/ScrollTop.png);\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"	image: url(:/theme/ScrollTopHover.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"	image: url(:/theme/ScrollTopPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	image: url(:/theme/ScrollBottom.png);\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"	image: url(:/theme/ScrollBottomHover.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"	image: url(:/theme/Scroll"
                        "BottomPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"/* QScrollBar Horizontal */\n"
"QScrollBar:horizontal {\n"
"    border: 6px solid transparent;\n"
"    margin: 0px 14px 0px 14px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QScrollBar:horizontal:hover {\n"
"    border: 5px solid transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: gray;\n"
"	border-radius: 2px;\n"
"	min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	image: url(:/theme/ScrollLeft.png);\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"	image: url(:/theme/ScrollLeftHover.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"	image: url(:/theme/ScrollLeftPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	image: url(:/theme/ScrollRight.png);\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"	image: url(:/theme/ScrollRightHover.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"	image: url(:/theme/ScrollRightPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar {\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QAbstractItemView::corner {\n"
"	background-color: transparent;\n"
"}")
        self.paint_graphicsview.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.paint_graphicsview.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.paint_graphicsview.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.paint_graphicsview.setRenderHints(QPainter.Antialiasing|QPainter.TextAntialiasing)
        self.paint_graphicsview.setDragMode(QGraphicsView.NoDrag)
        self.paint_graphicsview.setResizeAnchor(QGraphicsView.NoAnchor)
        self.paint_tab_undo_button = QPushButton(self.paint_tab)
        self.paint_tab_undo_button.setObjectName(u"paint_tab_undo_button")
        self.paint_tab_undo_button.setGeometry(QRect(810, 10, 50, 45))
        self.paint_tab_undo_button.setToolTipDuration(-5)
        self.paint_tab_undo_button.setStyleSheet(u"\n"
"					   QPushButton:hover {\n"
"					   background-color: rgb(242, 242, 242);\n"
"					   icon: url(:/ui/undoHover.png);\n"
"					   }\n"
"\n"
"					   QPushButton {\n"
"					   background-color: white;\n"
"					   }\n"
"				   ")
        icon15 = QIcon()
        icon15.addFile(u":/ui/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paint_tab_undo_button.setIcon(icon15)
        self.paint_tab_undo_button.setIconSize(QSize(30, 30))
        self.MainTabManager.addTab(self.paint_tab, "")
        self.search_tab = QWidget()
        self.search_tab.setObjectName(u"search_tab")
        self.search_entry = QLineEdit(self.search_tab)
        self.search_entry.setObjectName(u"search_entry")
        self.search_entry.setGeometry(QRect(10, 10, 341, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.search_entry.setFont(font1)
        self.search_entry.setToolTipDuration(-5)
        self.search_entry.setStyleSheet(u"	background-color: rgba(255, 255, 255, 150);")
        self.case_sensitive_checkbox = QCheckBox(self.search_tab)
        self.case_sensitive_checkbox.setObjectName(u"case_sensitive_checkbox")
        self.case_sensitive_checkbox.setGeometry(QRect(360, 10, 151, 31))
        self.case_sensitive_checkbox.setToolTipDuration(-5)
        self.case_sensitive_checkbox.setStyleSheet(u"")
        self.regex_checkbox = QCheckBox(self.search_tab)
        self.regex_checkbox.setObjectName(u"regex_checkbox")
        self.regex_checkbox.setGeometry(QRect(530, 10, 71, 31))
        self.regex_checkbox.setToolTipDuration(-5)
        self.regex_checkbox.setStyleSheet(u"")
        self.search_mode_combobox = QComboBox(self.search_tab)
        self.search_mode_combobox.addItem("")
        self.search_mode_combobox.addItem("")
        self.search_mode_combobox.addItem("")
        self.search_mode_combobox.setObjectName(u"search_mode_combobox")
        self.search_mode_combobox.setGeometry(QRect(640, 10, 101, 31))
        self.search_mode_combobox.setToolTipDuration(-5)
        self.search_mode_combobox.setStyleSheet(u"")
        self.tags_combobox = QComboBox(self.search_tab)
        self.tags_combobox.setObjectName(u"tags_combobox")
        self.tags_combobox.setGeometry(QRect(750, 10, 171, 31))
        self.tags_combobox.setToolTipDuration(-5)
        self.tags_combobox.setStyleSheet(u"")
        self.search_scroll_area = QScrollArea(self.search_tab)
        self.search_scroll_area.setObjectName(u"search_scroll_area")
        self.search_scroll_area.setGeometry(QRect(10, 50, 911, 681))
        self.search_scroll_area.setToolTipDuration(-5)
        self.search_scroll_area.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: 6px solid transparent;\n"
"    margin: 14px 0px 14px 0px;\n"
"	width: 16px;\n"
"}\n"
"\n"
"QScrollBar:vertical:hover {\n"
"    border: 5px solid transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color:gray;\n"
"	border-radius: 2px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	image: url(:/theme/ScrollTop.png);\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"	image: url(:/theme/ScrollTopHover.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"	image: url(:/theme/ScrollTopPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	image: url(:/theme/ScrollBottom.png);\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"	image: url(:/theme/ScrollBottomHover.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"	image: url(:/theme/ScrollB"
                        "ottomPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"/* QScrollBar Horizontal */\n"
"QScrollBar:horizontal {\n"
"    border: 6px solid transparent;\n"
"    margin: 0px 14px 0px 14px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QScrollBar:horizontal:hover {\n"
"    border: 5px solid transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: gray;\n"
"	border-radius: 2px;\n"
"	min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	image: url(:/theme/ScrollLeft.png);\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"	image: url(:/theme/ScrollLeftHover.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"	image: url(:/theme/ScrollLeftPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	image: url(:/theme/ScrollRight.png);\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"	image: url(:/theme/ScrollRightHover.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"	image: url(:/theme/ScrollRightPressed.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QAbstractItemView::corner {\n"
"	background-color: transparent;\n"
"}")
        self.search_scroll_area.setFrameShape(QFrame.NoFrame)
        self.search_scroll_area.setLineWidth(1)
        self.search_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.search_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.search_scroll_area.setWidgetResizable(True)
        self.search_scroll_area.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 895, 665))
        self.search_scroll_area.setWidget(self.scrollAreaWidgetContents_2)
        self.MainTabManager.addTab(self.search_tab, "")
        self.settings_button = QPushButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(1199, 8, 31, 31))
        self.settings_button.setStyleSheet(u"border-width:0px; border-radius: 12px; background-color: rgba(255, 255, 255, 200);")
        icon16 = QIcon()
        icon16.addFile(u":/ui/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon16)
        self.settings_button.setIconSize(QSize(25, 25))
        self.background_overlay = QFrame(self.centralwidget)
        self.background_overlay.setObjectName(u"background_overlay")
        self.background_overlay.setEnabled(False)
        self.background_overlay.setGeometry(QRect(0, 0, 1237, 795))
        self.background_overlay.setFrameShape(QFrame.NoFrame)
        self.background_overlay.setFrameShadow(QFrame.Plain)
        self.background_overlay.setLineWidth(0)
        self.blur_shield = QFrame(self.centralwidget)
        self.blur_shield.setObjectName(u"blur_shield")
        self.blur_shield.setEnabled(False)
        self.blur_shield.setGeometry(QRect(0, 0, 1237, 795))
        self.blur_shield.setFrameShape(QFrame.NoFrame)
        self.blur_shield.setFrameShadow(QFrame.Plain)
        self.blur_shield.setLineWidth(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.blur_shield.raise_()
        self.background_overlay.raise_()
        self.HierarchicalView.raise_()
        self.MainTabManager.raise_()
        self.settings_button.raise_()

        self.retranslateUi(MainWindow)

        self.MainTabManager.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Notes", None))
#if QT_CONFIG(tooltip)
        self.delete_entry_button.setToolTip(QCoreApplication.translate("MainWindow", u"delete", None))
#endif // QT_CONFIG(tooltip)
        self.delete_entry_button.setText("")
#if QT_CONFIG(tooltip)
        self.insert_entry_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>create new</p><p>press &quot;Shift&quot; to create a sub entry</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.insert_entry_button.setText("")
#if QT_CONFIG(tooltip)
        self.name_color_button.setToolTip(QCoreApplication.translate("MainWindow", u"Name Color", None))
#endif // QT_CONFIG(tooltip)
        self.name_color_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"creation time:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"modification time:", None))
        self.id_label.setText("")
        self.creation_time_label.setText("")
        self.modification_time_label.setText("")
#if QT_CONFIG(tooltip)
        self.insert_tag_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>create new</p><p>press &quot;Shift&quot; to create a sub entry</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.insert_tag_button.setText("")
        self.MainTabManager.setTabText(self.MainTabManager.indexOf(self.general_tab), QCoreApplication.translate("MainWindow", u"General", None))
#if QT_CONFIG(tooltip)
        self.text_tab_bold_button.setToolTip(QCoreApplication.translate("MainWindow", u"bold", None))
#endif // QT_CONFIG(tooltip)
        self.text_tab_bold_button.setText("")
#if QT_CONFIG(tooltip)
        self.text_tab_italic_button.setToolTip(QCoreApplication.translate("MainWindow", u"italic", None))
#endif // QT_CONFIG(tooltip)
        self.text_tab_italic_button.setText("")
#if QT_CONFIG(tooltip)
        self.text_tab_underline_button.setToolTip(QCoreApplication.translate("MainWindow", u"underline", None))
#endif // QT_CONFIG(tooltip)
        self.text_tab_underline_button.setText("")
#if QT_CONFIG(tooltip)
        self.text_tab_overstrike_button.setToolTip(QCoreApplication.translate("MainWindow", u"overstrike", None))
#endif // QT_CONFIG(tooltip)
        self.text_tab_overstrike_button.setText("")
#if QT_CONFIG(tooltip)
        self.text_tab_foreground_color_button.setToolTip(QCoreApplication.translate("MainWindow", u"text color", None))
#endif // QT_CONFIG(tooltip)
        self.text_tab_foreground_color_button.setText("")
#if QT_CONFIG(tooltip)
        self.text_tab_size_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"Text Size", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.text_tab_background_color_button.setToolTip(QCoreApplication.translate("MainWindow", u"background color", None))
#endif // QT_CONFIG(tooltip)
        self.text_tab_background_color_button.setText("")
#if QT_CONFIG(tooltip)
        self.text_tab_font_combobox.setToolTip(QCoreApplication.translate("MainWindow", u"Text Font", None))
#endif // QT_CONFIG(tooltip)
        self.MainTabManager.setTabText(self.MainTabManager.indexOf(self.text_tab), QCoreApplication.translate("MainWindow", u"Text", None))
#if QT_CONFIG(tooltip)
        self.paint_tab_clear_button.setToolTip(QCoreApplication.translate("MainWindow", u"delete all", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_clear_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_enable_selector_button.setToolTip(QCoreApplication.translate("MainWindow", u"select", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_enable_selector_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_enable_pen_button.setToolTip(QCoreApplication.translate("MainWindow", u"pen", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_enable_pen_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_enable_eraser_button.setToolTip(QCoreApplication.translate("MainWindow", u"eraser", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_enable_eraser_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_eraser_settings_size_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"line size", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.paint_tab_line_settings_size_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"line size", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.paint_tab_line_settings_color_button.setToolTip(QCoreApplication.translate("MainWindow", u"line color", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_line_settings_color_button.setText("")
        self.paint_tab_line_settings_one_click_line_checkbutton.setText(QCoreApplication.translate("MainWindow", u"One-Click Line", None))
#if QT_CONFIG(tooltip)
        self.paint_tab_shape_settings_fill_color_button.setToolTip(QCoreApplication.translate("MainWindow", u"fill color", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_shape_settings_fill_color_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_shape_settings_outline_size_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"outline size", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.paint_tab_shape_settings_outline_color_button.setToolTip(QCoreApplication.translate("MainWindow", u"outline color", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_shape_settings_outline_color_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_text_settings_overstrike_button.setToolTip(QCoreApplication.translate("MainWindow", u"overstrike", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_text_settings_overstrike_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_text_settings_underline_button.setToolTip(QCoreApplication.translate("MainWindow", u"underline", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_text_settings_underline_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_text_settings_italic_button.setToolTip(QCoreApplication.translate("MainWindow", u"italic", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_text_settings_italic_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_text_settings_bold_button.setToolTip(QCoreApplication.translate("MainWindow", u"bold", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_text_settings_bold_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_text_settings_font_combobox.setToolTip(QCoreApplication.translate("MainWindow", u"Text Font", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.paint_tab_enable_rectangle_button.setToolTip(QCoreApplication.translate("MainWindow", u"rectangle", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_enable_rectangle_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_enable_ellipse_button.setToolTip(QCoreApplication.translate("MainWindow", u"ellipse", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_enable_ellipse_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_enable_polygon_button.setToolTip(QCoreApplication.translate("MainWindow", u"polygon", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_enable_polygon_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_export_button.setToolTip(QCoreApplication.translate("MainWindow", u"export", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_export_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_enable_image_button.setToolTip(QCoreApplication.translate("MainWindow", u"image", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_enable_image_button.setText("")
#if QT_CONFIG(tooltip)
        self.paint_tab_undo_button.setToolTip(QCoreApplication.translate("MainWindow", u"export", None))
#endif // QT_CONFIG(tooltip)
        self.paint_tab_undo_button.setText("")
        self.MainTabManager.setTabText(self.MainTabManager.indexOf(self.paint_tab), QCoreApplication.translate("MainWindow", u"Paint", None))
#if QT_CONFIG(tooltip)
        self.case_sensitive_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Case Sensitive", None))
#endif // QT_CONFIG(tooltip)
        self.case_sensitive_checkbox.setText(QCoreApplication.translate("MainWindow", u"Case Sensitive", None))
        self.regex_checkbox.setText(QCoreApplication.translate("MainWindow", u"Regex", None))
        self.search_mode_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"name", None))
        self.search_mode_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"text", None))
        self.search_mode_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"all", None))

#if QT_CONFIG(tooltip)
        self.search_mode_combobox.setToolTip(QCoreApplication.translate("MainWindow", u"category", None))
#endif // QT_CONFIG(tooltip)
        self.search_mode_combobox.setCurrentText(QCoreApplication.translate("MainWindow", u"name", None))
#if QT_CONFIG(tooltip)
        self.tags_combobox.setToolTip(QCoreApplication.translate("MainWindow", u"tag", None))
#endif // QT_CONFIG(tooltip)
        self.tags_combobox.setCurrentText("")
        self.MainTabManager.setTabText(self.MainTabManager.indexOf(self.search_tab), QCoreApplication.translate("MainWindow", u"Search", None))
        self.settings_button.setText("")
    # retranslateUi

