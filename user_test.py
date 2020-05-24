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

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,'Paul')
        self.assertEqual(self.new_user.last_name,'Mburu')
        self.assertEqual(self.new_user.email,'paulmburu08@gmail.com')
        self.assertEqual(self.new_user.password,'python34562')

    def test_save_account(self):
        '''
        test_save_account test case to test if the new_user object is saved into
        the login_details
        '''

        self.new_user.save_account()
        self.assertEqual(len(User.login_details),1)

    def test_delete_account(self):
        '''
        test_delete_contact to test if we can remove an account from our login_details
        '''

        self.new_user.save_account()
        self.new_user.delete_account()

        self.assertEqual(len(User.login_details),0)

if __name__ == '__main__':
    unittest.main()
