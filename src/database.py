from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config import DB_NAME

engine = create_engine(f'sqlite:///{DB_NAME}.db')

Session = sessionmaker(bind=engine)

Base = declarative_base()
