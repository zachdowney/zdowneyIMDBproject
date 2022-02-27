import tkinter
import pprint
from tkinter import ttk

from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox
from tkinter import *

# https://www.youtube.com/watch?v=AK1J8xF4fuk&t=1360s video helped with everything


import sprintOne
import sprintTwo
import sprintThree
import main
import sqlite3
import requests


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
    root.geometry('150x150')

    # Button
    show_button = tkinter.Button(root, text='Show Info', command=lambda: pop_shows_gui())
    show_button.grid(row=1, column=1, padx=10, pady=20, )
    movie_button = tkinter.Button(root, text='Movie Info', command=lambda: pop_movies_gui())
    movie_button.grid(row=2, column=1, padx=10, pady=10)
    root.mainloop()


def pop_shows_gui():
    pop_tv = sprintOne.get_data("https://imdb-api.com/en/API/MostPopularTVs/")
    root = tkinter.Tk()
    root.title("Most Popular TV Shows")
    root.geometry('2000x2000')

    # https://www.youtube.com/watch?v=0WafQCaok6g&t=613s
    # showed me how to add a scrollbar
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

    # Button
    id_label = tkinter.Label(second_frame, text='id')
    id_label.grid(row=0, column=0)
    rankings_button = tkinter.Button(second_frame, text='rank')
    rankings_button.grid(row=0, column=1)
    up_down_button = tkinter.Button(second_frame, text='rankUpDown')
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

    conn = sqlite3.connect('shows_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('''SELECT * from popular_tv''')

    for i in range(len(pop_tv)):
        record = cursor.fetchone()
        id_input = Label(second_frame, text=str(record[0]))
        id_input.grid(row=i+1, column=0)
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


def pop_movies_gui():
    pop_movies = sprintOne.get_data("https://imdb-api.com/en/API/MostPopularMovies/")
    root = tkinter.Tk()
    root.title("Most Popular Movies")
    root.geometry('2000x2000')

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


    # Button
    id_label = tkinter.Label(second_frame, text='id')
    id_label.grid(row=0, column=0)
    rankings_button = tkinter.Button(second_frame, text='rank')
    rankings_button.grid(row=0, column=1)
    up_down_button = tkinter.Button(second_frame, text='rankUpDown')
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

    conn = sqlite3.connect('shows_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('''SELECT * from popular_movies''')

    for i in range(len(pop_movies)):
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





