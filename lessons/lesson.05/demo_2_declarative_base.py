from itertools import zip_longest
from typing import Sequence

from sqlalchemy import Table
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import func
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db import engine


class Base(DeclarativeBase):
    pass


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     username = Column(String(32), unique=True, nullable=False)
#     email = Column(String(255), unique=True, nullable=True)


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(String(255), unique=True)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"username={self.username!r}, "
            f"email={self.email!r}"
            ")"
        )

    def __repr__(self):
        return str(self)


def create_table():
    # print("tables:", metadata.tables)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert_rows(session: Session):
    user_admin = User(
        username="admin",
        email="admin@admin.com",
    )
    session.add(user_admin)

    users = [
        User(username=username, email=email)
        for username, email in zip_longest(
            ["john", "sam", "nick"],
            ["john@example.com"],
        )
    ]

    session.add_all(users)

    session.commit()


def update_rows(session: Session):
    stmt = (
        update(User)
        .where(
            User.email.is_(None),
        )
        .values(
            {
                User.email: func.concat(User.username, "@ya.ru"),
            },
        )
    )

    # session.execute(stmt)
    # session.commit()

    with session.begin():
        session.execute(stmt)


def fetch_all_users(session: Session) -> Sequence[User]:
    # stmt = select(User.id, User, text("1")).order_by(User.id)
    stmt = select(User).order_by(User.id)
    # result = session.execute(stmt)
    # return result.all()
    # return result.scalars().all()
    return session.scalars(stmt).all()


def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def get_user_by_username(session: Session, username: str) -> User | None:
    stmt = (
        # select user
        select(User)
        # filter by...
        .where(
            # lower all
            func.lower(User.username)
            # == username.lower()
            == func.lower(username)
        )
    )
    return session.scalars(stmt).first()


def select_users(session: Session):
    users = fetch_all_users(session)

    print("users:", users)
    for user in users:
        print(user)

    user_1 = get_user_by_id(session, 1)
    print("user_1", user_1)
    user_10 = get_user_by_id(session, 10)
    print("user_10", user_10)
    # if user_1 is not None:
    #     session.refresh(user_1)

    user_john = get_user_by_username(session, "john")
    print("user_john:", user_john)
    user_bob = get_user_by_username(session, "bob")
    print("user_bob:", user_bob)
    # if user_john is not None:
    #     user_john.username.strip()


def main():
    # create_table()

    with Session(engine) as session:
        # insert_rows(session)
        # update_rows(session)
        select_users(session)


if __name__ == "__main__":
    main()
