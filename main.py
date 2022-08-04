import sqlite3
import platform
import os

from user_operations.user import Session
from user_operations.user import User


class DatabaseOperator():

    def __init__(self):
        self.database_name = "bank_db"
        self.cursor = self.setup_connection()

    def setup_connection(self):
        connection = sqlite3.connect('bank_db')
        cursor = connection.cursor()

        return cursor

    def save_instance(self):
        pass

    def load_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        results = self.cursor.fetchall()

        return results


class Window():

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
                                   ~@@@5J@@@. J@@@@@#  #@@@^J@@5 &@@&!@@@.                                    
                                   ~@@@J~@@@: B@@B@@@. #@@@#5@@5 &@@&&@@Y                                     
                                   ~@@@@@@@?  &@@7&@@~ #@@@@@@@5 &@@@@@@.                                     
                                   ~@@@G5@@@^.@@@:B@@5 #@@&@@@@5 &@@@@@@?                                     
                                   ~@@@7:@@@?!@@@@@@@& #@@?&@@@5 &@@&G@@@                                     
                                   ~@@@BG@@@?P@@@P#@@@:#@@~?@@@5 &@@&~@@@Y                                    
                                   ^@@@@@@&G.#@@& ~@@@!G@@^ &@@Y #@@# B@@&                                    
                                  ..:::::....:::...:::..::...::...::...:::..                                  
                                 ^GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG^                                 
                               ?PP555555555555555555555555555555555555555555PP?                               
                            ~JJ555555555555555555555555555555555555555555555555JJ^                            
                          ^^J55YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY55?^^\n\n\n"""

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


class Main():

    transactions=DatabaseOperator.load_data("Transaction")
    users=DatabaseOperator.load_data("Users")
    wallets=DatabaseOperator.load_data("Wallets")

    # user_class = User()
    # user_session = Session()

    def main_loop():

        if Session.is_logged_in():
            Window.print_menu()
