import shutil
import orjson

from pathlib import Path

from storage.paint import create_new_paint
from storage.paths import DATA_DIR_PATH, ENTRIES_FILE_PATH, IMAGES_DIR_PATH, IMAGES_REGISTRY_FILE_PATH, SETTINGS_FILE_PATH
from storage.templates import ENTRY_TEMPLATE, SETTINGS_TEMPLATE, PAINT_TEMPLATE

def delete_data() -> None:
    shutil.rmtree(DATA_DIR_PATH)
    
    
def prepare_first_run() -> None:
    Path(IMAGES_DIR_PATH).mkdir(parents=True) # creates the full directory structure
    
    with open(ENTRIES_FILE_PATH, "wb") as entries_file:
        entries_file.write(orjson.dumps([ENTRY_TEMPLATE]))

    with open(IMAGES_REGISTRY_FILE_PATH, "wb") as images_registry_file:
        images_registry_file.write(orjson.dumps(PAINT_TEMPLATE))

    with open(SETTINGS_FILE_PATH, "wb") as settings_file:
        settings_file.write(orjson.dumps(SETTINGS_TEMPLATE))

    create_new_paint(ENTRY_TEMPLATE["id"])