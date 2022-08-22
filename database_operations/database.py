import sqlite3
from unittest import result


class DatabaseOperator():

    def __init__(self) -> None:
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

    def load_data(self, table_name: str):
        query = f"SELECT * from {table_name}"
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        return results

    def find_match(self, table_name: str, matching_cell: str, searched_phrase: str):
        query = f"SELECT * from {table_name} WHERE {matching_cell} = '{searched_phrase}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        return result

    def write_data(self, table_name: str, cell_names, values) -> None:
        query = f"INSERT INTO {table_name} {*cell_names,} VALUES {*values,}"

        self.cursor.execute(query)
        self.connection.commit()

    def update_data_one_item(self, table_name: str, cell_value: str, value: str, matching_cell: str, matching_value: str) -> None:
        query = f"UPDATE {table_name} SET {cell_value} = '{value}' WHERE {matching_cell} = '{matching_value}'"
        self.cursor.execute(query)
        self.connection.commit()

    def find_newest(self, cell_name: str, table_name: str):
        query = f"SELECT MAX({cell_name}) FROM {table_name}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        return result
