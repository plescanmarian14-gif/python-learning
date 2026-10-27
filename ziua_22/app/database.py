from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,declarative_base
from starlette.middleware.sessions import Session

SQLALCHEMY_DATABASE_URL="sqlite:///./magazin.db"

engine=create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check-same_thread":False}
)
Session_Local = sessionmaker(autocommit=True, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db=Session_Local()
    try:
        yield db
    finally:
        db.close()