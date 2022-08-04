

class Session():

    def __init__(self,user=None,logged_in=False):
        self.user=user
        self.logged_in=logged_in




class User():

    def __init__(self,id,username,password,first_name,last_name):
        self.id=id
        self.username=username
        self.password=password
        self.first_name=first_name
        self.last_name=last_name
        