import logging
from typing import List, Optional
from xml.etree import ElementTree

import requests
from pydantic import BaseModel

from src.config import settings
from src.models.board_game import BoardGame

logger = logging.getLogger(__name__)


class BGGSearchResult(BaseModel):
    """Model for a search result from BoardGameGeek."""

    id: str
    name: str
    year_published: Optional[int] = None


class BGGClient:
    """Client for interacting with the BoardGameGeek API."""

    BASE_URL = settings.get("BGG_API_V1_BASE_URL")  # type: ignore

    def search(self, query: str) -> List[BGGSearchResult]:
        """
        Search for board games on BoardGameGeek.

        Args:
            query (str): The search term for board games.

        Returns:
            bytes: The XML response from the BoardGameGeek API.
        """
        url = f"{self.BASE_URL}/search"
        params = {"search": query}
        response = requests.get(url, params=params)
        response.raise_for_status()

        search_results = self._parse_search_results(response.content)
        return search_results

    def get_game_details(self, game_id: str) -> BoardGame:
        """
        Get details of a specific board game by its ID.

        Args:
            game_id (str): The ID of the board game.

        Returns:
            bytes: The XML response containing the game details.
        """
        url = f"{self.BASE_URL}/game/{game_id}"
        response = requests.get(url)
        response.raise_for_status()

        game_details = self._parse_game_details(response.content)
        return game_details

    def _parse_search_results(self, xml_data: bytes) -> List[BGGSearchResult]:
        """
        Parse the XML search results.

        Args:
            xml_data (bytes): The XML data from the search response.

        Returns:
            list: A list of BGGSearchResult objects.
        """
        root = ElementTree.fromstring(xml_data)
        results = []
        for bg in root.findall("boardgame"):
            _id = bg.get("objectid")
            name = bg.findtext("name")
            year_published_elem = bg.findtext("yearpublished")

            if _id is not None and name is not None:
                year_published = (
                    int(year_published_elem)
                    if year_published_elem is not None
                    else None
                )
                results.append(
                    BGGSearchResult(id=_id, name=name, year_published=year_published)
                )
            else:
                logger.warning(
                    f"Missing data in search result: objectid={_id}, name={name}, yearpublished={year_published_elem}"
                )

        return results

    def _parse_game_details(self, xml_data: bytes) -> BoardGame:
        """
        Parse the XML game details.

        Args:
            xml_data (bytes): The XML data from the game details response.

        Returns:
            BGGGameDetails: A BGGGameDetails object with the parsed data.
        """
        root = ElementTree.fromstring(xml_data)
        bg = root.find("boardgame")
        if bg is None:
            logger.error("No boardgame element found in the XML data.")
            raise ValueError("Invalid XML data: No boardgame element found.")

        _id = bg.get("objectid")
        name = bg.findtext("name[@primary='true']")
        year_published = bg.findtext("yearpublished")
        min_players = bg.findtext("minplayers")
        max_players = bg.findtext("maxplayers")
        playing_time = bg.findtext("playingtime")
        min_playing_time = bg.findtext("minplaytime")
        max_playing_time = bg.findtext("maxplaytime")
        age = bg.findtext("age")
        description = bg.findtext("description")
        thumbnail = bg.findtext("thumbnail")
        original_image = bg.findtext("image")

        if _id is not None and name is not None:
            return BoardGame(
                id=_id,
                name=name,
                year_published=int(year_published) if year_published else None,
                min_players=int(min_players) if min_players else None,
                max_players=int(max_players) if max_players else None,
                playing_time=int(playing_time) if playing_time else None,
                min_playing_time=int(min_playing_time) if min_playing_time else None,
                max_playing_time=int(max_playing_time) if max_playing_time else None,
                age=int(age) if age else None,
                description=description,
                thumbnail=thumbnail,
                original_image=original_image,
            )

        raise ValueError(
            "Invalid XML data: Missing required fields in boardgame element."
        )
