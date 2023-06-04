from pathlib import Path

DATA_DIR_PATH = Path("data")

ENTRIES_FILE_PATH = Path(DATA_DIR_PATH, "entries.json")

PAINT_DATA_DIR_PATH = Path(DATA_DIR_PATH, "paint")
IMAGES_DIR_PATH = Path(DATA_DIR_PATH, "paint/images")
IMAGES_REGISTRY_FILE_PATH = Path(IMAGES_DIR_PATH, "registry.json")

SETTINGS_FILE_PATH = Path(DATA_DIR_PATH, "settings.json")