from sqlalchemy import select, text

from db import engine


def main():
    stmt = select(text("1 + 2"))
    # stmt = select(text("current_catalog"))
    with engine.connect() as conn:
        cur = conn.execute(stmt)

    # for res in cur.scalars():
    #     print(res)
    print(cur.scalar_one())


if __name__ == "__main__":
    main()
