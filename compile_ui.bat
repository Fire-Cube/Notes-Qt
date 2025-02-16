@REM compile
cd src\designer
call pyside6-uic MainWindow.ui > ..\ui_generated\MainWindow.py
call pyside6-uic SettingsDialog.ui > ..\ui_generated\SettingsDialog.py
call pyside6-uic AskTagDialog.ui > ..\ui_generated\AskTagDialog.py

@REM replace a line in the compiled ui to make sure that it can become imported
cd ..\ui_generated\
powershell "(Get-Content MainWindow.py) -replace 'import main_window_resources_rc', 'import ui_generated.main_window_resources' | Out-File -encoding UTF8 MainWindow.py"
powershell "(Get-Content SettingsDialog.py) -replace 'import settings_dialog_resources_rc', 'import ui_generated.settings_dialog_resources' | Out-File -encoding UTF8 SettingsDialog.py
powershell "(Get-Content AskTagDialog.py) -replace 'import ask_tag_dialog_resources_rc', 'import ui_generated.ask_tag_dialog_resources' | Out-File -encoding UTF8 AskTagDialog.py

@REM compile resources
cd ..\designer\resources
call pyside6-rcc main_window_resources.qrc --no-compress -o ..\..\ui_generated\main_window_resources.py
call pyside6-rcc settings_dialog_resources.qrc --no-compress -o ..\..\ui_generated\settings_dialog_resources.py
call pyside6-rcc ask_tag_dialog_resources.qrc --no-compress -o ..\..\ui_generated\ask_tag_dialog_resources.py

@REM set working directory to main directory
cd ..\..\..