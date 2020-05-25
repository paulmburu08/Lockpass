#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

#User

def create_account(first_name,last_name,email,password):
    '''
    Function to create a new lockpass account
    '''

    new_user = User(first_name,last_name,email,password)
    return new_user

def save_accounts(account):
    '''
    Function to save user account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to delete user account
    '''
    account.delete_account()

#Credentials

def create_credentials(account_name,username,email,password):
    '''
    Function to create new account credentials
    '''

    new_credentials = Credentials(account_name,username,email,password)
    return new_credentials

def save_credential(credentials):
    '''
    Function to save account credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete account credentials
    '''
    credentials.delete_credentials()

def find_credentials(name):
    '''
    Function that finds credentials by account_name and returns credentials
    '''
    return Credentials.find_by_name(name)

def display_credential():
    '''
    Function that returns all the saved account credentials
    '''
    Credentials.display_credentials()

def main():
    print('Welcome to LOCKPASS. Sign up below to be login into your account')
    print('\n')
    
    print('First name.....')
    f_name = input()

    print('Last name....')
    l_name = input()

    print('email')
    email = input()

    print('password')
    password = input()

    save_accounts(create_account(f_name,l_name,email,password))
    print('\n')

    while True:
        print(f'Hello {f_name}. What would you like to do?')
        print('\n')
        print('Use the codes: sc - Save existing account credentials, cc - Create new account credentials')


if __name__ == '__main__':
    main()