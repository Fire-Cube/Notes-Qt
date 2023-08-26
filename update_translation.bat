cd src

call pyside6-lupdate main.py .\designer\MainWindow.ui  .\designer\resources\main_window_resources.qrc -ts .\translations\main_window_de.ts
call pyside6-lupdate main.py .\designer\ImageSettingsDialog.ui -ts .\translations\image_settings_dialog_de.ts

cd ..