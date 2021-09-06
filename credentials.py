import random
from user import User
from run import display_users
import string
class Credentials:
    """
    Class that generates new instances of credentials
    """
    pass
    credentials_list = []

    def __init__(self,account,username,password):
        '''
        __init__method that helps us define properties for our objects.

        Args:
        account: New credential account.
        username: New credential username.
        password: New credential password.
        '''
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        save_credentials method saves credential objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes saved credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in a user's account and returns credentials that matches that
        account.

        Args:
            account: account to search for
        Returns:
            Credentials that matches the account.
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential