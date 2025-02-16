# compile output
# nuitka-project: --verbose
# nuitka-project: --show-progress
# nuitka-project: --verbose-output=../build/verbose.log
# nuitka-project: --output-dir=../build
# nuitka-project: --report=../build/report.xml

# compile settings
# nuitka-project: --onefile
# nuitka-project: --lto=yes
# nuitka-project: --jobs=24
# nuitka-project: --plugin-enable=pyside6
# nuitka-project: --prefer-source-code
# nuitka-project: --follow-stdlib
# nuitka-project: --include-module=importlib._abc

# exe settings
# nuitka-project: --windows-icon-from-ico=designer/resources/icon.ico
# nuitka-project: --windows-company-name="Ben Fässler"
# nuitka-project: --windows-product-name=Notes
# nuitka-project: --windows-file-version=1.0

import os
import sys

os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"

if "profile" in sys.argv:
    import cProfile

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from tendo.singleton import SingleInstance, SingleInstanceException

from constants import *

from core.special_logging import LOG_PROFILING, LOG_FATAL_ERROR, log

from storage.helpers import delete_data, prepare_first_run, check_if_data_is_valid
from storage.migrations import migrate

from ui.main_window import MainWindow


def main() -> None:
    # this fails if more then one instance exists
    try:
        MySingleton = SingleInstance()

    except SingleInstanceException:
        log("One instance is already running.\nExit")
        return # break the function to exit
    
    if "ddos" in sys.argv:
        delete_data()

    if not Path("data").is_dir():
        prepare_first_run()

    if not check_if_data_is_valid():
        log("data is invalid\nexit", LOG_FATAL_ERROR)
        return 

    migrate()

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)

    app.setFont(QFont("Segoe UI", 9, QFont.Normal))

    window = MainWindow(app)
    window.show()

    app.exec()


if __name__ == "__main__":
    if "profile" in sys.argv:
        log("Started profiling...", LOG_PROFILING)
        pr = cProfile.Profile()
        pr.enable()
        main()
        pr.disable()
        log("Profiling finished.", LOG_PROFILING)
        pr.dump_stats("stats")

        import pyprof2calltree
        pyprof2calltree.convert("stats", "callgrind.out")

    else:
        main()