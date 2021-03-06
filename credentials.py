import string
import random
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

    def delete_credentials(self):
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

    @classmethod
    def credential_exist(cls,account):
        '''
        Method that checks if credential exists from the credentials list.
        Args:
            account: Account to search if it exists
        Returns:
        Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    def generatePassword(stringLength=8):
        '''
        method that generates a random password string of letters,digits and special characters
        '''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))