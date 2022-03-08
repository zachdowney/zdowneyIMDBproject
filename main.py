import sprintOne
import sprintThree
import sprintTwo
import sprintFour


def previous_sprints():
    pop_movies = sprintOne.get_data("https://imdb-api.com/en/API/MostPopularMovies/")
    movies = sprintOne.get_data("https://imdb-api.com/en/API/Top250Movies/")
    pop_tv = sprintOne.get_data("https://imdb-api.com/en/API/MostPopularTVs/")
    shows = sprintOne.get_data("https://imdb-api.com/en/API/Top250TVs/")
    sprintOne.save_data(shows)
    conn, cursor = sprintTwo.open_db('shows_db.sqlite')
    sprintTwo.create_top250_tables(cursor, 'shows')
    sprintTwo.fill_top250_table(cursor, shows, 'shows')
    sprintTwo.wheel_of_time_into_shows_table(cursor)
    sprintTwo.create_show_ratings_table(cursor)
    sprintTwo.fill_show_ratings_table(cursor, shows)
    sprintThree.create_popular_tables(cursor, 'popular_tv')
    sprintThree.fill_pop_tables(cursor, pop_tv, 'popular_tv')
    sprintTwo.create_top250_tables(cursor, 'movies')
    sprintTwo.fill_top250_table(cursor, movies, 'movies')
    sprintThree.create_popular_tables(cursor, 'popular_movies')
    sprintThree.fill_pop_tables(cursor, pop_movies, 'popular_movies')
    sprintThree.create_movie_ratings_table(cursor)
    sprintThree.fill_movie_ratings_table(cursor, pop_movies)
    sprintTwo.close_db(conn)


def main():
    sprintFour.gui_home_page()


if __name__ == '__main__':
    main()
