import platform
import os
import time

from money_operations.transfer import Transaction
from money_operations.exchange_rate import get_exchange_rate


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

        if os_type == "Linux" or os_type == "Darwin":
            os.system('clear')
        else:
            os.system('cls')

    def print_upper_section(self):
        self.clear_window()

        print(self.logo)
        print("\n\n")

    def print_incorrect_screen(self):
        self.clear_window()
        print("\n\n\n")
        print("\n There was a problem ")
        print("\n Incorrect data...")
        time.sleep(1)
        print("\n Please try again...")
        time.sleep(2)

    def send_money(self, session, db_operator):
        self.print_upper_section()

        user_currency = input("Which currency do you choose? (Currency)")
        user_amount = float(
            input("How much do you want to transfer? (Amount)").replace(',', '.'))
        user_recipient = input("Recipient username: ")

        possible_currencies = ['usd', 'pln', 'btc', 'eur']

        if(
            (len(user_currency) < 4 or len(user_currency) > 0)
            and user_currency.isalpha()
            and user_currency.lower() in possible_currencies
        ):

            taking_transaction = Transaction(
                currency=user_currency, wallet_from_id=session.user.wallet_id, amount=-user_amount)
            transaction_outcome = taking_transaction.make_transaction(
                session, db_operator, session.user.username)

            if transaction_outcome:
                current_transaction = Transaction(
                    currency=user_currency, wallet_from_id=session.user.wallet_id, amount=user_amount)
                current_transaction.make_transaction(
                    session, db_operator, user_recipient)

        else:
            self.print_incorrect_screen()

    def account_details(self, session):
        self.print_upper_section()

        print(session.user)
        print("\n ============================== \n Balance \n ============================== \n")
        print(session.wallet)

        input("\n Press any key to continue...")

    def exchange_money(self, session, db_operator):

        self.print_upper_section()

        print("\n Current prices:")
        print("\n USD/PLN - "+'%.2f' % get_exchange_rate("USD", "PLN"))
        print("\n EUR/PLN - "+'%.2f' % get_exchange_rate("EUR", "PLN"))
        print("\n BTC/PLN - "+'%.2f' % get_exchange_rate("BTC", "PLN"))

        possible_currencies = ['usd', 'pln', 'btc', 'eur']

        user_from_currency = input(
            "\nWhich currency do you want to exchange? (Currency FROM): ")
        user_to_currency = input(
            "Currency you want to receive? (Currency TO): ")
        user_amount_from = float(input(
            "What amount of your FROM currency do you want to exchange?: ").replace(',', '.'))

        if (
            (len(user_from_currency) < 4 or len(user_from_currency) > 0)
            and (len(user_to_currency) < 4 or len(user_to_currency) > 0)
            and (user_from_currency.isalpha() and user_to_currency.isalpha())
            and (user_from_currency.lower() in possible_currencies)
            and (user_to_currency.lower() in possible_currencies)
        ):

            calculated_exchange_rate = get_exchange_rate(
                user_from_currency, user_to_currency)
            money_to_recive = float(
                '%.8f' % calculated_exchange_rate) * user_amount_from

            taking_transaction = Transaction(
                currency=user_from_currency, wallet_from_id=session.user.wallet_id, amount=-user_amount_from)
            transaction_outcome = taking_transaction.make_transaction(
                session, db_operator, session.user.username)

            if transaction_outcome:
                giving_transaction = Transaction(
                    currency=user_to_currency, wallet_from_id=session.user.wallet_id, amount=money_to_recive)
                giving_transaction.make_transaction(
                    session, db_operator, session.user.username)

        else:
            self.print_incorrect_screen()

    def logout(self, session):
        session.user = None
        session.logged_in = False
        session.wallet = None

    def print_menu(self, session, db_operator):

        is_true = True

        while(is_true):

            self.print_upper_section()

            print(f" Welcome back, {session.user.first_name}\n")
            print(" What do you want to do today?")
            print(" 1 - Send money")
            print(" 2 - Exchange")
            print(" 3 - Account details")
            print(" 4 - Logout")

            try:
                user_choice = str(input("\n Choise: "))
                if user_choice == "1":
                    self.send_money(session, db_operator)
                elif user_choice == "2":
                    self.exchange_money(session, db_operator)
                elif user_choice == "3":
                    self.account_details(session)
                elif user_choice == "4":
                    self.logout(session)
                    is_true = False

            except KeyboardInterrupt:
                pass

    def print_prelogin_menu(self):

        self.print_upper_section()

        print("\n Welcome, what do you want to do?")
        print("\n 1 - Login")
        print("\n 2 - Register")
        print("\n 3 - Exit")

        input_user_choice = input("\n Choice: ")

        return input_user_choice

    def login_menu(self):

        self.print_upper_section()

        print("\n\n LOGIN \n\n")

        input_username = input("\n Username: ")
        input_password = input("\n Password: ")

        return [input_username, input_password]

    def register_menu(self):

        self.print_upper_section()

        print("\n\n REGISTER \n\n")

        input_username = input("\n Username: ")
        input_password = input("\n Password: ")
        input_first_name = input("\n First name: ")
        input_last_name = input("\n Last name: ")

        return [input_username, input_password, input_first_name, input_last_name]
