@REM update translation file with new or edited strings
call .\update_translation.bat

@REM open linguist
cd .\src\translations
if "%1" == "main" call pyside6-linguist main_window_de.ts
if "%1" == "image" call pyside6-linguist image_settings_dialog_de.ts

@REM compile translation
cd ..\..
call .\release_translation.bat

cd ..\..
@REM compile ui
call .\compile_ui.bat