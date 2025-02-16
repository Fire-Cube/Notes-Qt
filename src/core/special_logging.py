import inspect

from pathlib import Path

from core.shared_functions import shorten_path_to_program_directory

LOG_ENTRY_CHANGES = 0
LOG_HIERARCHICAL_VIEW_UPDATES = 1
LOG_CHOOSEN_COLOR = 2
LOG_PROFILING = 3
LOG_UNDO_ACTION = 4
LOG_INVALID_FILE = 5
LOG_FATAL_ERROR = 6
LOG_DATA_CHECKER_STATISTICS = 7
LOG_DATA_MIGRATIONS = 8

DISABLED_CATEGORYS = ()

def get_caller_info():
    frame = inspect.stack()[2]
    return f"{shorten_path_to_program_directory(Path(frame.filename[:-3]))}.{frame.function} line {frame.lineno}"


def log(message, category):
    if category not in DISABLED_CATEGORYS:
        print(f"INFO ({get_caller_info()}): {message}")