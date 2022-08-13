from operator import is_
from user_operations.user import Authorization
from user_operations.user import User
from user_operations.user import Session
from window_operations.menu import Menu
from database_operations.database import DatabaseOperator


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

        is_true = True

        while(is_true):

            if self.main_session.is_logged_in():
                self.main_menu.print_menu(self.main_session, self.db_operator)
            else:
                try:
                    prelogin_input = self.main_menu.print_prelogin_menu()

                    if int(prelogin_input) == 1:

                        user_inputs = self.main_menu.login_menu()

                        if len(user_inputs[0])>1 or len(user_inputs[1])<1:
                            self.main_auth.login(
                                user_inputs[0], user_inputs[1], self.main_session, self.db_operator)
                        else:
                            self.main_loop()
                        
                    elif int(prelogin_input) == 2:

                        user_inputs = self.main_menu.register_menu()

                        self.main_auth.register(
                            user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3], self.main_session, self.db_operator
                        )

                    elif int(prelogin_input) == 3:
                        is_true=False

                except KeyboardInterrupt:
                    self.main_loop()


if __name__ == '__main__':
    main = Main()
    main.main_loop()
