import sqlite3
from sqlite3 import IntegrityError

import requests
import secrets
from typing import Tuple

# https://www.youtube.com/watch?v=byHcYRpMgI4
# this whole video helped me a ton with a creating and filling the database
# also helped me with the SELECT and fetchall part


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = connection.cursor()  # get ready to read/write data
    return connection, cursor


def create_shows_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS shows (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        fullTitle TEXT NOT NULL,
        year INTEGER DEFAULT 0,
        crew TEXT NOT NULL,
        imDbRating REAL DEFAULT 0,
        imDbRatingCount INTEGER DEFAULT 0
        );''')


def create_show_ratings_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS show_ratings (
            imDbID TEXT NOT NULL UNIQUE,
            totalRating INTEGER DEFAULT 0,
            totalRatingVotes INTEGER DEFAULT 0,
            ten_rating_percentage REAL DEFAULT 0,
            ten_rating_votes INTEGER DEFAULT 0,
            nine_rating_percentage REAL DEFAULT 0,
            nine_rating_votes INTEGER DEFAULT 0,
            eight_rating_percentage REAL DEFAULT 0,
            eight_rating_votes INTEGER DEFAULT 0,
            seven_rating_percentage REAL DEFAULT 0,
            seven_rating_votes INTEGER DEFAULT 0,
            six_rating_percentage REAL DEFAULT 0,
            six_rating_votes INTEGER DEFAULT 0,
            five_rating_percentage REAL DEFAULT 0,
            five_rating_votes INTEGER DEFAULT 0,
            four_rating_percentage REAL DEFAULT 0,
            four_rating_votes INTEGER DEFAULT 0,
            three_rating_percentage REAL DEFAULT 0,
            three_rating_votes INTEGER DEFAULT 0,
            two_rating_percentage REAL DEFAULT 0,
            two_rating_votes INTEGER DEFAULT 0,
            one_rating_percentage REAL DEFAULT 0,
            one_rating_votes INTEGER DEFAULT 0,
            FOREIGN KEY (imDbId) REFERENCES shows (id)
            ON DELETE CASCADE
            );''')


def fill_shows_table(cursor: sqlite3.Cursor, data):
    for i in range(0, len(data)):
        try:
            cursor.execute('''INSERT INTO shows (id, title,
                           fullTitle, year, crew, imDbRating, imDbRatingCount)
                           VALUES(?, ?, ?, ?, ?, ?, ?)''',
                           (data[i]['id'], data[i]['title'], data[i]['fullTitle'], data[i]['year'],
                            data[i]['crew'], data[i]['imDbRating'], data[i]['imDbRatingCount']))

            cursor.execute('SELECT rowid, * FROM shows')
            cursor.fetchall()
        except IntegrityError:
            cursor.execute('''DROP TABLE shows''')
            create_shows_table(cursor)
            fill_shows_table(cursor, data)


def wheel_of_time_into_shows_table(cursor: sqlite3.Cursor):
    cursor.execute('''INSERT OR IGNORE INTO shows (id, title,
                           fullTitle, year, crew, imDbRating, imDbRatingCount)
                           VALUES(?, ?, ?, ?, ?, ?, ?)''',
                   ('tt0331080', 'Wheel of Time', 'Wheel of Time (2003)', '2003',
                    'The Dalai Lama, Lama Lhundup Woeser, Takna Jigme Sangpo',
                    0, 0))
    cursor.execute('SELECT rowid, * FROM shows')
    cursor.fetchone()


