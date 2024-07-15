from sqlalchemy import Table
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import func

from db import engine

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True, nullable=False),
    Column("email", String(255), unique=True, nullable=True),
)


SQL = """
CREATE TABLE users
(
    id       SERIAL      NOT NULL,
    username VARCHAR(32) NOT NULL,
    email    VARCHAR(255),
    PRIMARY KEY (id),
    UNIQUE (username),
    UNIQUE (email)
);
"""


def create_table():
    # print("tables:", metadata.tables)
    # metadata.drop_all(engine)
    metadata.create_all(engine)


def insert_rows():

    stmt1 = insert(users_table).values(
        {
            users_table.c.username: "admin",
            users_table.c.email: "admin@admin.com",
        }
    )

    stmt2 = insert(users_table).values(
        [
            {
                users_table.c.username: "john",
                users_table.c.email: "john@example.com",
            },
            {
                users_table.c.username: "sam",
                users_table.c.email: None,
            },
            {
                users_table.c.username: "nick",
                users_table.c.email: None,
            },
        ]
    )

    with engine.connect() as conn:
        with conn.begin():
            conn.execute(stmt1)
            conn.execute(stmt2)


def update_rows():
    stmt = (
        update(users_table)
        .where(
            users_table.c.email.is_(None),
        )
        .values(
            {
                users_table.c.email: func.concat(users_table.c.username, "@ya.ru"),
            },
        )
    )

    with engine.connect() as conn:
        with conn.begin():
            conn.execute(stmt)


def main():
    # create_table()
    # insert_rows()
    update_rows()


if __name__ == "__main__":
    main()
