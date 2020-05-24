import unittest
from user import User

class UserTest(unittest.TestCase):
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_user = User('Paul','Mburu','paulmburu08@gmail.com','python34562')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.login_details = []
