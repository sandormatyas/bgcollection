from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel

from src.database import engine


class BoardGame(SQLModel):
    """
    Represents a board game in the collection.
    """

    id: str = Field(index=True, unique=True)
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


class OwnedBoardGame(BoardGame, table=True):
    """
    Represents a board game owned by a user.
    """

    __tablename__ = "owned_board_games"  # type: ignore
    __table_args__ = {"extend_existing": True}

    uuid: UUID = Field(default_factory=uuid4, primary_key=True)


class WishlistedBoardGame(BoardGame, table=True):
    """
    Represents a board game in a user's wishlist.
    """

    __tablename__ = "wishlisted_board_games"  # type: ignore
    __table_args__ = {"extend_existing": True}

    uuid: UUID = Field(default_factory=uuid4, primary_key=True)


SQLModel.metadata.create_all(
    engine, checkfirst=True
)  # Create the table if it doesn't exist
