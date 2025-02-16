from time import localtime, strftime
from pathlib import Path

def get_actual_time() -> str:
    return strftime("%Y.%m.%d %H:%M:%S", localtime())


def shorten_path_to_program_directory(path: Path) -> Path:
    for parent in path.parents:
        if parent.name == "src":
            relative_path = path.relative_to(parent)
            return relative_path