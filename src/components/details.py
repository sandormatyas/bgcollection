import html

import flet as ft

from config import settings
from models.board_game import BoardGame


class BoardGameDetails(ft.Container):
    def __init__(self, page: ft.Page, board_game: BoardGame, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.board_game = board_game
        self.expand = True
        self.padding = settings.COMPONENT_PADDING * 2  # type: ignore
        self.scroll = ft.ScrollMode.AUTO

        self._render()

    def _render(self):
        """
        Render the details of the board game.
        This method can be overridden to customize the display.
        """
        description = (
            html.unescape(self.board_game.description.replace("<br/>", "\n"))
            if self.board_game.description
            else "No description available."
        )
        self.content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(
                                    self.board_game.name,
                                    size=settings.FONT_TITLE,  # type: ignore
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Row(
                                    [
                                        ft.Icon(
                                            ft.Icons.CALENDAR_MONTH,
                                        ),
                                        ft.Text(
                                            f"{self.board_game.year_published}",
                                            size=settings.FONT_MEDIUM,  # type: ignore
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.Icon(
                                            ft.Icons.PEOPLE,
                                        ),
                                        ft.Text(
                                            f"{self.board_game.min_players} - {self.board_game.max_players} players",
                                            size=settings.FONT_MEDIUM,  # type: ignore
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.Icon(
                                            ft.Icons.TIMER,
                                        ),
                                        ft.Text(
                                            f"{self.board_game.min_playing_time} - {self.board_game.max_playing_time} minutes",
                                            size=settings.FONT_MEDIUM,  # type: ignore
                                        ),
                                    ]
                                ),
                            ],
                            width=300,
                        ),
                        ft.Image(
                            src=self.board_game.original_image,
                            fit=ft.ImageFit.CONTAIN,
                            width=300,
                            height=300,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=settings.COMPONENT_SPACING,  # type: ignore
                ),
                ft.Text(
                    "Description:",
                    size=settings.FONT_MEDIUM,  # type: ignore
                ),
                ft.Text(
                    description,
                    size=settings.FONT_SMALL,  # type: ignore
                    no_wrap=False,  # Enable wrapping
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        )
