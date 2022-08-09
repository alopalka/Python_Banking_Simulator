from money_operations.wallet import Wallet
from secrets import values

import hashlib


class Session():

    def __init__(self, user=None, logged_in=False, wallet=None):
        self.user = user
        self.logged_in = logged_in
        self.wallet = wallet

    def is_logged_in(self):

        if self.logged_in:
            return True
        else:
            return False


class Authorization():

    def __init__(self, users):
        self.users = users
        self.login_pass_dict = {}

        self.set_values()

    def set_values(self):

        for user in self.users:
            self.login_pass_dict.update({f'{user[1]}': user[2]})

    @staticmethod
    def hash_text(text):
        salt = values.get("salt")

        key = hashlib.pbkdf2_hmac(
            'sha256',
            text.encode(),
            salt,
            100000
        )

        return key

    def user_existance(self, username, password):
        key_list = list(self.login_pass_dict.keys())
        values_list = list(self.login_pass_dict.values())

        try:
            user_index = key_list.index(username)
            password_index = values_list.index(password)

            if user_index == password_index:
                return user_index
            else:
                return False
        except:
            return False

    def login(self, username, password, session, db_operator):
        password = self.hash_text(password)
        result = self.user_existance(username, password)

        if result is not False:
            session.logged_in = True
            exact_user = self.users[result]
            session.user = User(
                exact_user[0], exact_user[1], exact_user[2], exact_user[3], exact_user[4], exact_user[5])
            wallet_id = exact_user[5]
            wallet = db_operator.find_match("Wallets", "id", wallet_id)
            session.wallet = Wallet(
                wallet[0], wallet[1], wallet[2], wallet[3], wallet[4])

        else:
            return False

    def register(self, username, password, first_name, last_name, session, db_operator):
        password = self.hash_text(password)
        result = self.user_existance(username, password)

        if result is False:
            highest_wallet_id = int(
                db_operator.find_newest("id", "Wallets")[0])+1
            current_wallet = Wallet(highest_wallet_id, 0, 0, 0, 0)
            current_wallet.create_empty(db_operator)

            session.wallet = current_wallet
            highest_user_id = int(
                db_operator.find_newest("id", "Users")[0])+1
            current_user = User(highest_user_id,username,password,first_name,last_name,highest_user_id)
            current_user.create_empty(db_operator)

            session.user=current_user

            session.logged_in = True

        else:

            return False


class User():

    def __init__(self, id, username, password, first_name, last_name, wallet_id):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.wallet_id = wallet_id

    def create_empty(self, db_operator):

        cell_names = ['id', 'username', 'password',
                      'first_name', 'last_name', 'wallet_key']

        values = [self.id, self.username, self.password,
                  self.first_name, self.last_name, self.wallet_id]

        db_operator.write_data("Users", cell_names, values)

    def __str__(self):
        return f" First name: {self.first_name}\n" + f" Last name: {self.last_name}\n" + f" Username: {self.username}\n"
