import tkinter
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plot

# https://www.youtube.com/watch?v=AK1J8xF4fuk&t=1360s video helped with everything


import sprintOne
import main
import sqlite3


def gui_home_page():
    root = tkinter.Tk()
    root.title("Update Data or Visualization")
    root.geometry('150x150')

    # Button
    update_button = tkinter.Button(root, text='Update Data', command=lambda: main.previous_sprints())
    update_button.grid(row=1, column=1, padx=10, pady=20)
    visual_button = tkinter.Button(root, text='Run Data Visualization', command=lambda: data_visualization())
    visual_button.grid(row=2, column=1, padx=10, pady=10)
    root.mainloop()


def data_visualization():
    root = tkinter.Tk()
    root.title("Show or Movie Info")
    root.geometry('200x400')

    # Button
    show_button = tkinter.Button(root, text='Most Popular Shows', command=lambda: pop_shows_gui())
    show_button.grid(row=1, column=1, padx=10, pady=20, )
    movie_button = tkinter.Button(root, text='Most Popular Movies', command=lambda: pop_movies_gui())
    movie_button.grid(row=2, column=1, padx=10, pady=10)
    movie_button = tkinter.Button(root, text='Top 250 Shows', command=lambda: top250_shows_gui())
    movie_button.grid(row=3, column=1, padx=10, pady=10)
    movie_button = tkinter.Button(root, text='Top 250 Movies', command=lambda: top250_movies_gui())
    movie_button.grid(row=4, column=1, padx=10, pady=10)
    up_down_button = tkinter.Button(root, text='Up/Down Graph', command=lambda: up_down_graph('popular_movies',
                                                                                              'popular_tv',
                                                                                              'shows_db.sqlite'))
    up_down_button.grid(row=5, column=1, padx=10, pady=10)
    up_down_button = tkinter.Button(root, text='Movies appearing \n in most popular movies\n and top 250 movies',
                                    command=lambda: in_both_tables('popular_movies', 'movies', 'shows_db.sqlite'))
    up_down_button.grid(row=6, column=1, padx=10, pady=10)
    up_down_button = tkinter.Button(root, text='Shows appearing \n in most popular shows\n and top 250 shows',
                                    command=lambda: in_both_tables('popular_tv', 'shows', 'shows_db.sqlite'))
    up_down_button.grid(row=7, column=1, padx=10, pady=10)
    root.mainloop()


def pop_shows_gui():
    pop_tv = sprintOne.get_data("https://imdb-api.com/en/API/MostPopularTVs/")
    create_most_popular_tables(pop_tv, 'popular_tv', "Most Popular Tv Shows", '2000x600', 'shows_db.sqlite')


def pop_movies_gui():
    pop_movies = sprintOne.get_data("https://imdb-api.com/en/API/MostPopularMovies/")
    create_most_popular_tables(pop_movies, 'popular_movies', "Most Popular Movies", '2000x600', 'shows_db.sqlite')


def top250_shows_gui():
    shows = sprintOne.get_data("https://imdb-api.com/en/API/Top250TVs/")
    create_top250_tables(shows, 'shows', "Top 250 Shows", '2000x600')


def top250_movies_gui():
    movies = sprintOne.get_data("https://imdb-api.com/en/API/Top250Movies/")
    create_top250_tables(movies, 'movies', "Top 250 Movies", '2000x600')


