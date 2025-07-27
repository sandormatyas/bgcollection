import flet as ft
from sqlmodel import Session

from models.board_game import OwnedBoardGame, WishlistedBoardGame
from src.clients.bgg import BGGClient, BGGSearchResult
from src.config import settings
from src.repositories.board_games import BoardGameRepository


class SearchField(ft.TextField):
    def __init__(self, on_submit, **kwargs):
        super().__init__(label="Search Board Games", on_submit=on_submit, **kwargs)
        self.autofocus = True
        self.width = 500

    def clear(self):
        self.value = ""
        self.update()


class SearchResult(ft.Container):
    def __init__(
        self, game: BGGSearchResult, page: ft.Page, db_session: Session, **kwargs
    ):
        super().__init__(**kwargs)
        self.game = game
        self.page = page
        self.bgg_client = BGGClient()
        self.__owned_repo = BoardGameRepository(db_session, OwnedBoardGame)
        self.__wishlist_repo = BoardGameRepository(db_session, WishlistedBoardGame)
        self.game_in_collection = self._game_in_collection()
        self.game_in_wishlist = self._game_in_wishlist()

        self.bgcolor = settings.BLACK_SEMI_TRANSPARENT  # type: ignore
        self.border_radius = settings.COMPONENT_RADIUS  # type: ignore
        self.padding = settings.COMPONENT_PADDING  # type: ignore

        self._render()

    def _render(self):
        """
        Render the contents of the search result.
        This method can be overridden to customize the display.
        """
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(
                            self.game.name,
                            size=settings.FONT_MEDIUM,  # type: ignore
                            weight=ft.FontWeight.BOLD,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        ft.Text(
                            f"Year Published: {self.game.year_published}",
                            size=settings.FONT_SMALL,  # type: ignore
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    width=600,
                ),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.LIBRARY_ADD_CHECK
                            if self.game_in_collection
                            else ft.Icons.MY_LIBRARY_ADD_OUTLINED,
                            on_click=self._on_add_to_collection,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.BOOKMARK_ADDED
                            if self.game_in_wishlist
                            else ft.Icons.BOOKMARK_ADD_OUTLINED,
                            on_click=self._on_add_to_wishlist,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        self.page.update()  # type: ignore

    def _on_add_to_collection(self, e):
        if not self.game_in_collection:
            board_game = self.bgg_client.get_game_details(self.game.id)
            if board_game:
                self.__owned_repo.add(board_game)  # type: ignore
                self.game_in_collection = True
                self.page.open(  # type: ignore
                    ft.SnackBar(
                        ft.Text("Game added to your owned games collection!"),
                        duration=settings.SNACKBAR_DURATION_MS,  # type: ignore
                    )
                )
                self._render()

    def _on_add_to_wishlist(self, e):
        if not self.game_in_wishlist:
            board_game = self.bgg_client.get_game_details(self.game.id)
            if board_game:
                self.__wishlist_repo.add(board_game)  # type: ignore
                self.game_in_wishlist = True
                self.page.open(  # type: ignore
                    ft.SnackBar(
                        ft.Text("Game added to your wishlist!"),
                        duration=settings.SNACKBAR_DURATION_MS,  # type: ignore
                    )
                )
                self._render()

    def _game_in_collection(self):
        return self.__owned_repo.get(self.game.id) is not None

    def _game_in_wishlist(self):
        return self.__wishlist_repo.get(self.game.id) is not None
