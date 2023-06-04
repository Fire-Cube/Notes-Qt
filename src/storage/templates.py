from tools import get_actual_time


ENTRY_TEMPLATE = {
    "parent": "0",
    "id": "1",
    "is_open": False,
    "paint_tab": {
        "activated_mode": "pen",
        "eraser": {
            "size": 10,
        },
        "line": {
            "line_size": 10,
            "line_color": "#000000"
        },
        "shape": {
            "outline_size": 10,
            "outline_color": "#000000",
            "fill_color": "#ffffff"
        }
    },
    "text": "",
    "position": 0,
    "times": {
        "creation_time": get_actual_time(),
        "modification_time": get_actual_time()
    },
    "tags": [],
    "name": {
        "text": "new",
        "color": "#ffffff"
    }
}

SETTINGS_TEMPLATE = {
    "background_image": 1,
    "background_color": "#ffffff",
    "background_acryl": True,
    "background_mode": "image",
    "language": "en",
    "active_entry": "1",
    "active_tab": 0,
    "vertical_scrollbar_value": 0,
    "horizontal_scrollbar_value": 0,
    "search_tab": {
        "category": "title"
    },
    "color_chooser_custom_colors": ["#ffffff"] * 16,

}

PAINT_TEMPLATE = {}