def create_most_popular_tables(data, table_name, title, geometry, db_name):
    root = tkinter.Tk()
    root.title(title)
    root.geometry(geometry)

    second_frame = scrollbar(root)
    rank_statement = '''SELECT * from ''' + table_name + ''' ORDER BY rank DESC'''
    up_down_statement = '''SELECT * from ''' + table_name + ''' ORDER BY rankUpDown ASC'''

    popular_labeling(data, table_name, title, geometry, second_frame, rank_statement, up_down_statement,
                     db_name)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''SELECT * from ''' + table_name)
    fill_window(data, cursor, second_frame)


def create_top250_tables(data, table_name, title, geometry):
    root = tkinter.Tk()
    root.title(title)
    root.geometry(geometry)

    second_frame = scrollbar(root)

    id_label = tkinter.Label(second_frame, text='id')
    id_label.grid(row=0, column=0)
    title_label = tkinter.Label(second_frame, text='title')
    title_label.grid(row=0, column=1)
    year_label = tkinter.Label(second_frame, text='year')
    year_label.grid(row=0, column=2)
    crew_label = tkinter.Label(second_frame, text='crew')
    crew_label.grid(row=0, column=3)
    imdb_rating_label = tkinter.Label(second_frame, text='imDbRating')
    imdb_rating_label.grid(row=0, column=4)
    imdb_count_label = tkinter.Label(second_frame, text='imDbRatingCount')
    imdb_count_label.grid(row=0, column=5)
    ratings_label = tkinter.Label(second_frame, text='Ratings (if available)')
    ratings_label.grid(row=0, column=6)

    conn = sqlite3.connect('shows_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('''SELECT * from ''' + table_name)

    for i in range(len(data)):
        record = cursor.fetchone()
        id_input = Label(second_frame, text=str(record[0]))
        id_input.grid(row=i + 1, column=0)
        full_title_input = Label(second_frame, text=str(record[2]))
        full_title_input.grid(row=i + 1, column=1)
        year_input = Label(second_frame, text=str(record[3]))
        year_input.grid(row=i + 1, column=2)
        crew_input = Label(second_frame, text=str(record[4]))
        crew_input.grid(row=i + 1, column=3)
        imdb_rating_input = Label(second_frame, text=str(record[5]))
        imdb_rating_input.grid(row=i + 1, column=4)
        imdb_count_input = Label(second_frame, text=str(record[6]))
        imdb_count_input.grid(row=i + 1, column=5)
        ratings_input = tkinter.Button(second_frame, text='Ratings')
        ratings_input.grid(row=i + 1, column=6)


def rank_up_down_sorting(data, table_name, title, geometry, select_statement, db_name):
    root = tkinter.Tk()
    root.title(title)
    root.geometry(geometry)

    second_frame = scrollbar(root)
    rank_statement = '''SELECT * from ''' + table_name + ''' ORDER BY rank ASC'''
    up_down_statement = '''SELECT * from ''' + table_name + ''' ORDER BY rankUpDown DESC'''

    # Button
    popular_labeling(data, table_name, title, geometry, second_frame, rank_statement, up_down_statement,
                     'shows_db.sqlite')

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    statement = select_statement
    cursor.execute(statement)
    fill_window(data, cursor, second_frame)


def fill_window(data, cursor, second_frame):
    for i in range(len(data)):
        record = cursor.fetchone()
        id_input = Label(second_frame, text=str(record[0]))
        id_input.grid(row=i + 1, column=0)
        rank_input = Label(second_frame, text=str(record[1]))
        rank_input.grid(row=i + 1, column=1)
        up_down_input = Label(second_frame, text=str(record[2]))
        up_down_input.grid(row=i + 1, column=2)
        full_title_input = Label(second_frame, text=str(record[4]))
        full_title_input.grid(row=i + 1, column=3)
        year_input = Label(second_frame, text=str(record[5]))
        year_input.grid(row=i + 1, column=4)
        crew_input = Label(second_frame, text=str(record[6]))
        crew_input.grid(row=i + 1, column=5)
        imdb_rating_input = Label(second_frame, text=str(record[7]))
        imdb_rating_input.grid(row=i + 1, column=6)
        imdb_count_input = Label(second_frame, text=str(record[8]))
        imdb_count_input.grid(row=i + 1, column=7)
        ratings_input = tkinter.Button(second_frame, text='Ratings', command=lambda: ratings_check(cursor, record))
        ratings_input.grid(row=i + 1, column=8)


def ratings_check(cursor, record):
    root = Tk()
    root.title = 'Ratings'
    root.geometry = '1000x1000'
    if cursor.execute('''SELECT * from movie_ratings WHERE movie_ratings.fullTitle = ''' + str(record[4])):
        ratings = cursor.fetchone()
        ratings_input = Label(root, text=str(ratings))
        ratings_input.grid(row=1, column=1, rowspan=10, columnspan=10)
    else:
        ratings_input = Label(root, text='No Ratings for this movie')
        ratings_input.grid(row=1, column=1)


# https://www.youtube.com/watch?v=0WafQCaok6g&t=613s
# showed me how to add a scroll bar
def scrollbar(root):
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    return second_frame


def popular_labeling(data, table_name, title, geometry, second_frame, rank_statement, up_down_statement, db_name):
    id_label = tkinter.Label(second_frame, text='id')
    id_label.grid(row=0, column=0)
    rankings_button = tkinter.Button(second_frame, text='rank',
                                     command=lambda: rank_up_down_sorting(data, table_name, title, geometry,
                                                                          rank_statement, db_name))
    rankings_button.grid(row=0, column=1)
    up_down_button = tkinter.Button(second_frame, text='rankUpDown',
                                    command=lambda: rank_up_down_sorting(data, table_name, title, geometry,
                                                                         up_down_statement, db_name))
    up_down_button.grid(row=0, column=2)
    title_label = tkinter.Label(second_frame, text='title')
    title_label.grid(row=0, column=3)
    year_label = tkinter.Label(second_frame, text='year')
    year_label.grid(row=0, column=4)
    crew_label = tkinter.Label(second_frame, text='crew')
    crew_label.grid(row=0, column=5)
    imdb_rating_label = tkinter.Label(second_frame, text='imDbRating')
    imdb_rating_label.grid(row=0, column=6)
    imdb_count_label = tkinter.Label(second_frame, text='imDbRatingCount')
    imdb_count_label.grid(row=0, column=7)
    ratings_label = tkinter.Label(second_frame, text='Ratings (if available)')
    ratings_label.grid(row=0, column=8)


def up_down_graph(first_table, second_table, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''SELECT * from ''' + first_table + ''' WHERE rankUpDown > 0''')
    movies_up = cursor.fetchall()
    cursor.execute('''SELECT * from ''' + first_table + ''' WHERE rankUpDown < 0''')
    movies_down = cursor.fetchall()
    cursor.execute('''SELECT * from ''' + second_table + ''' WHERE rankUpDown > 0''')
    shows_up = cursor.fetchall()
    cursor.execute('''SELECT * from ''' + second_table + ''' WHERE rankUpDown < 0''')
    shows_down = cursor.fetchall()

    # https://www.geeksforgeeks.org/bar-plot-in-matplotlib/?ref=lbp
    # helped make graph
    data = {'Movies moving up': len(movies_up), 'Movies moving down': len(movies_down),
            'Shows moving up': len(shows_up), 'Shows moving down': len(shows_down)}
    up_down = list(data.keys())
    values = list(data.values())
    fig = plot.figure(figsize=(10, 5))
    # creating the bar plot
    plot.bar(up_down, values, color='maroon', width=0.4)
    plot.ylabel("No. of shows/movies")
    plot.title("Shows/Movies Movement")
    plot.show()


