EMPTY_HTML = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>

<head>
    <meta name="qrichtext" content="1" />
    <meta charset="utf-8" />
    <style type="text/css">
        p,
        li {
            white-space: pre-wrap;
        }

        hr {
            height: 1px;
            border-width: 0;
        }

        li.unchecked::marker {
            content: "\\2610";
        }

        li.checked::marker {
            content: "\\2612";
        }
        
    </style>
</head>

<body style=" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;">
    <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br/></p>
</body>

</html>
"""

SCROLL_AREA_STYLE_SHEET = """
QFrame {
    background-color: transparent;
}

QScrollBar:vertical {
    border: 6px solid transparent;
    margin: 14px 0px 14px 0px;
	width: 16px;
}

QScrollBar:vertical:hover {
    border: 5px solid transparent;
}

QScrollBar::handle:vertical {
    background-color:gray;
	border-radius: 2px;
	min-height: 25px;
}

QScrollBar::sub-line:vertical {
	image: url(:/theme/ScrollTop.png);
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover {
	image: url(:/theme/ScrollTopHover.png);
}

QScrollBar::sub-line:vertical:pressed {
	image: url(:/theme/ScrollTopPressed.png);
}

QScrollBar::add-line:vertical {
	image: url(:/theme/ScrollBottom.png);
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical:hover {
	image: url(:/theme/ScrollBottomHover.png);
}

QScrollBar::add-line:vertical:pressed {
	image: url(:/theme/ScrollBottomPressed.png);
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	background: none;
}

/* QScrollBar Horizontal */
QScrollBar:horizontal {
    border: 6px solid transparent;
    margin: 0px 14px 0px 14px;
	height: 16px;
}

QScrollBar:horizontal:hover {
    border: 5px solid transparent;
}

QScrollBar::handle:horizontal {
    background-color: gray;
	border-radius: 2px;
	min-width: 25px;
}

QScrollBar::sub-line:horizontal {
	image: url(:/theme/ScrollLeft.png);
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal:hover {
	image: url(:/theme/ScrollLeftHover.png);
}

QScrollBar::sub-line:horizontal:pressed {
	image: url(:/theme/ScrollLeftPressed.png);
}

QScrollBar::add-line:horizontal {
	image: url(:/theme/ScrollRight.png);
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover {
	image: url(:/theme/ScrollRightHover.png);
}

QScrollBar::add-line:horizontal:pressed {
	image: url(:/theme/ScrollRightPressed.png);
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
	background: none;
}

QScrollBar {
	background-color: transparent;
}

QAbstractItemView::corner {
	background-color: transparent;
}"""

ID_ROLE = 257
SELECTION_ROLE = 258

DISPLAY_ROLE = 0
EDIT_ROLE = 2
BACKGROUND_ROLE = 8

KEY_PRESS_EVENT = 6
KEY_RELEASE_EVENT = 7

UP_KEY = 16777235
DOWN_KEY = 16777237
SHIFT_KEY = 16777248
RETURN_KEY = 16777220