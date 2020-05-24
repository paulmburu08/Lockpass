from user import User

class Credentials(User):
    '''
    class that generate new instances of credentials
    '''

    credentials_list = []

    def __init__(self,first_name,last_name,email,password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password