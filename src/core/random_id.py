from os import urandom
from unidecode import unidecode

class IDGenerator():
    def __init__(self):
        self._ids = []


    def get_id(self):
        iid = unidecode(urandom(36).decode("latin-1")).replace("\n", "")
        while len(iid) < 5:
            iid = unidecode(urandom(36).decode("latin-1")).replace("\n", "")

        if iid not in self._ids:
            self._ids.append(iid)
            return iid