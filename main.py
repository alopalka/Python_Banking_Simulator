import sqlite3
import platform
import os

connection = sqlite3.connect('bank_db')

cursor = connection.cursor()


class Screen():

    def clear_screen():
        os_type = platform.system()

        if os_type == "Linux":
            os.system('clear')
        else:
            os.system('cls')

    def print_screen():
        pass
