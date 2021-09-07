#!/usr/bin/env python3.8
from credentials import Credentials
from user import User

def create_user(fname,lname,email,uname,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,email,uname,password)
    return new_user

def login_user(username,password):
    '''
    Function that checks whether a user exist and then allows them to log in.
    '''

    check_user = User.verify_user(username,password)
    return check_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def create_credential(account,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(account,username,password)
    return new_credential

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    Function to delete credentials 
    '''
    credentials.delete_credentials()

def find_credentials(account):
    '''
    Function that finds a user's credentials by account and returns the credential
    '''
    return Credentials.find_by_account(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password = Credentials.generatePassword()
    return auto_password

def main():
    print("Hello Welcome to the Password Locker App...\n Please enter the following to proceed.\n CA --- Create a New Account  \n HA ---  Have An Account  \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        
        fname = input("First name: ")
        lname = input("Last name: ")
        email = input("Email: ")
        uname = input("Username: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
            
        save_users(create_user(fname,lname,email,uname,password))
        print("*" * 85)
        print(f"Hello {fname} {lname}, Your accout has been created succesfully! here are more of your details Email: {email}, Username: {uname} and your password is: {password}")
        print("*" * 85)

    elif short_code == "ha":
        print("*" * 50)
        print("Enter your Username and Password to login:")
        print('*' * 50)
        uname = input("Username: ")
        password = input("password: ")
        login = login_user(uname,password)
        if login_user == login:
            print(f"Hello {uname}.Welcome to the Password locker APP")
            print('\n')

    while True:
        print("Use these keys:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find specified credentials \n Gp - Generate random password \n D - Delete Credential \n EX - Exit the app \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            username = input()
            while True:
                print(" TP - To type youre password on your already existing account:\n GP- To be generated for Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")

            save_credentials(create_credential(account,username,password))
            print('\n')
            print(f"Account Credentials for: {account} - Username: {username} & Password:{password} was created successfully") 
            print('\n')

        elif short_code == "dc":
            if display_credentials():
                print("Here's your list of accounts: ")

                print('*' * 30)
                print('_'*30)

                for account in display_credentials():
                    print(f" Account:{account.account} \n Username:{username}\n Password:{password}")
                    print('_' * 30)
                print('*' * 30)
            else:
                print("Ooops...Sorry, we dont seem to find youre credentials.........")

        elif short_code == "fc":
            print("Enter the Account handle you want to search for")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print(f"Account Name: {search_credential.account}")
                print('-' * 50)
                print(f"Username: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("The Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the Account handle credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_" * 50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for: {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("The Credential you want to delete does not exist")
        
        elif short_code == 'gp':
            password = generate_Password()
            print(f" {password} Has been generated successfully. You may proceed to use your account")
        
        elif short_code == 'ex':
            print("Bye and Thanks for using our App.")
            break
        else:
            print("Didn't get that, please use the short codes")

if __name__ == '__main__':
    main()
        