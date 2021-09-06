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
    Function to delete a contact
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

def main():
    print("Hello Welcome to the Password Locker App...\n Please enter the following to proceed.\n")
    user_username = input()

    print(f"Hello {user_username}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create a new user, du - display users, fu - find a user, ex - exit the user list ")

        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-"*50)

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Email address ...")
            e_address = input()

            print("Username name ...")
            u_name = input()

            print("User password ...")
            u_password = input()

            save_users(create_user(f_name,l_name,e_address,u_name,u_password))
            print('\n')
            print(f"New User {u_name} created")
            print('\n')

        elif short_code == 'du':
            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} {user.email} {user.username} {user.password}")

                    print('\n')
            else:
                print('\n')
                print("It seems to be there are no users saved")
                print('\n')

        elif short_code == 'fu':
            print("Enter the username you want to search for")

            search_name = input()
            if find_user(search_name):
                search_user = find_user(search_name)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 50)

                print(f"Email address.......{search_user.email}")

                print(f"Username name.......{search_user.username}")

            else:
                print("Sorry! The user does not exist")

        elif short_code == "ex":
            print("Bye and thanks for using our App.")
            break
        else:
            print("Didn't get that, please uae the short codes")

if __name__ == '__main__':
    main()
        