import sprintTwo


def test_get_shows():
    shows = sprintTwo.get_data()
    num_shows = len(shows['items'])
    assert num_shows == 250


# def test_show_db():
#     show = {"items": [{"id": "tt5491994", "rank": "1", "title": "Planet Earth II",
#                        "fullTitle": "Planet Earth II (2016)",
#                      "year": "2016", "image": "https://m.media-amazon.com/images/M/MV5BZWYxODViMGYtMGE2ZC00ZGQ3LThhM \
#                        WUtYTVkNGE3OWU4NWRkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjYwNDA2MDE@._V1_UX128_CR0,3,128,176_AL_.jpg",
#                        "crew": "David Attenborough, Gordon Buchanan", "imDbRating": "9.5",
#                        "imDbRatingCount": "110148"}]}
#     conn, cursor = sprintTwo.open_db('test.db')
#     print(type(conn))
#     sprintTwo.setup_db(cursor)
#     sprintTwo.fill_shows_table(cursor, show)
#     cursor.execute("""SELECT * FROM show""")
#     data = cursor.fetchone()
#     sprintTwo.close_db(conn)
#     assert data[2] == 'Planet Earth II'


if __name__ == '__main__':
    test_get_shows()
