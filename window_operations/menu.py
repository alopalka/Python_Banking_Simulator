import platform
import os

class Menu():

    def __init__(self) -> None:
        self.logo = """                                                   .7GB55BG7.                                                  
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

    def send_money_menu(self):
        self.clear_window()

        print(self.logo)

        print("How ")

    def account_details(self,session):
        self.clear_window()

        print(self.logo)

        print(f"First name: {session.user.first_name}")
        print(f"Last name: {session.user.last_name}")
        print(f"Username: {session.user.username}")

        input("Press any key to continue...")


    def exchange_money(self):
        pass

    def logout(self,session):
        session.user=""
        session.logged_in=False

    def print_menu(self,session):

        is_true=True

        while(is_true):

            self.clear_window()

            print(self.logo)

            print(f"Welcome back, {session.user.first_name}\n")
            print("What do you want to do today?")
            print("1 - Send money")
            print("2 - Exchange")
            print("3 - Account details")
            print("4 - Logout")
            user_choice = str(input())

            if user_choice == "1":
                self.send_money()
            elif user_choice == "2":
                self.exchange_money()
            elif user_choice == "3":
                self.account_details(session)
            elif user_choice == "4":
                self.logout(session)
                is_true=False
            
        

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