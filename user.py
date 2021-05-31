class User:

    user_list = []

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def add_user(self):
        User.user_list.append(self)

    @classmethod
    def user_login(cls, identification, userpass):
        for user in cls.user_list:
            if user.user == identification:
                if user.password == userpass:
                    return user
                else:
                    return ''

    def modify_password(self, new_password):
        self.password = new_password
