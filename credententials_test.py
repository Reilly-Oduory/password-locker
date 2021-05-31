import unittest
from credentials import Credential

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("qwerty", "password", "qwerty@testing.com", "twitter")

    def tearDown(self):
        Credential.credential_list = []

    def test_credential(self):
        self.assertEqual(self.new_credential.user_name, "qwerty")
        self.assertEqual(self.new_credential.password, "password")
        self.assertEqual(self.new_credential.email_address, "qwerty@testing.com")
        self.assertEqual(self.new_credential.account, "twitter")

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_many_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credential("wet", "1234", "wet@testing.com", "instagram")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_find_by_acount(self):
        self.new_credential.save_credential()
        test_credential = Credential("wet", "1234", "wet@testing.com", "instagram")
        test_credential.save_credential()
        found_credential = Credential.find_by_account("instagram")
        self.assertEqual(found_credential.account, test_credential.account)

    def test_modify_account_password(self):
        self.new_credential.save_credential()
        test_credential = Credential("wet", "1234", "wet@testing.com", "instagram")
        test_credential.save_credential()
        found_account = Credential.find_by_account("instagram")
        found_account.modify_account_password("yeah")
        self.assertEqual(test_credential.password, "yeah")

    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("wet", "1234", "wet@testing.com", "instagram")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_display_credentials(self):
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)





# if __name__ == '__main__':
#     unittest.main()
