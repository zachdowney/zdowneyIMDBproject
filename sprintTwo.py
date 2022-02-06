import sqlite3
import requests
import pprint
import config
import sys
from typing import Tuple

base_url = "https://imdb-api.com/en/API/Top250TVs/"
user_url = "https://imdb-api.com/en/API/UserRatings/"
# https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c
# showed me how to use a secrets file
# https://www.youtube.com/watch?v=QovKok-2u9k
# showed me how to get data and what pprint is
response = requests.get(base_url + config.apiKey)
shows = response.json()


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = connection.cursor()   # get ready to read/write data
    return connection, cursor


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS shows (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        fullTitle TEXT NOT NULL,
        year INTEGER DEFAULT 0,
        crew TEXT NOT NULL,
        imDbRating REAL DEFAULT 0,
        imDbRatingCount INTEGER DEFAULT 0
        );''')


def fill_shows_table(cursor: sqlite3.Cursor):
    for i in range(0, 250):
        cursor.execute('''INSERT INTO shows (id, title,
                       fullTitle, year, crew, imDbRating, imDbRatingCount)
                       VALUES(?, ?, ?, ?, ?, ?, ?)''',
                       (shows['items'][i]['id'], shows['items'][i]['title'],
                        shows['items'][i]['fullTitle'], shows['items'][i]['year'],
                        shows['items'][i]['crew'], shows['items'][i]['imDbRating'],
                        shows['items'][i]['imDbRatingCount']))

    cursor.execute('SELECT rowid, * FROM shows')
    items = cursor.fetchall()

    for item in items:
        print(item)


def close_db(connection : sqlite3.Connection):
    connection.commit()   # make sure any changes get saved
    connection.close()


def main():
    conn, cursor = open_db('shows.db')
    print(type(conn))
    setup_db(cursor)
    fill_shows_table(cursor)
    close_db(conn)


if __name__ == '__main__':
    main()