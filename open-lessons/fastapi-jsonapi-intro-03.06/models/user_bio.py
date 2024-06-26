from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from .database import Base


class UserBio(Base):
    __tablename__ = "user_bio"
    birth_city = Column(String, nullable=False, default="", server_default="")
    favourite_movies = Column(String, nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    user = relationship(
        "User",
        back_populates="bio",
        uselist=False,
    )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f" birth_city={self.birth_city!r},"
            f" favourite_movies={self.favourite_movies!r},"
            f" user_id={self.user_id}"
            ")"
        )
