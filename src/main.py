import flet as ft

from components.nav import NavBar
from components.pages.collection import (
    OwnedGamesCollectionPage,
    WishlistedGamesCollectionPage,
)
from components.pages.search import SearchPage


def main(page: ft.Page):
    page.title = "Board Game Collection"
    page.scroll = ft.ScrollMode.AUTO

    content_container = ft.Container(expand=True)

    def route_change(_e):
        match page.route:
            case "/":
                content_container.content = OwnedGamesCollectionPage(page)
            case "/wishlist":
                content_container.content = WishlistedGamesCollectionPage(page)
            case "/search":
                content_container.content = SearchPage(page)
        page.update()

    page.add(content_container)

    page.on_route_change = route_change
    page.navigation_bar = NavBar(page)
    page.go("/")
    page.update()


ft.app(main)
