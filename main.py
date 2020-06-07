#!/usr/bin/env python3

import sys
import yaml


SETTINGS = '/Users/dorje/Projects/Sindria/dorjecurreli/aubergina/settings.yml'
DATABASE = '/Users/dorje/Projects/Sindria/dorjecurreli/aubergina/db.yml'

def auth(data,x):
    password = data['config']['key']


    if (password == x):
        return True
    else:
        return False

def load(file):

    with open(file, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def save(file,data):
    with open(file, 'w') as f:
        yaml.dump(data,f)
        return True

def add_credential(i,credentials):

    name = input('Insert a name: ')
    username = input('Insert your username: ')
    psw = input('Insert your Password: ')
    url = input('Insert the URL  of your service: ')
    note = input('Insert optional note: ')

    credential = {
        'id': i,
        'name': name,
        'username': username,
        'password': psw,
        'url': url,
        'note': note,
    }


    credentials[i] = credential
    i += 1

    return credentials

def store_credential():

    i = 0
    credentials = dict()
    credentials = add_credential(i,credentials)
    i += 1

    while True:
        choice = input('Do you want to add a new credential? (y/n) ')
        if (choice == 'y'):
            credentials = add_credential(i,credentials)
            i += 1

        if (choice == 'n'):
            break


    save(DATABASE,credentials)

def main():

     # Inizio autenticazione.
     x = input('Welcome in aubergina password manager \n please enter your password: \n ')

     data = load(SETTINGS)

     if (not auth(data, x)):
        print('Credenziali Errate')
        return sys.exit(1)

     # Fine autenticazione.

     # Inizio opzioni utente.

     option = input('Choose a option:\n\na) add credential\nb) exit ')
     if (option == 'a'):
         store_credential()

     if (option == 'b'):
         return sys.exit(0)


     # Fine opzioni utente.








# Execute
if __name__ == "__main__":
        main()


