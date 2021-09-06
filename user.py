class User:
    """
    Class that generates new instances of users
    """
    pass
    user_list = []

    def __init__(self,first_name,last_name,email,username,password):

        '''
        __init__method that helps us define properties for our objects.

        Args:
        first_name: New user firstname.
        last_name: New user lastname.
        email: New user email.
        username: New user username.
        password: New user password.
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
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

    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in a username and returns a user that matches that 
        username.

        Args:
            username: User's name to search for
        Returns :
            User of person that matches the username. 
        '''
        for user in cls.user_list:
            if user.email == email:
                return user   

    @classmethod
    def user_exist(cls,email):
        '''
        Method that checks if user exists from the user list.
        Args:
            username: Users' to search if it exists
        Returns:
            Boolean: True or false depending if the user exists 
        ''' 
        for user in cls.user_list:
            if user.email == email:
                return True

        return False
    
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list