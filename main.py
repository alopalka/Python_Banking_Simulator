import sqlite3
import platform
import os

from user_operations.user import Session
from user_operations.user import User
from user_operations.user import Authorization


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


class Menu():

    def __init__(self) -> None:
        self.logo = """                             .7GB55BG7.                                                  
                                               :JBBY!?GG77YBB?.                                               
                                            ^YBGJ!?B@@@@@@B?!JBBY:                                            
                                         ~5BG?!J#@@@@@@@@@@@@#J!?GB5^                                         
                                     .!G#G?75&@@@@@@@@@@@@@@@@@@&57?G#P!.                                     
                                    ^YP!.:?PGPPPPPPPPPPPPPPPPPPPPGP?:.!PY^                                    
                                 ^GGPPPPPPPPPPP55555PPPP55PPP55PPP5PPGP5PPGG^                                 
                                    :::::.     :::::.  .::. .::. :::: .:::                                    
                                   ^@@@@@@&?  ^@@@@@Y  #@@G Y@@5 &@@& B@@G                                    
                                   ~@@@..@@@. J@@@@@#  #@@@^J@@5 &@@& @@@.                                    
                                   ~@@@..@@@: B@@B.@@. #@@@#5@@5 &@@&&@@Y                                     
                                   ~@@@@@@@?  &@@..@@~ #@@@@@@@5 &@@@@@@.                                     
                                   ~@@@G5@@@^.@@@`.@@5 #@@&@@@@5 &@@@@@@?                                     
                                   ~@@@..@@@?!@@@@@@@& #@@?&@@@5 &@@&G@@@                                     
                                   ~@@@..@@@?P@@@P#@@@:#@@~?@@@5 &@@& @@@Y                                    
                                   ^@@@@@@&G.#@@& ~@@@!G@@^ &@@Y #@@# B@@&                                    
                                  ..:::::....:::...:::..::...::...::...:::..                                  
                                 ^GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG^                                 
                               ?PP555555555555555555555555555555555555555555PP?                               
                            ~JJ555555555555555555555555555555555555555555555555JJ^                            
                          ^^J55YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY55?^^"""

    @staticmethod
    def clear_window():
        os_type = platform.system()

        if os_type == "Linux":
            os.system('clear')
        else:
            os.system('cls')

    def print_menu(self, user):

        self.clear_window()

        print(self.logo)


        print(f"Welcome back, {user.first_name}\n")
        print("What do you want to do today?")
        print("1 - Send money")
        print("2 - Exchange")
        print("3 - Logout")
        user_choice = input()

    def print_prelogin_menu(self):

        self.clear_window()

        print(self.logo)

        print("\n Welcome, what do you want to do?")
        print("\n 1 - Login")
        print("\n 2 - Register")

    def login_menu(self):

        self.clear_window()

        print(self.logo)

        input_username = input("\n Username:")
        input_password = input("\n Password:")

        return [input_username, input_password]


class Main():

    def __init__(self) -> None:
        self.database_operator = DatabaseOperator()
        self.transactions = self.database_operator.load_data("Transactions")
        self.users = self.database_operator.load_data("Users")
        self.wallets = self.database_operator.load_data("Wallets")
        self.main_session = Session()
        self.main_menu = Menu()
        self.main_user = ""

        self.main_auth = Authorization(self.users)

    def main_loop(self):


        if self.main_session.is_logged_in():
            self.main_menu.print_menu(self.main_session.user)
        else:
            user_inputs = self.main_menu.login_menu()


            self.main_auth.login(user_inputs[0], user_inputs[1], self.main_session)

            self.main_loop()


if __name__ == '__main__':
    main = Main()
    main.main_loop()
