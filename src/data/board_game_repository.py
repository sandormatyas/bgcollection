from typing import List

from sqlmodel import Session, select

from src.models.board_game import BoardGame


class BoardGameRepository:
    """
    A repository for managing board games.
    """

    def __init__(self, db_session: Session):
        self.__db_session = db_session

    def add_game(self, game: BoardGame):
        """
        Add a new board game to the repository.
        """
        self.__db_session.add(game)
        self.__db_session.commit()

    def get_game_by_id(self, game_id: str) -> BoardGame | None:
        """
        Retrieve a board game by its ID.
        """
        query = select(BoardGame).where(BoardGame.id == game_id)
        return self.__db_session.exec(query).first()

    def list_all_games(self) -> List[BoardGame]:
        """
        List all board games in the repository.
        """
        query = select(BoardGame)
        return list(self.__db_session.exec(query).all())
