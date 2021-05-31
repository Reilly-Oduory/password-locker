from random import *
import string

class Credential:

    credential_list = []

    def __init__(self, user_name, password, email_address, account):
        self.user_name = user_name
        self.password = password
        self.email_address = email_address
        self.account =account

    def save_credential(self):
        Credential.credential_list.append(self)

    @classmethod
    def find_by_account(cls, account_name):
        for credential in cls.credential_list:
            if credential.account == account_name:
                return credential

    def modify_account_password(self, new_credential_password):
        self.password = new_credential_password

    def delete_credential(self):
        Credential.credential_list.remove(self)

    @classmethod
    def display_credentials(cls):
        return cls.credential_list

