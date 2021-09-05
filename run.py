#!/usr/bin/env python3.8
from user import User

def create_user(fname,lname,email,uname,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,email,uname,password)
    return new_user

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

def find_user(email):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_email(email)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Hello Welcome to the Password Locker App. Please input your username")
    user_username = input()

    print(f"Hello {user_username}. what would you like to do?")
    print('/n')

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
            

            