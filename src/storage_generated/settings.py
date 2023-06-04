"""
This file is generated
Do not edit this directly
"""

import orjson

from types import NoneType

from storage.paths import SETTINGS_FILE_PATH

class Settings(dict):
    def save(self) -> None:
        with open(SETTINGS_FILE_PATH, "wb") as data_file:
            data_file.write(orjson.dumps(dict(self)))

    def get_background_image(self) -> int:
        return self['background_image']


    def set_background_image(self, data: int) -> None:
        if isinstance(data, int):
            self['background_image'] = data

        else:
            raise TypeError(f"settings.background_image: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_background_color(self) -> str:
        return self['background_color']


    def set_background_color(self, data: str) -> None:
        if isinstance(data, str):
            self['background_color'] = data

        else:
            raise TypeError(f"settings.background_color: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_background_acryl(self) -> bool:
        return self['background_acryl']


    def set_background_acryl(self, data: bool) -> None:
        if isinstance(data, bool):
            self['background_acryl'] = data

        else:
            raise TypeError(f"settings.background_acryl: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_background_mode(self) -> str:
        return self['background_mode']


    def set_background_mode(self, data: str) -> None:
        if isinstance(data, str):
            self['background_mode'] = data

        else:
            raise TypeError(f"settings.background_mode: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_language(self) -> str:
        return self['language']


    def set_language(self, data: str) -> None:
        if isinstance(data, str):
            self['language'] = data

        else:
            raise TypeError(f"settings.language: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_active_entry(self) -> str | None:
        return self['active_entry']


    def set_active_entry(self, data: str | None) -> None:
        if isinstance(data, (str,NoneType)):
            self['active_entry'] = data

        else:
            raise TypeError(f"settings.active_entry: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_active_tab(self) -> int:
        return self['active_tab']


    def set_active_tab(self, data: int) -> None:
        if isinstance(data, int):
            self['active_tab'] = data

        else:
            raise TypeError(f"settings.active_tab: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_vertical_scrollbar_value(self) -> int:
        return self['vertical_scrollbar_value']


    def set_vertical_scrollbar_value(self, data: int) -> None:
        if isinstance(data, int):
            self['vertical_scrollbar_value'] = data

        else:
            raise TypeError(f"settings.vertical_scrollbar_value: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_horizontal_scrollbar_value(self) -> int:
        return self['horizontal_scrollbar_value']


    def set_horizontal_scrollbar_value(self, data: int) -> None:
        if isinstance(data, int):
            self['horizontal_scrollbar_value'] = data

        else:
            raise TypeError(f"settings.horizontal_scrollbar_value: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_search_category(self) -> str:
        return self['search_tab']['category']


    def set_search_category(self, data: str) -> None:
        if isinstance(data, str):
            self['search_tab']['category'] = data

        else:
            raise TypeError(f"settings.search_tab.category: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    def get_color_chooser_custom_colors(self) -> list:
        return self['color_chooser_custom_colors']


    def set_color_chooser_custom_colors(self, data: list) -> None:
        if isinstance(data, list):
            self['color_chooser_custom_colors'] = data

        else:
            raise TypeError(f"settings.color_chooser_custom_colors: Type of value '{data!r}' {type(data)} is not in specification")

        self.save()

    
def load_settings() -> Settings:
    with open(SETTINGS_FILE_PATH, encoding="utf-8") as data_file:
        data = Settings()
        data.update(orjson.loads(data_file.read()))
        return data