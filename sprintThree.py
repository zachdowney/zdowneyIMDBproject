import sqlite3
import requests
import secrets


def create_popular_tv_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS popular_tv (
            id TEXT PRIMARY KEY,
            rank INTEGER DEFAULT 0,
            rankUpDown INTEGER DEFAULT 0,
            title TEXT NOT NULL,
            fullTitle TEXT NOT NULL,
            year INTEGER DEFAULT 0,
            crew TEXT NOT NULL,
            imDbRating REAL DEFAULT 0,
            imDbRatingCount INTEGER DEFAULT 0
            );''')


def create_movies_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            fullTitle TEXT NOT NULL,
            year INTEGER DEFAULT 0,
            crew TEXT NOT NULL,
            imDbRating REAL DEFAULT 0,
            imDbRatingCount INTEGER DEFAULT 0
            );''')


def create_popular_movies_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS popular_movies (
            id TEXT PRIMARY KEY,
            rank INTEGER DEFAULT 0,
            rankUpDown INTEGER DEFAULT 0,
            title TEXT NOT NULL,
            fullTitle TEXT NOT NULL,
            year INTEGER DEFAULT 0,
            crew TEXT NOT NULL,
            imDbRating REAL DEFAULT 0,
            imDbRatingCount INTEGER DEFAULT 0
            );''')


def create_movie_ratings_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS movie_ratings (
                imDbID TEXT NOT NULL,
                title TEXT,
                fullTitle TEXT,
                type TEXT,
                year INTEGER DEFAULT 0,
                imDb REAL DEFAULT 0,
                metacritic REAL DEFAULT 0,
                theMovieDb REAL DEFAULT 0,
                rottenTomatoes REAL DEFAULT 0,
                tV_com REAL DEFAULT 0,
                filmAffinity INTEGER DEFAULT 0,
                FOREIGN KEY (imDbId) REFERENCES movies (id)
                ON DELETE CASCADE
                );''')


def fill_pop_tv_table(cursor: sqlite3.Cursor, data):
    for i in range(0, len(data)):
        cursor.execute('''INSERT INTO popular_tv (id, rank, rankUpDown, title,
                       fullTitle, year, crew, imDbRating, imDbRatingCount)
                       VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (data[i]['id'], data[i]['rank'], data[i]['rankUpDown'], data[i]['title'],
                        data[i]['fullTitle'], data[i]['year'], data[i]['crew'], data[i]['imDbRating'],
                        data[i]['imDbRatingCount']))

    cursor.execute('SELECT rowid, * FROM popular_tv')
    cursor.fetchall()


def fill_pop_movies_table(cursor: sqlite3.Cursor, data):
    for i in range(0, len(data)):
        cursor.execute('''INSERT INTO popular_movies (id, rank, rankUpDown, title,
                       fullTitle, year, crew, imDbRating, imDbRatingCount)
                       VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (data[i]['id'], data[i]['rank'], data[i]['rankUpDown'], data[i]['title'],
                        data[i]['fullTitle'], data[i]['year'], data[i]['crew'], data[i]['imDbRating'],
                        data[i]['imDbRatingCount']))

    cursor.execute('SELECT rowid, * FROM popular_movies')
    cursor.fetchall()


def fill_movies_table(cursor: sqlite3.Cursor, data):
    for i in range(0, len(data)):
        cursor.execute('''INSERT INTO movies (id, title,
                       fullTitle, year, crew, imDbRating, imDbRatingCount)
                       VALUES(?, ?, ?, ?, ?, ?, ?)''',
                       (data[i]['id'], data[i]['title'], data[i]['fullTitle'], data[i]['year'],
                        data[i]['crew'], data[i]['imDbRating'], data[i]['imDbRatingCount']))

    cursor.execute('SELECT rowid, * FROM movies')
    cursor.fetchall()


def find_biggest_movers(data):
    rank_changes = []
    for i in range(0, len(data)):
        if data[i]['rankUpDown'].startswith('+'):
            data[i]['rankUpDown'] = data[i]['rankUpDown'][1:]
        if "," in data[i]['rankUpDown'][0:4]:
            data[i]['rankUpDown'] = data[i]['rankUpDown'].replace(",", "")
        float(data[i]['rankUpDown'])
        rank_changes.append(data[i]['rankUpDown'])

    biggest_changes = []
    changes = sorted(rank_changes, key=int)
    biggest_changes.append(changes[len(changes) - 1])
    biggest_changes.append(changes[len(changes) - 2])
    biggest_changes.append(changes[len(changes) - 3])
    biggest_changes.append(changes[0])
    return biggest_changes


def fill_movie_ratings_table(cursor: sqlite3.Cursor, data):
    ratings_url = "https://imdb-api.com/en/API/Ratings/"
    rank_changes = find_biggest_movers(data)
    for i in range(0, len(data)):
        if data[i]['rankUpDown'] == rank_changes[3] or data[i]['rankUpDown'] == rank_changes[2] or \
                data[i]['rankUpDown'] == rank_changes[1] or data[i]['rankUpDown'] == rank_changes[0]:
            r = requests.get(ratings_url + secrets.apiKey + "/" + data[i]['id'])
            info = r.json()
            cursor.execute('''INSERT INTO movie_ratings (imDbId, title, fullTitle, type, year, imDb, metacritic,
                                    theMovieDb, rottenTomatoes, tV_com, filmAffinity)
                                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                           (
                               info['imDbId'], info['title'], info['fullTitle'], info['type'],
                               info['year'], info['imDb'], info['metacritic'], info['theMovieDb'],
                               info['rottenTomatoes'], info['tV_com'], info['filmAffinity']))

        cursor.execute('SELECT * FROM movie_ratings')
        cursor.fetchall()
