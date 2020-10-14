#!/usr/bin/env python3

import sys
import os
import yaml

CONFIG = '/var/www/app/config/app.yml'
DATA_STORAGE = '/var/www/app/storage/data/data.yml'


# Load CONFIG
def load(file):
    if not os.path.exists(file):
        os.mknod(file)
    with open(file, 'r') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
    return content

# Store data into a yaml file using a yaml file and data object (dict) as parameters
def save(storage, credential_data):
    if not os.path.exists(storage):
        os.mknod(storage)
    with open(storage, 'w') as f:
       yaml.dump(credential_data,f)
    return True


def add_credential():

    # Create an empty dict that will contain all the credentials from the credential variable.
    #cache_credentials = dict()

    # Load existing credentials data
    cache_data = load(DATA_STORAGE)

    if (cache_data == None):
        save(DATA_STORAGE, dict())

    cache_data = load(DATA_STORAGE)

    increment_value = 0
    for increment in cache_data:
        print(increment)
        increment_value += 1

    # Get data from input
    #id = 666
    label = input('Insert your label: ')
    username = input('Insert your username: ')
    password = input('Insert your password: ')
    note = input('Note: ')

    # Store inputs in one credential variable (dict type)
    credential = {
        'id': increment_value,
        'label': label,
        'username': username,
        'password': password,
        'note': note,
    }
    # Assign a key at the empty dict (credentials) and assign credential as a value.
    # With a value on the [] parentesis we can assign or overwrite existing values on a list or dict.



    cache_data[increment_value] = credential
    save(DATA_STORAGE, cache_data)



    #TODO: append more then one credential into the data.yml (check old code and loops)





# Authentication
def auth(credentials,input_password):
    config_password  = credentials['config']['psw']
    if (input_password == config_password):
        return True
    return False



def main():
    print('# Aubergina Password Manager #')

    data = load(CONFIG)


    fullname = data['config']['fullname']
    username = data['config']['username']

    print('Welcome Sir ' + fullname + ' your username is ' + username + " \n\nInsert your password for authentication: ")

    password = input('Enter the Password: ')


    if (auth(data,password)):
        print('Hi ' + username + '. You logged in successfully')
        # User Option

        user_option = input('Choose a option:\n\na) add credential\nb) exit ')

        if (user_option == 'a'):
            add_credential()
        elif (user_option == 'b'):
            print('Goodbye :)')
            sys.exit(0)
        else:
            print('Option unavaible')
            sys.exit(2)
    else:
        print('stronzo')
        sys.exit(1)





# Execute
if __name__ == "__main__":
        main()


