import unittest
# from unittest.case import TestCase
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.Testcase: Testcase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Roy","Rasugu","royratchizi@gmail.com","Ratchez","Pass1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Roy")
        self.assertEqual(self.new_user.last_name,"Rasugu")
        self.assertEqual(self.new_user.email,"royratchizi@gmail.com")
        self.assertEqual(self.new_user.username,"Ratchez")
        self.assertEqual(self.new_user.password,"Pass1234")
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved in to
        the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple users
        objects to our user_list 
        '''
        self.new_user.save_user()
        test_user = User("Brianna","Masiga","bree@yahoo.com","Bree","nighty")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our 
        user list
        '''
        self.new_user.save_user()
        test_user = User("Brianna","Masiga","bree@yahoo.com","Bree","nighty")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by email and display 
        information
        '''
        self.new_user.save_user()
        test_user = User("Brianna","Masiga","bree@yahoo.com","Bree","nighty")
        test_user.save_user()

        found_user = User.find_by_username("Bree")

        self.assertEqual(found_user.username,test_user.username)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Brianna","Masiga","bree@yahoo.com","Bree","nighty")
        test_user.save_user()

        user_exists = User.user_exist("Bree")

        self.assertTrue(user_exists)
    
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.Testcase: Testcase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Instagram","Ratchez","Pass1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account,"Instagram")
        self.assertEqual(self.new_credential.username,"Ratchez")
        self.assertEqual(self.new_credential.password,"Pass1234")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved in to
        the credential list
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
      
    def tearDown(self):
        '''
        tearDown method that does cean up after each test case has run. 
        '''
        Credentials.credentials_list = []

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credentials
        objects to our credential_list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Pinterest","Bree","Damn12")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove credentials from our
        credential list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Pinterest","Bree","Damn12")
        test_credential.save_credentials()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential_by_account(self):
        '''
        test to check if we can find a credential entry by account name and display
        the details of the credential
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Pinterest","Bree","Damn12")
        test_credential.save_credentials()

        found_credential = Credentials.find_by_account("Pinterest")

        self.assertEqual(found_credential.account,test_credential.account)

    def test_credential_exist(self):
        '''
        test to check if we can return a Boolean if we cannot find the credential.
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Pinterest","Bree","Damn12")
        test_credential.save_credentials()

        credential_exists = Credentials.credential_exist("Pinterest")

        self.assertTrue(credential_exists)
    
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
if __name__ == '__main__':
    unittest.main()