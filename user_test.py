import unittest
from user import User 

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.Testcase: Testcase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up methodto run before each test cases.
        '''
        self.new_user = User("Ratchez","Pass1234")

        def test_init(self):
            '''
            test_init test case to test if the object is initailized properly
            '''

            self.assertEqual(self.new_user.username,"Ratchez")
            self.assertEqual(self.new_user.password,"Pass1234")

if __name__ == '__main__':
    unittest.main()