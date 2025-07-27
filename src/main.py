import flet as ft

from components.pages.collections import (
    OwnedGamesCollectionPage,
    WishlistedGamesCollectionPage,
)
from src.components.pages.search import SearchPage
from src.components.nav import NavBar


def main(page: ft.Page):
    page.title = "Board Game Collection"
    page.scroll = ft.ScrollMode.AUTO

    content_container = ft.Container(expand=True)

    def route_change(e):
        print(f"Route changed to: {page.route}")
        match page.route:
            case "/":
                content_container.content = OwnedGamesCollectionPage(page)
            case "/wishlist":
                content_container.content = WishlistedGamesCollectionPage(page)
            case "/search":
                content_container.content = SearchPage(page)
        page.update()

    page.add(
        ft.Column(
            [
                content_container,
            ],
            expand=True,
        )
    )

    page.on_route_change = route_change
    page.navigation_bar = NavBar(page)
    page.go("/")
    page.update()


ft.app(main)
