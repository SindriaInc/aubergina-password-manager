#!/usr/bin/env python3

import sys
import os
import yaml
import hashlib

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

def string_to_hash(string):
    password = string.encode('utf-8')
    hashed_password = hashlib.sha256(password).hexdigest()
    return hashed_password



def add_credential(session):

    # Load existing credentials data
    cache_data = load(DATA_STORAGE)

    if (cache_data == None):
        save(DATA_STORAGE, dict())

    cache_data = load(DATA_STORAGE)

    increment_value = 0
    for increment in cache_data:
        increment_value += 1

    # Get data from input

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

    new_credential = input(session['config']['username'] + ' do you want to add a new credential? y/n ')
    if (new_credential == 'y'):
        add_credential(session)
    elif (new_credential == 'n'):
        main_menu(session)
    else:
        print('Option unavaible')
        sys.exit(2)


def register():
    print('Welcome in Aubergina Password Manager.\n')

    fullname = input('Set your Fullname: ')
    username = input('Set your Username: ')
    password = input('Set your Password: ')
    hashed_password = string_to_hash(password)

    config = {
        'config': {
            'fullname': fullname,
            'username': username,
            'psw': hashed_password
        }
    }


    save(CONFIG, config)



# Authentication
def auth(credentials,input_password):

    config_password  = credentials['config']['psw']

    if (input_password == config_password):
        return True
    return False

def edit_credential(session):

    cache_data = load(DATA_STORAGE)

    id = int(input('Insert the id of the value you want to modify: '))

    credential = cache_data[id]

    label = input('Insert your label: ')
    username = input('Insert your username: ')
    password = input('Insert your password: ')
    note = input('Note: ')

    if (label != ''):
        credential['label'] = label

    if (username != ''):
        credential['username'] = username

    if (password != ''):
        credential['password'] = password

    if (note != ''):
        credential['note'] = note

    save(DATA_STORAGE, cache_data)
    main_menu(session)

def delete_credential(session):

    cache_data = load(DATA_STORAGE)

    id = int(input('Insert the id of the value you want to delete: '))

    cache_data.pop(id, None)

    save(DATA_STORAGE, cache_data)
    main_menu(session)

def show_credentials(session):

    print("Aviable credentials: \n")
    cache_data = load(DATA_STORAGE)

    for k,credential in cache_data.items():
        print("ID: " + str(credential['id']))
        print("Label: " + credential['label'])
        print("\n")

    main_menu(session)

def show_credential(session):

    id = int(input('Insert the ID from the credential you want to display: \n'))

    cache_data = load(DATA_STORAGE)

    if (not id in cache_data):
        print('Credential not aviable.')
        main_menu(session)

    print('Credential: \n')

    print('ID: '+ str(cache_data[id]['id']))
    print('Label: '+ cache_data[id]['label'])
    print('Username: '+ cache_data[id]['username'])
    print('Password: '+ cache_data[id]['password'])
    print('Note: '+ cache_data[id]['note']+'\n')


    main_menu(session)



def main_menu(session):
    # User Option

    user_option = input('Choose a option:\n\na) add credential\nb) edit credential\nc) delete credential\nd) show credentials\ne) show credential\nz) exit \n\n')

    if (user_option == 'a'):
        add_credential(session)
    elif (user_option == 'b'):
        edit_credential(session)
    elif (user_option == 'c'):
        delete_credential(session)
    elif (user_option == 'd'):
        show_credentials(session)
    elif (user_option == 'e'):
        show_credential(session)
    elif (user_option == 'z'):
        print('Goodbye :)')
        sys.exit(0)
    else:
        print('Option unavaible')
        sys.exit(2)



def main():
    print('# Aubergina Password Manager #')

    cache_config = load(CONFIG)
    if (cache_config == None):
        register()

    session = load(CONFIG)

    fullname = session['config']['fullname']
    username = session['config']['username']

    print('Welcome Sir ' + fullname + ' your username is ' + username + " \n\nInsert your password for authentication: ")

    password = input('Enter the Password: ')
    hashed_password = string_to_hash(password)


    if (auth(session,hashed_password)):
       print('Hi ' + username + '. You logged in successfully')
       main_menu(session)
    else:
        print('stronzo')
        sys.exit(1)




# Execute
if __name__ == "__main__":
        main()


