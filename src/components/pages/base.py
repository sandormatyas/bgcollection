import flet as ft


class BasePage(ft.Container):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.expand = True
        self.padding = 16
