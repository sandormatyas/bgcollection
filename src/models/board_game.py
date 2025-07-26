from typing import Optional

from sqlmodel import Field, SQLModel


class BoardGame(SQLModel, table=True):
    """
    Represents a board game in the collection.
    """

    __tablename__ = "board_games"  # type: ignore

    id: str = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    year_published: Optional[int] = Field(default=None, nullable=True)
    min_players: Optional[int] = Field(default=None, nullable=True)
    max_players: Optional[int] = Field(default=None, nullable=True)
    playing_time: Optional[int] = Field(default=None, nullable=True)
    min_playing_time: Optional[int] = Field(default=None, nullable=True)
    max_playing_time: Optional[int] = Field(default=None, nullable=True)
    age: Optional[int] = Field(default=None, nullable=True)
    description: Optional[str] = Field(default=None, nullable=True)
    thumbnail: Optional[str] = Field(default=None, nullable=True)
    original_image: Optional[str] = Field(default=None, nullable=True)
