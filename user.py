class User:
    '''
    class that generate new instances of user account login details
    '''

    login_details = []

    def __init__(self,first_name,last_name,email,password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_account(self):
        '''
        save_account method saves account details to the login_details
        '''

        User.login_details.append(self)

    def delete_account(self):
        '''
        delete_account method deletes a saved account details from the login_details
        '''

        User.login_details.remove(self)

