from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Follower(Base):
    __tablename__ = 'followers'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    posts: Mapped[int]
    followers: Mapped[int]
    following: Mapped[int]
