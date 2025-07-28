from typing import Callable

import flet as ft

from config import settings
from models.board_game import BoardGame


class BoardGameCard(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        board_game: BoardGame,
        on_remove: Callable,
        on_click: Callable,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.page = page
        self.board_game = board_game
        self.on_remove = on_remove
        self.click_callback = on_click
        self.border_radius = settings.COMPONENT_RADIUS  # type: ignore

        self.on_click = self._on_click
        self._render()

    def _render(self):
        """
        Render the contents of the board game card.
        This method can be overridden to customize the display.
        """
        self.content = ft.Stack(
            [
                ft.Image(
                    src=self.board_game.thumbnail,
                    fit=ft.ImageFit.CONTAIN,
                    width=settings.CARD_WIDTH,  # type: ignore
                    height=settings.CARD_HEIGHT,  # type: ignore
                ),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINED,
                            on_click=self._on_remove,
                            icon_color=settings.TEXT_COLOR,  # type: ignore
                            bgcolor=settings.BLACK_SEMI_TRANSPARENT,  # type: ignore
                            tooltip="Remove from collection",
                            scale=0.75,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Column(
                    [
                        ft.Container(
                            ft.Text(
                                self.board_game.name,
                                size=settings.FONT_MEDIUM,  # type: ignore
                                weight=ft.FontWeight.BOLD,
                                color=settings.TEXT_COLOR,  # type: ignore
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            padding=settings.COMPONENT_PADDING,  # type: ignore
                            bgcolor=settings.BLACK_SEMI_TRANSPARENT,  # type: ignore
                            alignment=ft.alignment.center,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        )

    def _on_remove(self, e):
        """
        Handle the removal of a board game from the collection.
        """
        self.on_remove(self.board_game)

    def _on_click(self, e):
        """
        Handle the click event on the card.
        This can be overridden to provide additional functionality.
        """
        self.click_callback(self.board_game)
