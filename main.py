#!/usr/bin/env python3

import sys
import yaml


CONFIG = '/Users/dorje/Projects/Sindria/dorjecurreli/aubergina/settings.yml'

def auth(config,x):
    password = config['config']['key']


    if (password == x):
        print('You logged in')
    else:
        print('Try again')

def main():

     x = input('Welcome in aubergina password manager \n please enter your password: \n ')

     with open(CONFIG, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

     auth(config,x)

# Execute
if __name__ == "__main__":
        main()


