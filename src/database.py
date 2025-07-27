from sqlmodel import Session, create_engine

from src.config import settings

engine = create_engine(settings.get("DB_URL"), echo=False)  # type: ignore


def get_session() -> Session:
    """
    Create a new SQLAlchemy session.

    Returns:
        Session: A new SQLAlchemy session.
    """
    return Session(engine)
