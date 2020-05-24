import unittest
from credentials import Credentials

class CredentialsTest(unittest.TestCase):
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_credentials = Credentials('Twitter','paulmburu65','paulmburu08@gmail.com','python3465')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_name,'Twitter')
        self.assertEqual(self.new_credentials.username,'paulmburu65')
        self.assertEqual(self.new_credentials.email,'paulmburu08@gmail.com')
        self.assertEqual(self.new_credentials.password,'python3465')

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the account credentials object is saved into
        the credentials list
        '''

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple account credentials
        objects to our credentials_list
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials('Instagram','mburupavl','paulmburu08@gmail.com','think4562')
        test_credentials.save_credentials()

        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove and account credentials from our credentials list
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials('Instagram','mburupavl','paulmburu08@gmail.com','think4562')
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_by_name(self):
        '''
        test to check if we can find an account credentials by account_name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials('instagram','mburupavl','paulmburu08@gmail.com','think4562')
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_name('instagram')

        self.assertEqual(found_credentials.username,test_credentials.username)

    def test_display_credentials(self):
        '''
        method that returns a list of all account credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        

if __name__ == '__main__':
    unittest.main()