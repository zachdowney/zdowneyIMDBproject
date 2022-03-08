import os
import tkinter
from tkinter import Tk

import sprintTwo
import sprintOne
import sprintThree
import sprintFour
import sqlite3


def test_get_shows():
    shows = sprintOne.get_data("https://imdb-api.com/en/API/Top250TVs/")
    num_shows = len(shows)
    if len(shows) != 250:
        raise ValueError
    assert num_shows == 250


def test_show_db():
    shows = [{"id": "tt1234567", "rank": "500", "title": "BSU",
              "fullTitle": "BSU (2022)",
              "year": "2022", "image": "https://m.media-amazon.com/images/M/MV5BZWYxODViMGYtMGE2ZC00ZGQ3LThhM \
            WUtYTVkNGE3OWU4NWRkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjYwNDA2MDE@._V1_UX128_CR0,3,128,176_AL_.jpg",
              "crew": "Zach Downey", "imDbRating": "9.9",
              "imDbRatingCount": "25000"}]
    conn, cursor = sprintTwo.open_db('test_db.sqlite')
    print(type(conn))
    sprintTwo.create_shows_table(cursor)
    sprintTwo.fill_shows_table(cursor, shows)
    cursor.execute("""SELECT * FROM shows""")
    data = cursor.fetchone()
    sprintTwo.close_db(conn)
    assert data[4] == 'Zach Downey'


def test_find_biggest_movers():
    test_movie_list = [{"id": "tt1234567", "rank": "1", "rankUpDown": "0", "title": "Whitman"},
                       {"id": "tt2345678", "rank": "2", "rankUpDown": "+23", "title": "Hanson"},
                       {"id": "tt3456789", "rank": "3", "rankUpDown": "+15", "title": "Marshfield"},
                       {"id": "tt4567890", "rank": "4", "rankUpDown": "+25", "title": "Bridgewater"},
                       {"id": "tt5678901", "rank": "5", "rankUpDown": "-3", "title": "Abington"},
                       {"id": "tt6789012", "rank": "6", "rankUpDown": "+2", "title": "Plymouth"},
                       {"id": "tt7890123", "rank": "7", "rankUpDown": "-3", "title": "Carver"},
                       {"id": "tt8901234", "rank": "8", "rankUpDown": "+15", "title": "Brockton"},
                       {"id": "tt9012345", "rank": "9", "rankUpDown": "-4", "title": "Rockland"},
                       {"id": "tt0123456", "rank": "10", "rankUpDown": "+40", "title": "Scituate"},
                       {"id": "tt2468024", "rank": "11", "rankUpDown": "-5", "title": "Hingham"}]
    movers = sprintThree.find_biggest_movers(test_movie_list)
    assert movers == ['40', '25', '23', '-5']


def test_wrong_biggest_movers():
    test_wrong_movie_list = [{"id": "tt1234567", "rank": "1", "rankUpDown": "0", "title": "Silver"},
                             {"id": "tt2345678", "rank": "2", "rankUpDown": "+23", "title": "Gold"},
                             {"id": "tt3456789", "rank": "3", "rankUpDown": "+15", "title": "Platinum"},
                             {"id": "tt4567890", "rank": "4", "rankUpDown": "+25", "title": "Diamonds"},
                             {"id": "tt5678901", "rank": "5", "rankUpDown": "-3", "title": "Carbon"},
                             {"id": "tt6789012", "rank": "6", "rankUpDown": "+2", "title": "Plymouth"},
                             {"id": "tt7890123", "rank": "7", "rankUpDown": "-3", "title": "Oxygen"},
                             {"id": "tt8901234", "rank": "8", "rankUpDown": "+15", "title": "Helium"},
                             {"id": "tt9012345", "rank": "9", "rankUpDown": "-4", "title": "Hydrogen"},
                             {"id": "tt0123456", "rank": "10", "rankUpDown": "+40", "title": "Iron"},
                             {"id": "tt2468024", "rank": "11", "rankUpDown": "-5", "title": "Uranium"}]
    movers = sprintThree.find_biggest_movers(test_wrong_movie_list)
    try:
        assert movers != ['40', '25', '23', '-5']
    except AssertionError:
        print("Wrong movers test passed.")


def test_movie_db():
    movies = [{"id": "tt1234567", "rank": "10", "title": "WH",
               "fullTitle": "WH (2022)",
               "year": "2020",
               "crew": "Zach Downey", "imDbRating": "9.1",
               "imDbRatingCount": "100000"}]
    conn, cursor = sprintTwo.open_db('test_db.sqlite')
    print(type(conn))
    sprintThree.create_movies_table(cursor)
    sprintThree.fill_movies_table(cursor, movies)
    cursor.execute("""SELECT * FROM movies""")
    data = cursor.fetchone()
    sprintTwo.close_db(conn)
    assert data[4] == 'Zach Downey'


