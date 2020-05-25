from user import User

class Credentials(User):
    '''
    class that generate new instances of credentials
    '''

    credentials_list = []

    def __init__(self,account_name,username,email,password):

        self.account_name = account_name
        self.username = username
        self.email = email
        self.password = password

    def save_credentials(self):
        '''
        save_credentials method saves credentials to the credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def credentials_exist(cls,name):
        '''
        Method that checks if an account credentials exists from the credentials list.
        Args:
        name: account name to search if it exists.
        Returns :
        Boolean: True or false depending if the account credentials exists.
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == name:
                return True
        
        return False

    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in an account_name and returns credentials that matches that account_name.
        Args:
        account_name: account_name to search for
        Returns :
        Credentials of account that matches the account_name.
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == name :
                return credentials

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''

        return cls.credentials_list

    