def in_both_tables(first_table_name, second_table_name, db_name):
    root = tkinter.Tk()
    root.title("Existing In Both")
    root.geometry('1000x1000')
    second_frame = scrollbar(root)

    in_both = in_both_finder(first_table_name, second_table_name, db_name)

    id_label = tkinter.Label(second_frame, text='id')
    id_label.grid(row=0, column=0)
    rankings_button = tkinter.Label(second_frame, text='rank')
    rankings_button.grid(row=0, column=1)
    up_down_button = tkinter.Label(second_frame, text='rankUpDown')
    up_down_button.grid(row=0, column=2)
    title_label = tkinter.Label(second_frame, text='title')
    title_label.grid(row=0, column=3)
    year_label = tkinter.Label(second_frame, text='year')
    year_label.grid(row=0, column=4)

    for i in range(len(in_both)):
        record = in_both[i]
        id_input = Label(second_frame, text=str(record[0]))
        id_input.grid(row=i + 1, column=0)
        rank_input = Label(second_frame, text=str(record[1]))
        rank_input.grid(row=i + 1, column=1)
        up_down_input = Label(second_frame, text=str(record[2]))
        up_down_input.grid(row=i + 1, column=2)
        full_title_input = Label(second_frame, text=str(record[4]))
        full_title_input.grid(row=i + 1, column=3)
        year_input = Label(second_frame, text=str(record[5]))
        year_input.grid(row=i + 1, column=4)


