

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