def fill_show_ratings_table(cursor: sqlite3.Cursor, data):
    user_url = "https://imdb-api.com/en/API/UserRatings/"
    for i in range(len(data)):
        try:
            if data[i]['rank'] == '1' or data[i]['rank'] == '50' \
                    or data[i]['rank'] == '100' or data[i]['rank'] == '200':
                r = requests.get(user_url + secrets.apiKey + "/" + data[i]['id'])
                info = r.json()
                if len(info['ratings']) == 0:
                    cursor.execute('''INSERT INTO show_ratings (imDbId, totalRating, totalRatingVotes, 
                    ten_rating_percentage, ten_rating_votes, nine_rating_percentage, nine_rating_votes, 
                    eight_rating_percentage, eight_rating_votes, seven_rating_percentage, seven_rating_votes, 
                    six_rating_percentage, six_rating_votes, five_rating_percentage, five_rating_votes, 
                    four_rating_percentage, four_rating_votes, three_rating_percentage, three_rating_votes, 
                    two_rating_percentage, two_rating_votes, one_rating_percentage, one_rating_votes) VALUES(?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                   (
                                       info['imDbId'], info['totalRating'], info['totalRatingVotes'],
                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
                else:
                    cursor.execute('''INSERT INTO show_ratings (imDbId, totalRating, totalRatingVotes, 
                    ten_rating_percentage, ten_rating_votes, nine_rating_percentage, nine_rating_votes, 
                    eight_rating_percentage, eight_rating_votes, seven_rating_percentage, seven_rating_votes, 
                    six_rating_percentage, six_rating_votes, five_rating_percentage, five_rating_votes, 
                    four_rating_percentage, four_rating_votes, three_rating_percentage, three_rating_votes, 
                    two_rating_percentage, two_rating_votes, one_rating_percentage, one_rating_votes) VALUES(?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                   (
                                       info['imDbId'], info['totalRating'], info['totalRatingVotes'],
                                       info['ratings'][0]['percent'], info['ratings'][0]['votes'],
                                       info['ratings'][1]['percent'], info['ratings'][1]['votes'],
                                       info['ratings'][2]['percent'], info['ratings'][2]['votes'],
                                       info['ratings'][3]['percent'], info['ratings'][3]['votes'],
                                       info['ratings'][4]['percent'], info['ratings'][4]['votes'],
                                       info['ratings'][5]['percent'], info['ratings'][5]['votes'],
                                       info['ratings'][6]['percent'], info['ratings'][6]['votes'],
                                       info['ratings'][7]['percent'], info['ratings'][7]['votes'],
                                       info['ratings'][8]['percent'], info['ratings'][8]['votes'],
                                       info['ratings'][9]['percent'], info['ratings'][9]['votes']))

                cursor.execute('SELECT * FROM shows where title is "Wheel of Time"')
                cursor.fetchone()

                wheel_of_time_id = 'tt0331080'
                w = requests.get(user_url + secrets.apiKey + "/" + wheel_of_time_id)
                wheel_info = w.json()
                cursor.execute('''INSERT OR IGNORE INTO show_ratings (imDbId, totalRating, totalRatingVotes, 
                ten_rating_percentage, ten_rating_votes, nine_rating_percentage, nine_rating_votes, 
                eight_rating_percentage, eight_rating_votes, seven_rating_percentage, seven_rating_votes, 
                six_rating_percentage, six_rating_votes, five_rating_percentage, five_rating_votes, 
                four_rating_percentage, four_rating_votes, three_rating_percentage, three_rating_votes, 
                two_rating_percentage, two_rating_votes, one_rating_percentage, one_rating_votes) VALUES(?, ?, ?, ?, 
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                               (wheel_of_time_id, wheel_info['totalRating'],
                                wheel_info['totalRatingVotes'], wheel_info['ratings'][0]['percent'],
                                wheel_info['ratings'][0]['votes'], wheel_info['ratings'][1]['percent'],
                                wheel_info['ratings'][1]['votes'], wheel_info['ratings'][2]['percent'],
                                wheel_info['ratings'][2]['votes'], wheel_info['ratings'][3]['percent'],
                                wheel_info['ratings'][3]['votes'], wheel_info['ratings'][4]['percent'],
                                wheel_info['ratings'][4]['votes'], wheel_info['ratings'][5]['percent'],
                                wheel_info['ratings'][5]['votes'], wheel_info['ratings'][6]['percent'],
                                wheel_info['ratings'][6]['votes'], wheel_info['ratings'][7]['percent'],
                                wheel_info['ratings'][7]['votes'], wheel_info['ratings'][8]['percent'],
                                wheel_info['ratings'][8]['votes'], wheel_info['ratings'][9]['percent'],
                                wheel_info['ratings'][9]['votes']))

                cursor.execute('SELECT rowid, * FROM show_ratings')
                cursor.fetchall()
        except IntegrityError:
            cursor.execute('''DROP TABLE show_ratings''')
            create_show_ratings_table(cursor)
            fill_show_ratings_table(cursor, data)


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()
