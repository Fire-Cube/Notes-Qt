import shutil
import orjson

from pathlib import Path

from storage.paint import create_new_paint
from storage.paths import DATA_DIR_PATH, ENTRIES_FILE_PATH, IMAGES_DIR_PATH, IMAGES_REGISTRY_FILE_PATH, SETTINGS_FILE_PATH
from storage.templates import ENTRY_TEMPLATE, SETTINGS_TEMPLATE, PAINT_TEMPLATE

from core.special_logging import log, LOG_INVALID_FILE, LOG_DATA_CHECKER_STATISTICS


def delete_data() -> None:
    shutil.rmtree(DATA_DIR_PATH)
    
    
def check_if_data_is_valid() -> bool:
    counter = 0
    errors = 0
    for path in Path(DATA_DIR_PATH).rglob("*.json"):
        try:
            with open(path, encoding="utf-8") as input_file:
                orjson.loads(input_file.read())

        except Exception as exception:
            log(f"File {path.relative_to(DATA_DIR_PATH)} is invalid. Error in line {exception.lineno} position {exception.pos}.", LOG_INVALID_FILE)
            errors += 1
        
        counter += 1

    log(f"Checked {counter} files. {counter - errors} / {counter} are valid.", LOG_DATA_CHECKER_STATISTICS)

    return errors < 1


def prepare_first_run() -> None:
    Path(IMAGES_DIR_PATH).mkdir(parents=True) # creates the full directory structure
    
    with open(ENTRIES_FILE_PATH, "wb") as entries_file:
        entries_file.write(orjson.dumps([ENTRY_TEMPLATE]))

    with open(IMAGES_REGISTRY_FILE_PATH, "wb") as images_registry_file:
        images_registry_file.write(orjson.dumps(PAINT_TEMPLATE))

    with open(SETTINGS_FILE_PATH, "wb") as settings_file:
        settings_file.write(orjson.dumps(SETTINGS_TEMPLATE))

    create_new_paint(ENTRY_TEMPLATE["id"])