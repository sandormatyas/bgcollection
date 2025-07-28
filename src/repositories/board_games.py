from typing import Generic, List, Type, TypeVar

from sqlmodel import Session, select

from models.board_game import BoardGame

T = TypeVar("T", bound=BoardGame)


class BoardGameRepository(Generic[T]):
    """
    A repository for managing board games.
    """

    def __init__(self, db_session: Session, model: Type[T]):
        self.__db_session = db_session
        self.model = model

    def add(self, game: T) -> None:
        """
        Add a new board game to the repository.
        """
        if isinstance(game, BoardGame) and not isinstance(game, self.model):
            # If game is a BoardGame but not of the specific type, convert it
            game = self.model(**game.model_dump())
        self.__db_session.add(game)
        self.__db_session.commit()

    def get(self, game_id: str) -> T | None:
        """
        Retrieve a board game by its ID.
        """
        query = select(self.model).where(self.model.id == game_id)
        return self.__db_session.exec(query).first()

    def list(self) -> List[T]:
        """
        List all board games in the repository.
        """
        query = select(self.model)
        return list(self.__db_session.exec(query).all())

    def remove(self, game_id: str):
        """
        Remove a board game from the repository.
        """
        game = self.get(game_id)
        if game:
            self.__db_session.delete(game)
            self.__db_session.commit()

    @classmethod
    def get_default(cls, model: Type[T]) -> "BoardGameRepository":
        """
        Get a default instance of the repository with a sqlite session.
        """
        from database import get_session

        session = get_session()
        return cls(session, model=model)
