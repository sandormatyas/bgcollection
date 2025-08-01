import flet as ft

from clients.bgg import BGGClient
from components.grid import BoardGameGrid
from components.pages.base import BasePage
from config import settings
from models.board_game import OwnedBoardGame, WishlistedBoardGame
from repositories.board_games import BoardGameRepository


class OwnedGamesCollectionPage(BasePage):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(page, **kwargs)
        self.bgg_client = BGGClient()

        self.collection_repository = BoardGameRepository.get_default(OwnedBoardGame)

        self.content = ft.Column(
            [
                ft.Text(
                    "My Board Games",
                    size=settings.FONT_LARGE,  # type: ignore
                    weight=ft.FontWeight.BOLD,
                ),
                BoardGameGrid(
                    page=page,
                    collection_repository=self.collection_repository,
                ),
            ]
        )


class WishlistedGamesCollectionPage(BasePage):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(page, **kwargs)
        self.bgg_client = BGGClient()

        self.collection_repository = BoardGameRepository.get_default(
            WishlistedBoardGame
        )

        self.content = ft.Column(
            [
                ft.Text(
                    "My Wishlist",
                    size=settings.FONT_LARGE,  # type: ignore
                    weight=ft.FontWeight.BOLD,
                ),
                BoardGameGrid(
                    page=page,
                    collection_repository=self.collection_repository,
                ),
            ]
        )
