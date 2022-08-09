
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

    def load_data(self, table_name):
        query = f"SELECT * from {table_name}"
        self.cursor.execute(query)
        results = self.cursor.fetchall()

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

    def find_newest(self, cell_name, table_name):
        query = f"SELECT MAX({cell_name}) FROM {table_name}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        return result