def in_both_finder(first_table_name, second_table_name, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''SELECT * from ''' + first_table_name +
                   ''' INNER JOIN ''' + second_table_name +
                   ''' on ''' + first_table_name + '''.fullTitle = ''' + second_table_name + '''.fullTitle''')
    in_both = cursor.fetchall()
    return in_both


# Attempt at ratings
# def ratings_check(cursor, record, second_frame):
#     root = tkinter.Tk()
#     root.title('User Ratings')
#     root.geometry('2000x2000')
#     cursor.execute('''SELECT * from show_ratings''')
#     data = cursor.fetchall()
#     for i in range(len(data)):
#         print("in for")
#         if data[i]['imDbId'] == record[0]:
#             print("in if")
#             ratings = cursor.fetchone()
#             id_label = Label(second_frame, text='imDbId')
#             id_label.grid(row=0, column=0)
#             id_input = Label(second_frame, text=str(ratings[0]))
#             id_input.grid(row=1, column=0)
#             total_rating_label = Label(second_frame, text='totalRating')
#             total_rating_label.grid(row=0, column=1)
#             total_rating_input = Label(second_frame, text=str(ratings[1]))
#             total_rating_input.grid(row=1, column=1)
#             total_rating_votes_label = Label(second_frame, text='totalRatingVotes')
#             total_rating_votes_label.grid(row=0, column=2)
#             total_rating_votes_input = Label(second_frame, text=str(ratings[2]))
#             total_rating_votes_input.grid(row=1, column=2)
#             ten_rating_percentage_label = Label(second_frame, text='10Rating%')
#             ten_rating_percentage_label.grid(row=0, column=3)
#             ten_rating_percentage_input = Label(second_frame, text=str(ratings[3]))
#             ten_rating_percentage_input.grid(row=1, column=3)
#             ten_rating_votes_label = Label(second_frame, text='10RatingVotes')
#             ten_rating_votes_label.grid(row=0, column=4)
#             ten_rating_votes_input = Label(second_frame, text=str(ratings[4]))
#             ten_rating_votes_input.grid(row=1, column=4)
#             nine_rating_percentage_label = Label(second_frame, text='9Rating%')
#             nine_rating_percentage_label.grid(row=0, column=5)
#             nine_rating_percentage_input = Label(second_frame, text=str(ratings[5]))
#             nine_rating_percentage_input.grid(row=1, column=5)
#             nine_rating_votes_label = Label(second_frame, text='9RatingVotes')
#             nine_rating_votes_label.grid(row=0, column=6)
#             nine_rating_votes_input = Label(second_frame, text=str(ratings[6]))
#             nine_rating_votes_input.grid(row=1, column=6)
#             eight_rating_percentage_label = Label(second_frame, text='8Rating%')
#             eight_rating_percentage_label.grid(row=0, column=7)
#             eight_rating_percentage_input = Label(second_frame, text=str(ratings[7]))
#             eight_rating_percentage_input.grid(row=1, column=7)
#             eight_rating_votes_label = Label(second_frame, text='8RatingVotes')
#             eight_rating_votes_label.grid(row=0, column=8)
#             eight_rating_votes_input = Label(second_frame, text=str(ratings[8]))
#             eight_rating_votes_input.grid(row=1, column=8)
#             seven_rating_percentage_label = Label(second_frame, text='7Rating%')
#             seven_rating_percentage_label.grid(row=0, column=9)
#             seven_rating_percentage_input = Label(second_frame, text=str(ratings[9]))
#             seven_rating_percentage_input.grid(row=1, column=9)
#             seven_rating_votes_label = Label(second_frame, text='7RatingVotes')
#             seven_rating_votes_label.grid(row=0, column=10)
#             seven_rating_votes_input = Label(second_frame, text=str(ratings[10]))
#             seven_rating_votes_input.grid(row=1, column=10)
#             six_rating_percentage_label = Label(second_frame, text='6Rating%')
#             six_rating_percentage_label.grid(row=0, column=11)
#             six_rating_percentage_input = Label(second_frame, text=str(ratings[11]))
#             six_rating_percentage_input.grid(row=1, column=11)
#             six_rating_votes_label = Label(second_frame, text='6RatingVotes')
#             six_rating_votes_label.grid(row=0, column=12)
#             six_rating_votes_input = Label(second_frame, text=str(ratings[12]))
#             six_rating_votes_input.grid(row=1, column=12)
#             five_rating_percentage_label = Label(second_frame, text='5Rating%')
#             five_rating_percentage_label.grid(row=0, column=13)
#             five_rating_percentage_input = Label(second_frame, text=str(ratings[13]))
#             five_rating_percentage_input.grid(row=1, column=13)
#             five_rating_votes_label = Label(second_frame, text='5RatingVotes')
#             five_rating_votes_label.grid(row=0, column=14)
#             five_rating_votes_input = Label(second_frame, text=str(ratings[14]))
#             five_rating_votes_input.grid(row=1, column=14)
#             four_rating_percentage_label = Label(second_frame, text='4Rating%')
#             four_rating_percentage_label.grid(row=0, column=15)
#             four_rating_percentage_input = Label(second_frame, text=str(ratings[15]))
#             four_rating_percentage_input.grid(row=1, column=15)
#             four_rating_votes_label = Label(second_frame, text='4RatingVotes')
#             four_rating_votes_label.grid(row=0, column=16)
#             four_rating_votes_input = Label(second_frame, text=str(ratings[16]))
#             four_rating_votes_input.grid(row=1, column=16)
#             three_rating_percentage_label = Label(second_frame, text='3Rating%')
#             three_rating_percentage_label.grid(row=0, column=17)
#             three_rating_percentage_input = Label(second_frame, text=str(ratings[17]))
#             three_rating_percentage_input.grid(row=1, column=17)
#             three_rating_votes_label = Label(second_frame, text='3RatingVotes')
#             three_rating_votes_label.grid(row=0, column=18)
#             three_rating_votes_input = Label(second_frame, text=str(ratings[18]))
#             three_rating_votes_input.grid(row=1, column=18)
#             two_rating_percentage_label = Label(second_frame, text='2Rating%')
#             two_rating_percentage_label.grid(row=0, column=19)
#             two_rating_percentage_input = Label(second_frame, text=str(ratings[19]))
#             two_rating_percentage_input.grid(row=1, column=19)
#             two_rating_votes_label = Label(second_frame, text='2RatingVotes')
#             two_rating_votes_label.grid(row=0, column=20)
#             two_rating_votes_input = Label(second_frame, text=str(ratings[20]))
#             two_rating_votes_input.grid(row=1, column=20)
#             one_rating_percentage_label = Label(second_frame, text='1Rating%')
#             one_rating_percentage_label.grid(row=0, column=21)
#             one_rating_percentage_input = Label(second_frame, text=str(ratings[21]))
#             one_rating_percentage_input.grid(row=1, column=21)
#             one_rating_votes_label = Label(second_frame, text='1RatingVotes')
#             one_rating_votes_label.grid(row=0, column=22)
#             one_rating_votes_input = Label(second_frame, text=str(ratings[22]))
#             one_rating_votes_input.grid(row=1, column=22)
#
# # else:
# #     root = tkinter.Tk()
# #     root.title('User Ratings')
# #     root.geometry('200x200')
# #     no_ratings_label = Label(second_frame, text='This shows user ratings are not in the show_ratings table')
# #     no_ratings_label.grid(row=0, column=0)
