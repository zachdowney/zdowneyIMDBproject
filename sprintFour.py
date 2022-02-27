import tkinter

from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox
from tkinter import *


import sprintOne
import sprintTwo
import sprintThree
import main
import sqlite3
import requests


# class SprintFour(QWidget):
#
#     def __init__(self, data_to_show:dict):
#         super().__init__()
#         self.data = sprintOne.get_data("https://imdb-api.com/en/API/Top250TVs/")
#         self.setup_window()
#
#     def setup_window(self):
#         self.setWindowTitle("Tv/Movie information")
#         self.setGeometry(750, 100, 900, 200)
#         label = QLabel(self)
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
    show_button = tkinter.Button(root, text='Show Info')
    show_button.grid(row=1, column=1, padx=10, pady=20)
    movie_button = tkinter.Button(root, text='Movie Info')
    movie_button.grid(row=2, column=1, padx=10, pady=10)
    root.mainloop()



