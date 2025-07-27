import flet as ft

from src.clients.bgg import BGGClient
from src.components.pages.base import BasePage
from src.components.search import SearchField, SearchResult
from src.database import get_session


class SearchPage(BasePage):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(page, **kwargs)
        self.__db_session = get_session()

        self.bgg_client = BGGClient()

        self.search_field = SearchField(on_submit=self.on_search_submit)
        self.results_column = ft.ListView(spacing=10)
        self.loading_indicator = ft.ProgressRing(
            color=ft.Colors.BLUE, tooltip="Loading...", visible=False
        )

        self.content = ft.Column(
            [self.search_field, self.loading_indicator, self.results_column],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_search_submit(self, e):
        query = e.control.value
        if query:
            self.loading_indicator.visible = True
            self.update()
            results = self.bgg_client.search(query)
            self.results_column.controls = [
                SearchResult(game=result, page=self.page, db_session=self.__db_session)  # type: ignore
                for result in results
            ]
            self.loading_indicator.visible = False
            self.update()
