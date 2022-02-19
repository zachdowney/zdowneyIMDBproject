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
    user_url = "https://imdb-api.com/en/API/UserRatings/"
    rank_change_list = []
    for i in range(len(data)):
        rank_change_list += data[i]['rankUpDown']
        sorted(rank_change_list)


    #         r = requests.get(user_url + secrets.apiKey + "/" + data[i]['id'])
    #         info = r.json()
    #         cursor.execute('''INSERT INTO movie_ratings (imDbId, totalRating, totalRatingVotes,
    #         ten_rating_percentage, ten_rating_votes, nine_rating_percentage, nine_rating_votes,
    #         eight_rating_percentage, eight_rating_votes, seven_rating_percentage, seven_rating_votes,
    #         six_rating_percentage, six_rating_votes, five_rating_percentage, five_rating_votes, four_rating_percentage,
    #         four_rating_votes, three_rating_percentage, three_rating_votes, two_rating_percentage, two_rating_votes,
    #         one_rating_percentage, one_rating_votes)
    #         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    #                        (
    #                            info['imDbId'], info['totalRating'], info['totalRatingVotes'],
    #                            info['ratings'][0]['percent'], info['ratings'][0]['votes'],
    #                            info['ratings'][1]['percent'], info['ratings'][1]['votes'],
    #                            info['ratings'][2]['percent'], info['ratings'][2]['votes'],
    #                            info['ratings'][3]['percent'], info['ratings'][3]['votes'],
    #                            info['ratings'][4]['percent'], info['ratings'][4]['votes'],
    #                            info['ratings'][5]['percent'], info['ratings'][5]['votes'],
    #                            info['ratings'][6]['percent'], info['ratings'][6]['votes'],
    #                            info['ratings'][7]['percent'], info['ratings'][7]['votes'],
    #                            info['ratings'][8]['percent'], info['ratings'][8]['votes'],
    #                            info['ratings'][9]['percent'], info['ratings'][9]['votes']))
    #
    # cursor.execute('SELECT rowid, * FROM movie_ratings')
    # cursor.fetchall()


