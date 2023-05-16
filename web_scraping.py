import requests
from bs4 import BeautifulSoup
import sqlite3
from pprint import pprint

# Connect to the database
connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

# Create the movies table
cursor.execute("CREATE TABLE IF NOT EXISTS movies(title TEXT, year INTEGER);")

# Web scraping

html = requests.get("https://www.imdb.com/search/title/?groups=top_100", headers={"Accept-Language": "en-US"}).text

parsed_html = BeautifulSoup(html, "lxml")

movie_names = parsed_html.find_all("h3", {"class": "lister-item-header"})

movies = {}

for movie in movie_names:
    title = movie.find("a").text
    year = movie.find("span", {"class": "lister-item-year text-muted unbold"}).text.strip('()')
    movies[title] = year

# Add to database
for title, year in movies.items():
    cursor.execute("INSERT INTO movies (title, year) VALUES (?, ?);", (title, year))

# Commit changes and close the connection
connection.commit()
connection.close()

pprint(movies)