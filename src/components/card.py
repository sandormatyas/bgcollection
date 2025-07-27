from typing import Callable

import flet as ft

from src.models.board_game import BoardGame


class BoardGameCard(ft.Container):
    def __init__(self, board_game: BoardGame, on_remove: Callable, **kwargs):
        super().__init__(**kwargs)
        self.board_game = board_game
        self.on_remove = on_remove
        self.width = 250
        self.height = 250
        self.border_radius = 10

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
                    width=self.width,
                    height=self.height,
                ),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINED,
                            on_click=self._on_remove,
                            icon_color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLACK54,
                            tooltip="Remove from collection",
                            scale=0.75,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    spacing=1,
                ),
                ft.Column(
                    [
                        ft.Container(
                            ft.Text(
                                self.board_game.name,
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            padding=10,
                            bgcolor=ft.Colors.BLACK54,
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
