#! /usr/bin/env python3
def verify_user(first_name, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = Credential.check_user(first_name, password)
    return checking_user


def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass


def create_credential(user_name, site_name, account_name, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(user_name, site_name, account_name, password)
    return new_credential


def save_credential(credential):
    '''
    Function to save a newly created credential
    '''
    Credential.save_credentials(credential)


def display_credentials(user_name):
    '''
    Function to display credentials saved by a user
    '''
    return Credential.display_credentials(user_name)
