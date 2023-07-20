"""
This file is generated
Do not edit this directly
"""

from copy import deepcopy

import orjson

from special_logging import LOG_ENTRY_CHANGES, log
from storage.paths import ENTRIES_FILE_PATH

class InvalidIDError(BaseException):
    pass


class Entries(list):
    on_save = None
    
    def save(self) -> None:
        with open(ENTRIES_FILE_PATH, "wb") as data_file:
            data_file.write(orjson.dumps(list(self)))

    def get_parent(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['parent'])


    def set_parent(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of parent changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['parent'] = data

        else:
            raise TypeError(f"entries.parent: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_id(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['id'])


    def set_id(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of id changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['id'] = data

        else:
            raise TypeError(f"entries.id: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_is_open(self, iid: str) -> bool:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['is_open'])


    def set_is_open(self, iid: str, data: bool) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of is_open changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, bool):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['is_open'] = data

        else:
            raise TypeError(f"entries.is_open: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_text(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['text'])


    def set_text(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of text changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['text'] = data

        else:
            raise TypeError(f"entries.text: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_activated_paint_mode(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['paint_tab']['activated_mode'])


    def set_activated_paint_mode(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of activated_paint_mode changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['paint_tab']['activated_mode'] = data

        else:
            raise TypeError(f"entries.paint_tab.activated_mode: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_eraser_size(self, iid: str) -> int:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['paint_tab']['eraser']['size'])


    def set_eraser_size(self, iid: str, data: int) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of eraser_size changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, int):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['paint_tab']['eraser']['size'] = data

        else:
            raise TypeError(f"entries.paint_tab.eraser.size: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_line_size(self, iid: str) -> int:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['paint_tab']['line']['line_size'])


    def set_line_size(self, iid: str, data: int) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of line_size changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, int):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['paint_tab']['line']['line_size'] = data

        else:
            raise TypeError(f"entries.paint_tab.line.line_size: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_line_color(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['paint_tab']['line']['line_color'])


    def set_line_color(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of line_color changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['paint_tab']['line']['line_color'] = data

        else:
            raise TypeError(f"entries.paint_tab.line.line_color: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_shape_fill_color(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['paint_tab']['shape']['fill_color'])


    def set_shape_fill_color(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of shape_fill_color changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['paint_tab']['shape']['fill_color'] = data

        else:
            raise TypeError(f"entries.paint_tab.shape.fill_color: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_shape_outline_color(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['paint_tab']['shape']['outline_color'])


    def set_shape_outline_color(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of shape_outline_color changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['paint_tab']['shape']['outline_color'] = data

        else:
            raise TypeError(f"entries.paint_tab.shape.outline_color: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_shape_outline_size(self, iid: str) -> int:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['paint_tab']['shape']['outline_size'])


    def set_shape_outline_size(self, iid: str, data: int) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of shape_outline_size changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, int):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['paint_tab']['shape']['outline_size'] = data

        else:
            raise TypeError(f"entries.paint_tab.shape.outline_size: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_position(self, iid: str) -> int:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['position'])


    def set_position(self, iid: str, data: int) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of position changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, int):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['position'] = data

        else:
            raise TypeError(f"entries.position: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_creation_time(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['times']['creation_time'])


    def set_creation_time(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of creation_time changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['times']['creation_time'] = data

        else:
            raise TypeError(f"entries.times.creation_time: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
    def get_modification_time(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['times']['modification_time'])


    def set_modification_time(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of modification_time changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['times']['modification_time'] = data

        else:
            raise TypeError(f"entries.times.modification_time: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
    def get_tags(self, iid: str) -> list:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['tags'])


    def set_tags(self, iid: str, data: list) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of tags changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, list):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['tags'] = data

        else:
            raise TypeError(f"entries.tags: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_name_text(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['name']['text'])


    def set_name_text(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of name_text changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['name']['text'] = data

        else:
            raise TypeError(f"entries.name.text: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    def get_name_color(self, iid: str) -> str:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise InvalidIDError(f"The ID: {iid} doesn't exists")

        return deepcopy(self[index]['name']['color'])


    def set_name_color(self, iid: str, data: str) -> None:
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        log("value of name_color changed", LOG_ENTRY_CHANGES)
        
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        if isinstance(data, str):
            index = None
            for i, entry in enumerate(self):
                if entry["id"] == iid:
                    index = i

            if index is None:
                raise InvalidIDError(f"The ID: {iid} doesn't exists")

            self[index]['name']['color'] = data

        else:
            raise TypeError(f"entries.name.color: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()
        
        self.on_save()
        
    

    def delete_entry(self, iid: str) -> None:
        if not isinstance(iid, str):
            raise TypeError(f"ID: '{iid!r}' has to be 'str' not {type(iid)}")

        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        if index is None:
            raise f"{index} is not in data (lenght: {len(self)})"

        self.pop(index)

        self.save()


    def delete_entry_recursive(self, iid: str) -> None:
        self.delete_entry(iid)
        is_clean = False
        while not is_clean:
            is_clean = True
            for entry in self:
                if not self.id_exists(entry["parent"]) and not entry["parent"] == "0":
                    is_clean = False
                    self.delete_entry(entry["id"])
                    print(entry["id"])


    def id_exists(self, iid: str) -> bool:
        index = None
        for i, entry in enumerate(self):
            if entry["id"] == iid:
                index = i

        return index is not None


def load_entries() -> Entries:
    with open(ENTRIES_FILE_PATH, encoding="utf-8") as data_file:
        data = Entries()
        entries_by_parent = {}
        for entry in orjson.loads(data_file.read()):
            if entry["parent"] not in entries_by_parent:
                entries_by_parent[entry["parent"]] = [entry]

            else:
                entries_by_parent[entry["parent"]].append(entry)

        entries_by_parent = dict(sorted(entries_by_parent.items()))
        for key in entries_by_parent:
            entries_by_parent[key].sort(key=lambda x: x["position"])
            data.extend(entries_by_parent[key])
            
        return data