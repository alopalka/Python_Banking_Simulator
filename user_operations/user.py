

class Session():

    def __init__(self, user=None, logged_in=False):
        self.user = user
        self.logged_in = logged_in

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

    def login(self, username, password, session):

        result = self.user_existance(username, password)


        if result is not False:
            session.logged_in = True
            exact_user = self.users[result]

            session.user = User(exact_user[0],exact_user[1],exact_user[2],exact_user[3],exact_user[4])
        else:
            return False

    def register(self, username, password, first_name, last_name):
        pass


class User():

    def __init__(self, id, username, password, first_name, last_name):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"
