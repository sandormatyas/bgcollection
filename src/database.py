from os import getenv

from sqlmodel import Session, create_engine

APP_DATA_PATH = getenv("FLET_APP_STORAGE_DATA")
APP_TEMP_PATH = getenv("FLET_APP_STORAGE_TEMP")
DB_URL = f"sqlite:///{APP_DATA_PATH}/bgcollection.db"
engine = create_engine(DB_URL)


def get_session() -> Session:
    """
    Create a new SQLAlchemy session.

    Returns:
        Session: A new SQLAlchemy session.
    """
    return Session(engine)
