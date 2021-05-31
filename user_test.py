import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("reilly", "1234")

    def tearDown(self):
        User.user_list = []

    def test_instance(self):
        self.assertEqual(self.new_user.user, "reilly")
        self.assertEqual(self.new_user.password, "1234")

    def test_add_user(self):
        self.new_user.add_user()
        self.assertEqual(len(User.user_list), 1)

    def test_user_login(self):
        self.new_user.add_user()
        self.assertEqual(User.user_login("reilly", "1234"), True)



# if __name__ == '__main__':
#     unittest.main()
