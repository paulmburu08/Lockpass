#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_account(first_name,last_name,email,password):
    '''
    Function to create a new lockpass account
    '''

    new_user = User(first_name,last_name,email,password)
    return new_user

def save_account(account):
    '''
    Function to save user account
    '''
    account.save_account()

def delete_account(account):
    '''
    Function to delete user account
    '''
    account.delete_account()





if __name__ == '__main__':
    main()