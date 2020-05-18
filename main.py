#!/usr/bin/env python3

import sys
import yaml

# Costante percorso file di configurazione
CONFIG = '/Users/dorje/Projects/Sindria/dorjecurreli/aubergina/config.yaml'


# Funzione per l'utenticazione dell'utente
def auth(config):
    password = config['config']['key']
    
    if (password == x):
        print('You logged in')
    else:
        print('Try again')


# Main - funzinone princile dove eseguo le mie istruzioni e dove richiamo le altre funzioni
def main():
    x = input('Welcome in aubergina password manager \n please enter your password: \n ')
    
    with open(CONFIG, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    auth(config)


# Execute - esecuzione del programma
if __name__ == "__main__":
        main()
