call python -m pip install -U pip
call python -m pip freeze > to-uninstall.txt
call python -m pip uninstall -r to-uninstall.txt -y
del to-uninstall.txt
call python -m pip install unidecode
call python -m pip install wheel
call python -m pip install -r requirements.txt