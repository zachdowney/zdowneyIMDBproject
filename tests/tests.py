import sprintTwo


def test_get_shows():
    shows = sprintTwo.get_data()
    num_shows = len(shows)
    assert num_shows == 250


def test_show_db():
    shows = [{"id": "tt1234567", "rank": "500", "title": "BSU",
             "fullTitle": "BSU (2022)",
             "year": "2022", "image": "https://m.media-amazon.com/images/M/MV5BZWYxODViMGYtMGE2ZC00ZGQ3LThhM \
            WUtYTVkNGE3OWU4NWRkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjYwNDA2MDE@._V1_UX128_CR0,3,128,176_AL_.jpg",
             "crew": "Zach Downey", "imDbRating": "9.9",
             "imDbRatingCount": "25000"}]
    conn, cursor = sprintTwo.open_db('test.db')
    print(type(conn))
    sprintTwo.setup_db(cursor)
    sprintTwo.fill_shows_table(cursor, shows)
    cursor.execute("""SELECT * FROM shows""")
    data = cursor.fetchone()
    sprintTwo.close_db(conn)
    assert data[1] == 'BSU'


if __name__ == '__main__':
    test_get_shows()
