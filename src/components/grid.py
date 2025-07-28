import flet as ft

from components.card import BoardGameCard
from components.details import BoardGameDetails
from config import settings
from models.board_game import BoardGame
from repositories.board_games import BoardGameRepository


class BoardGameGrid(ft.GridView):
    def __init__(
        self, page: ft.Page, collection_repository: BoardGameRepository, **kwargs
    ):
        super().__init__(**kwargs)
        self.page = page
        self.collection_repository = collection_repository
        self.padding = settings.COMPONENT_PADDING  # type: ignore
        self.spacing = settings.COMPONENT_SPACING  # type: ignore
        self.runs_count = settings.GRID_COLUMNS  # type: ignore

        self.__repository = collection_repository

        self._populate_grid()

    def _populate_grid(self):
        """
        Populate the grid with board game cards.
        """
        self.controls = [
            BoardGameCard(
                page=self.page,  # type: ignore
                board_game=bg,
                on_remove=self._remove_item_from_grid,
                on_click=self._open_board_game_details,
            )
            for bg in self.__repository.list()
        ]
        self.page.update()  # type: ignore

    def _remove_item_from_grid(self, board_game: BoardGame):
        """
        Remove a board game from the grid.
        """
        self.__repository.remove(board_game.id)
        self.page.open(  # type: ignore
            ft.SnackBar(
                ft.Text(f"'{board_game.name}' removed from collection."),
                duration=settings.SNACKBAR_DURATION_MS,  # type: ignore
            )
        )
        self._populate_grid()

    def _open_board_game_details(self, board_game: BoardGame):
        """
        Open the details page for a board game.
        """
        self.page.open(  # type: ignore
            ft.BottomSheet(
                BoardGameDetails(self.page, board_game),  # type: ignore
                size_constraints=ft.BoxConstraints(
                    max_width=self.page.width - (settings.COMPONENT_PADDING * 4),  # type: ignore
                    max_height=self.page.window.height  # type: ignore
                    - (settings.COMPONENT_PADDING * 10),  # type: ignore
                ),
                is_scroll_controlled=True,
            )
        )
