import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
cursor.execute("INSERT INTO movies (title, year) VALUES (?, ?)", ("Inception", 2010))
conn.commit()

cursor.execute("SELECT * FROM movies WHERE year > 2000")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()


movies = session.query(Movie).filter(Movie.year > 2000).all()