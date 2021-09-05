import random
from run import display_users
import string
class Credentials:
    """
    Class that generates new instances of credentials
    """
    pass

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