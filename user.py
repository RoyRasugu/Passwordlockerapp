class User:
    """
    Class that generates new instances of contacts
    """
    pass
    user_list = []

    def __init__(self,username,password):

        '''
        __init__method that helps us define properties for our objects.

        Args:
        username: New user username.
        password: New user password
        '''

        self.username = username
        self.password = password
    
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved contact from the user_list
        '''

        User.user_list.remove(self)    