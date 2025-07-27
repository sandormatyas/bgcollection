import flet as ft


class NavBar(ft.NavigationBar):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(destinations=[], **kwargs)
        self.page = page
        self.pages = {
            0: {
                "route": "/",
                "label": "Collection",
                "icon": ft.Icons.GAMES_OUTLINED,
                "selected_icon": ft.Icons.GAMES,
            },
            1: {
                "route": "/wishlist",
                "label": "Wishlist",
                "icon": ft.Icons.BOOKMARK_BORDER,
                "selected_icon": ft.Icons.BOOKMARK,
            },
            2: {
                "route": "/search",
                "label": "Search",
                "icon": ft.Icons.SEARCH,
                "selected_icon": ft.Icons.SEARCH_ROUNDED,
            },
        }
        for item in self.pages.values():
            self.destinations.append(
                ft.NavigationBarDestination(
                    icon=item["icon"],
                    label=item["label"],
                    selected_icon=item["selected_icon"],
                )
            )
        self.on_change = self._on_change

    def _on_change(self, e):
        # Why no button specific callback?
        selected_route = self.pages[e.control.selected_index]
        self.page.go(selected_route["route"])
