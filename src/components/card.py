from typing import Callable

import flet as ft

from src.config import settings
from src.models.board_game import BoardGame


class BoardGameCard(ft.Container):
    def __init__(self, board_game: BoardGame, on_remove: Callable, **kwargs):
        super().__init__(**kwargs)
        self.board_game = board_game
        self.on_remove = on_remove
        self.border_radius = settings.COMPONENT_RADIUS  # type: ignore

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
