import sqlite3
import requests
import secrets
from typing import Tuple
import sprintTwo
import sprintOne


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


def fill_movie_ratings_table(cursor: sqlite3.Cursor, data):
    ratings_url = "https://imdb-api.com/en/API/Ratings/"
    rank_changes = []
    for i in range(0, len(data)):
        if data[i]['rankUpDown'].startswith('+'):
            data[i]['rankUpDown'] = data[i]['rankUpDown'][1:]
        if "," in data[i]['rankUpDown'][0:4]:
            data[i]['rankUpDown'] = data[i]['rankUpDown'].replace(",", "")
        float(data[i]['rankUpDown'])
        rank_changes.append(data[i]['rankUpDown'])

    changes = sorted(rank_changes, key=int)
    for i in range(0, len(data)):
        if data[i]['rankUpDown'] == changes[0] or data[i]['rankUpDown'] == changes[99] or \
                data[i]['rankUpDown'] == changes[96] or data[i]['rankUpDown'] == changes[97]:
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

