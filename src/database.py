from sqlmodel import Session, create_engine

DB_URL = "sqlite:///./bgcollection.db"
engine = create_engine(DB_URL)


def get_session() -> Session:
    """
    Create a new SQLAlchemy session.

    Returns:
        Session: A new SQLAlchemy session.
    """
    return Session(engine)
