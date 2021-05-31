class User:

    user_list = []

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def add_user(self):
        User.user_list.append(self)

    @classmethod
    def user_login(cls, identification, key):
        returned_user = User('', '')
        for user in cls.user_list:
            if identification == user.user:
                returned_user.user = user.user
                returned_user.password = user.password
        if returned_user.password == key:
            return True
        else:
            print("login failed")


