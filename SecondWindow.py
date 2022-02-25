from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox

import sprintOne
import sprintTwo
import sprintThree
import sqlite3
import requests

class SprintFour(QWidget):

    def __init__(self, data_to_show:dict):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        