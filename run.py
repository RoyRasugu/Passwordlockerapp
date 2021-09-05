#!/usr/bin/env python3.8
from user import User

def create_user(uname,password):
    '''
    Function to create a new user
    '''
    new_user = User(uname,password)
    return new_user

