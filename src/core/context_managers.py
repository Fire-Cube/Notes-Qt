class DontUpdateText:
    def __init__(self, window) -> None:
        self.window = window


    def __enter__(self) -> None:
        self.window.dont_update_text = True


    def __exit__(self, *args) -> None:
        self.window.dont_update_text = False


class DontUpdateModificationTime:
    def __init__(self, window) -> None:
        self.window = window


    def __enter__(self) -> None:
        self.window.entries.on_save = lambda: False


    def __exit__(self, *args) -> None:
        self.window.entries.on_save = self.window.on_save