class User:
    """
    Class that generates new instances of contacts
    """
    pass
    user_list = [] # Empty user list
    
    def __init__(self,username,password):

        '''
        __init__method that helps us define properties for our objects.

        Args:
        username: New user username.
        password: New user password
        '''

        # docstring removed for simplicity

        self.username = username
        self.password = password