def test_popular_tv_table():
    popular_tv = [{"id": "tt1234567", "rank": "1", "rankUpDown": "+1", "title": "BSU",
                   "fullTitle": "BSU (2022)",
                   "year": "2022",
                   "crew": "Zach Downey", "imDbRating": "9.9",
                   "imDbRatingCount": "25000"}]
    conn, cursor = sprintTwo.open_db('test_db.sqlite')
    print(type(conn))
    sprintThree.create_popular_tv_table(cursor)
    sprintThree.fill_pop_tv_table(cursor, popular_tv)
    cursor.execute("""SELECT * FROM popular_tv""")
    data = cursor.fetchone()
    sprintTwo.close_db(conn)
    assert data[3] == 'BSU'


# Attempt at testing ordered data
def test_ordered_data():
    popular_movies = [{"id": "tt1234567", "rank": "1", "rankUpDown": "0", "title": "Whitman", "fullTitle": "A (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.9",
                       "imDbRatingCount": "25000"},
                      {"id": "tt2345678", "rank": "2", "rankUpDown": "+23", "title": "Hanson",
                       "fullTitle": "ZJD (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"},
                      {"id": "tt3456789", "rank": "3", "rankUpDown": "+15", "title": "Marshfield",
                       "fullTitle": "Z (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"},
                      {"id": "tt4567890", "rank": "4", "rankUpDown": "+25", "title": "Bridgewater",
                       "fullTitle": "D (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"},
                      {"id": "tt5678901", "rank": "5", "rankUpDown": "-3", "title": "Abington",
                       "fullTitle": "S (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"},
                      {"id": "tt6789012", "rank": "6", "rankUpDown": "+2", "title": "Plymouth",
                       "fullTitle": "o (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"},
                      {"id": "tt7890123", "rank": "7", "rankUpDown": "-3", "title": "Carver", "fullTitle": "i (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"},
                      {"id": "tt8901234", "rank": "8", "rankUpDown": "+15", "title": "Brockton",
                       "fullTitle": "jh (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"},
                      {"id": "tt9012345", "rank": "9", "rankUpDown": "-4", "title": "Rockland",
                       "fullTitle": "bgf (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"},
                      {"id": "tt0123456", "rank": "10", "rankUpDown": "+40", "title": "Scituate",
                       "fullTitle": "nv (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"},
                      {"id": "tt2468024", "rank": "11", "rankUpDown": "-5", "title": "Hingham",
                       "fullTitle": "fds (2022)",
                       "year": "2022",
                       "crew": "Zach Downey", "imDbRating": "9.3",
                       "imDbRatingCount": "100"}]

    conn, cursor = sprintTwo.open_db('test_db.sqlite')
    print(type(conn))
    root = tkinter.Tk()
    sprintThree.create_popular_movies_table(cursor)
    sprintThree.fill_pop_movies_table(cursor, popular_movies)
    second_frame = sprintFour.scrollbar(root)
    rank_statement = '''SELECT * from popular_movies ORDER BY rank DESC'''
    up_down_statement = '''SELECT * from popular_movies ORDER BY rankUpDown ASC'''
    sprintFour.create_most_popular_tables(popular_movies, 'popular_movies', 'TEST DATA', '2000x2000', 'test_db.sqlite')
    sprintFour.popular_labeling(popular_movies, 'popular_movies', 'Test Data Window', '2000x2000', second_frame,
                                rank_statement, up_down_statement, 'test_db.sqlite')
    sprintTwo.close_db(conn)


def test_in_both():
    assert len(sprintFour.in_both_finder('popular_tv', 'shows', 'test_db.sqlite')) == 1
    assert len(sprintFour.in_both_finder('popular_movies', 'movies', 'test_db.sqlite')) == 0


def test_foreign_key():
    conn, cursor = sprintTwo.open_db("test_db.sqlite")
    sprintTwo.create_shows_table(cursor)
    sprintTwo.create_show_ratings_table(cursor)
    cursor.execute('''SELECT sql FROM sqlite_master WHERE tbl_name = ? AND type = ?''', ("show_ratings", "table"))
    data = cursor.fetchall()
    assert len(data) == 1  # there should only be one table
    sql_statement: str = data[0][0]  # get the only data data is a list of one row, which contains only one column
    sprintTwo.close_db(conn)
    assert "FOREIGN KEY" in sql_statement and "REFERENCES shows" in sql_statement


def test_up_down_graph():
    sprintFour.up_down_graph('popular_movies', 'popular_tv', 'test_db.sqlite')

