# Passwordlockerapp
## Author

Roy Rasugu

## Description

This project is a python application that allows one to be able to create,store and manage their passwords for various accounts they have in social media platforms or elsewhere with use of their username and passwords for their various account. The application also has a feature to generate passwords for users too as well.

## User Stories
The user can:
* Create an account in the application or log in if they have an account
* Store their existing account login details for various accounts that they have registered for.
* Be generated for a new password for an account that they have not been registered for and store it in accordance for the account in the application.
* Delete stored account login details that they have no use for

## Installation / Setup instructions

#### Requirements for the application to operate
* python3.8

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/RoyRasugu/Passwordlockerapp.git```

* cd Passlockerapp

* code . or atom . based on the text editor you prefer.

### Running the Application
* To run the application, open the cloned file in the terminal and run the following commands:

       $ chmod +x run.py
       $ ./run.py
* To run test for the application
       $  python3.8 user_test.py

## Dependencies

1. Open the application on the terminal. Run the command ```$ ./run.py```. You will see the Home menu 'Hello Welcome to the Password Locker App...'. From here you have to options tp choose: either to create an account(CA ---), that is if you dont have or login if already have an existing account(HA ---).
2. If you select (CA), then you will have to input you're firstname, lastname, email, username and password. Afterwards you will receive a message saying 'Hello ```firstname lastname```, Your account has been created successfully! Here are more of your details ```Email: , Username: ``` and your password is: ```password```.
3. If you select (HA), then you you will just input youre username and password that you signed up with to login. With that Abbreviations menu will be displayed to help you navigate through the application.
4. To strore a new credential in the application, one will enter ```CC```, where they will enter the account, username and password. Of which in terms of the password, they have two options: 1 which is to enter ```Tp``` to key in a password or 2 which is to enter ```Gp``` to be generated for a password.
5. To be displayed for credentials, one will enter ```DC```, where a list of all credentials that have been stored will be displayed. Otherwise if there is no credentials stored one will receive this message ```Ooops...Sorry, we dont seem to find youre credentials.........```.
6. To find a stored credential based on the account name, one will enter ```FC```, where they will have to enter the account name they want to search for and it will return all account details.
7. To delete an existing credential that you have no need for, one will enter ```D```. Then they will enter the account name of the Credentials that they want to delete and it returns true if the account has been deleted, however if it is false, that means the account does not exist.
8. To exit the application, one will enter ```EX```. Then they will exit the application.

## Technologies Used

* Ptyhon3.8

## Contact Information

You can reach me on my email [royratchizi@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2021 **Roy Rasugu**

