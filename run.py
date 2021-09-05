#!/usr/bin/env python3.8
from user import User

def create_user(uname,password):
    '''
    Function to create a new user
    '''
    new_user = User(uname,password)
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

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

    