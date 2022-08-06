from user_operations.user import Authorization
from user_operations.user import User
from user_operations.user import Session
from window_operations.menu import Menu

import sqlite3


class DatabaseOperator():

    def __init__(self):
        self.database_name = "bank_db"
        self.connection = self.setup_connection()
        self.cursor = self.setup_cursor()

    def __del__(self):

        self.connection.close()

    def setup_connection(self):

        connection = None

        try:
            connection = sqlite3.connect('bank_db.db')
        except:
            print("Database connection error")

        return connection

    def setup_cursor(self):

        cursor = self.connection.cursor()

        return cursor

    def save_instance(self):
        pass

    def load_data(self, table_name):
        query = f"SELECT * from {table_name}"
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        print(results)

        return results

    def find_match(self, table_name, matching_cell, searched_phrase):

        query = f"SELECT * from {table_name} WHERE {matching_cell} = '{searched_phrase}'"

        self.cursor.execute(query)

        result = self.cursor.fetchone()

        return result

    def write_data(self, table_name, cell_name, values):

        query = f"INSERT INTO {table_name} {*cell_name,} VALUES {*values,}"

        self.cursor.execute(query)

        self.connection.commit()

    def update_data_one_item(self, table_name, cell_value, value, matching_cell, matching_value):

        query = f"UPDATE {table_name} SET {cell_value} = '{value}' WHERE {matching_cell} = '{matching_value}'"

        self.cursor.execute(query)

        self.connection.commit()


class Main():

    def __init__(self) -> None:
        self.db_operator = DatabaseOperator()
        self.transactions = self.db_operator.load_data("Transactions")
        self.users = self.db_operator.load_data("Users")
        self.wallets = self.db_operator.load_data("Wallets")
        self.main_session = Session()
        self.main_menu = Menu()
        self.main_user = ""

        self.main_auth = Authorization(self.users)

    def main_loop(self):

        if self.main_session.is_logged_in():
            self.main_menu.print_menu(self.main_session, self.db_operator)
        else:
            user_inputs = self.main_menu.login_menu()

            self.main_auth.login(
                user_inputs[0], user_inputs[1], self.main_session, self.db_operator)

        self.main_loop()


if __name__ == '__main__':
    main = Main()
    main.main_loop()
