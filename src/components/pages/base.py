import flet as ft

from src.config import settings


class BasePage(ft.Container):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.expand = True
        self.padding = settings.COMPONENT_PADDING  # type: ignore
