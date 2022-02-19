import sqlite3
import requests
import secrets
from typing import Tuple
import sprintTwo
import sprintOne


def fill_pop_tv_table(cursor: sqlite3.Cursor, pop_tv):
    for i in range(0, len(pop_tv)):
        cursor.execute('''INSERT INTO popular_tv (id, rank, rankUpDown, title,
                       fullTitle, year, crew, imDbRating, imDbRatingCount)
                       VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (pop_tv[i]['id'], pop_tv[i]['rank'], pop_tv[i]['rankUpDown'], pop_tv[i]['title'],
                        pop_tv[i]['fullTitle'], pop_tv[i]['year'], pop_tv[i]['crew'], pop_tv[i]['imDbRating'],
                        pop_tv[i]['imDbRatingCount']))

    cursor.execute('SELECT rowid, * FROM popular_tv')
    cursor.fetchall()


def main():
    pop_tv = sprintOne.get_data("https://imdb-api.com/en/API/MostPopularTVs/k_fycin0jm")
    shows = sprintOne.get_data("https://imdb-api.com/en/API/Top250TVs/")
    conn, cursor = sprintTwo.open_db('shows.db')
    print(type(conn))
    sprintTwo.setup_shows_db(cursor)
    sprintTwo.fill_shows_table(cursor, shows)
    sprintTwo.wheel_of_time_into_shows_table(cursor)
    fill_ratings_table(cursor)
    close_db(conn)


if __name__ == '__main__':
    main()
