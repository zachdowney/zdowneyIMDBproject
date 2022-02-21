import sprintThree
import sprintTwo
import sprintOne


def main():
    pop_movies = sprintOne.get_data("https://imdb-api.com/en/API/MostPopularMovies/")
    movies = sprintOne.get_data("https://imdb-api.com/en/API/Top250Movies/")
    pop_tv = sprintOne.get_data("https://imdb-api.com/en/API/MostPopularTVs/")
    shows = sprintOne.get_data("https://imdb-api.com/en/API/Top250TVs/")
    sprintOne.save_data(shows)

    conn, cursor = sprintTwo.open_db('shows_db.sqlite')
    sprintTwo.create_shows_table(cursor)
    sprintTwo.fill_shows_table(cursor, shows)
    sprintTwo.wheel_of_time_into_shows_table(cursor)
    sprintTwo.create_show_ratings_table(cursor)
    sprintTwo.fill_show_ratings_table(cursor, shows)
    sprintThree.create_popular_tv_table(cursor)
    sprintThree.fill_pop_tv_table(cursor, pop_tv)
    sprintThree.create_movies_table(cursor)
    sprintThree.fill_movies_table(cursor, movies)
    sprintThree.create_popular_movies_table(cursor)
    sprintThree.fill_pop_movies_table(cursor, pop_movies)
    sprintThree.create_movie_ratings_table(cursor)
    sprintThree.fill_movie_ratings_table(cursor, pop_movies)
    sprintTwo.close_db(conn)


if __name__ == '__main__':
    main()
