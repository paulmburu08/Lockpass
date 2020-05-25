#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import random
import string

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

def credential_exist(name):
    '''
    Function that check if a contact exists with that account name and return a Boolean
    '''
    return Credentials.credentials_exist(name)

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
    return Credentials.display_credentials()

def main():
    print('Welcome to LOCKPASS. Sign up below to be login into your account')
    print('\n')
    
    print('First name.....')
    f_name = input()

    print('Last name....')
    l_name = input()

    print('Email')
    email = input()

    print('Password')
    password = input()

    save_accounts(create_account(f_name,l_name,email,password))
    print('\n')

    while True:
        print(f'Hello {f_name}. What would you like to do?')
        print('\n')
        print('Use the codes: sc - Save existing account credentials, cc - Create new account credentials, dc - Display accounts credentials, fc - Find an account credentials , dlc - Delete account credentials , ex - Exit')

        code = input().lower()

        if code == 'sc':
            print('Save existing account credentials')
            print('-'*10)

            print('account name(All in small letters) i.e instragram , twitter e.t.c')
            a_name = input().lower()

            print('username')
            u_name = input()

            print('Email')
            e_address = input()

            print('Password')
            pass_word = input()

            save_credential(create_credentials(a_name,u_name,e_address,pass_word))
            print('\n')
            print(f'New {a_name} account credentials saved')
            print('\n')
            
        elif code == 'cc':
            print('Create new account credentials')
            print('-'*10)

            print('account name(all in small letters) i.e instragram , twitter e.t.c')
            a_name = input().lower()

            print('username')
            u_name = input()

            print('Email')
            e_address = input()

            print('Password')
            print('-'*20)
            print('Use codes below to choose either to have your password generated for you or create your own password')
            print('gp - Password generated for you , cp - Create your own password')

            password_code = input().lower()
            a = random.choice(string.ascii_lowercase)
            b = random.choice(string.ascii_lowercase)
            c = random.choice(string.ascii_lowercase)
            d = random.randint(0,9)
            e = random.randint(0,9)
            f = random.randint(0,9)

            password = f'{a}{b}{c}{d}{e}{f}'
            if password_code == 'gp': 
                print('\n') 
                print(f'Password {password} generated')

                save_credential(create_credentials(a_name,u_name,e_address,password))
                print('-'*20)
                print(f'New {a_name} account credentials saved')
                print('\n')

            elif password_code == 'cp':
                print('Input your password')
                password = input()

                save_credential(create_credentials(a_name,u_name,e_address,password))
                print('\n')
                print(f'New {a_name} account credentials saved')
                print('\n')

            else:
                print('\n')
                print('Please input the correct code')
                print('\n')

        elif code == 'dc':
            if display_credential():
                print('Here is a list of all you account credentials')
                print('\n')

                for credential in display_credential():
                    print(f'{credential.account_name}')
                    print(f'Username - {credential.username}')
                    print(f'email - {credential.email}')
                    print(f'Password - {credential.password}')
                    print('\n')

            else:
                print('\n')
                print("You dont seem to have any account credentials saved yet")
                print('\n')

        elif code == 'fc':
            print('Enter account name you are searching for')
            search_name = input().lower()
            if credential_exist(search_name):
                search_credentials = find_credentials(search_name)
                print('\n') 
                print(f'{search_credentials.account_name}')
                print('-'*20)
                print(f'Username....{search_credentials.username}')
                print(f'email....{search_credentials.email}')
                print(f'Password....{search_credentials.password}')
                print('\n')

            else:
                print('\n')
                print('That account credentials does not exist')
                print('\n')

        elif code == 'dlc':
            print('Enter account name of credentials to be deleted')
            search_name = input().lower()
            search_credentials = find_credentials(search_name)
            del_credentials(search_credentials)

            print('\n')
            print(f'{search_credentials.account_name} credentials deleted.')
            print('\n')

        elif code == 'ex':
            print('Bye.....')
            break

        else:
            print('\n')
            print('Please use the codes provided. Thank you')


if __name__ == '__main__':
    main()