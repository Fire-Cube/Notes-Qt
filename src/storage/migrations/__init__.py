from pathlib import Path

from orjson import loads, dumps

from special_logging import log, LOG_DATA_MIGRATIONS

from storage.migrations import paint_add_z_order
from storage.paths import PAINT_DATA_DIR_PATH

MIGRATORS = [
    ("paint_add_z_order", paint_add_z_order)
]

def migrate():
    for path in Path(PAINT_DATA_DIR_PATH).glob("*.json"):
        with open(path, "rb") as file:
            data = loads(file.read())

            changed_migrators = []
            for name, migrator in MIGRATORS:
                data, changed = migrator.migrate(data)
                if changed:
                    changed_migrators.append(name)

            if changed_migrators:
                log(f"Migrators ({', '.join(changed_migrators)}): {path} has changed", LOG_DATA_MIGRATIONS)
                
            else:
                log(f"Migrators: {path} has not changed", LOG_DATA_MIGRATIONS)

        with open(path, "wb") as file:
            file.write(dumps(data))