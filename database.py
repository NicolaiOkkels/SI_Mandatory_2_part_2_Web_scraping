import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

result = cursor.execute("SELECT * FROM movies;")
print(result.fetchall())