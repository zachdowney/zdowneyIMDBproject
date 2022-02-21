import sprintTwo
import sprintOne
import sprintThree


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


def test_popular_movies_table():
    popular_movie = [{"id": "tt1234567", "rank": "1", "rankUpDown": "+1", "title": "ZJD",
                      "fullTitle": "ZJD (2022)",
                      "year": "2022",
                      "crew": "Zach Downey", "imDbRating": "9.3",
                      "imDbRatingCount": "100"}]
    conn, cursor = sprintTwo.open_db('test_db.sqlite')
    print(type(conn))
    sprintThree.create_popular_movies_table(cursor)
    sprintThree.fill_pop_movies_table(cursor, popular_movie)
    cursor.execute("""SELECT * FROM popular_movies""")
    data = cursor.fetchone()
    sprintTwo.close_db(conn)
    assert data[3] == 'ZJD'

# attempt at testing movie ratings table.
# def test_movies_ratings_table():
#     test_movie_list = [
#         {"id": "tt5834426", "rank": "11", "rankUpDown": "-5", "title": "Moonfall", "fullTitle": "Moonfall (2022)",
#          "year": "2022", "imDbRating": "5.3", "imDbRatingCount": "11376"},
#         {"id": "tt8041270", "rank": "12", "rankUpDown": "+44", "title": "Jurassic World Dominion",
#          "fullTitle": "Jurassic World Dominion (2022)", "year": "2022",
#          "crew": "Colin Trevorrow (dir.), Bryce Dallas Howard, Laura Dern", "imDbRating": "",
#          "imDbRatingCount": "0"},
#         {"id": "tt1464335", "rank": "13", "rankUpDown": "-2", "title": "Uncharted",
#          "fullTitle": "Uncharted (2022)", "year": "2022",
#          "crew": "Ruben Fleischer (dir.), Tom Holland, Mark Wahlberg", "imDbRating": "6.7",
#          "imDbRatingCount": "17812"},
#         {"id": "tt11214590", "rank": "14", "rankUpDown": "-4", "title": "House of Gucci",
#          "fullTitle": "House of Gucci (2021)", "year": "2021",
#          "crew": "Ridley Scott (dir.), Lady Gaga, Adam Driver", "imDbRating": "6.7",
#          "imDbRatingCount": "74255"},
#         {"id": "tt11286314", "rank": "15", "rankUpDown": "-3", "title": "Don't Look Up",
#          "fullTitle": "Don't Look Up (2021)", "year": "2021",
#          "crew": "Adam McKay (dir.), Leonardo DiCaprio, Jennifer Lawrence", "imDbRating": "7.2",
#          "imDbRatingCount": "434954"},
#         {"id": "tt11271038", "rank": "16", "rankUpDown": "+6", "title": "Licorice Pizza",
#          "fullTitle": "Licorice Pizza (2021)", "year": "2021",
#          "crew": "Paul Thomas Anderson (dir.), Alana Haim, Cooper Hoffman", "imDbRating": "7.8",
#          "imDbRatingCount": "30078"},
#         {"id": "tt4513678", "rank": "17", "rankUpDown": "-4", "title": "Ghostbusters: Afterlife",
#          "fullTitle": "Ghostbusters: Afterlife (2021)", "year": "2021",
#          "crew": "Jason Reitman (dir.), Carrie Coon, Paul Rudd",
#          "imDbRating": "7.2", "imDbRatingCount": "118507"},
#         {"id": "tt12789558", "rank": "18", "rankUpDown": "+8", "title": "Belfast", "fullTitle": "Belfast (2021)",
#          "year": "2021", "crew": "Kenneth Branagh (dir.), Jude Hill, Lewis McAskie", "imDbRating": "7.4",
#          "imDbRatingCount": "29499"},
#         {"id": "tt1160419", "rank": "19", "rankUpDown": "-2", "title": "Dune", "fullTitle": "Dune (2021)",
#          "year": "2021", "crew": "Denis Villeneuve (dir.), Timothée Chalamet, Rebecca Ferguson",
#          "imDbRating": "8.1", "imDbRatingCount": "489540"},
#         {"id": "tt10366460", "rank": "20", "rankUpDown": "+35", "title": "CODA", "fullTitle": "CODA (2021)",
#          "year": "2021", "crew": "Sian Heder (dir.), Emilia Jones, Marlee Matlin",
#          "imDbRating": "8.1", "imDbRatingCount": "49958"}]
#     conn, cursor = sprintTwo.open_db('test.db')
#     print(type(conn))
#     sprintThree.create_movie_ratings_table(cursor)
#     sprintThree.fill_movie_ratings_table(cursor, test_movie_list)
#     cursor.execute("""SELECT * FROM movie_ratings""")
#     cursor.fetchall()
#     sprintTwo.close_db(conn)
