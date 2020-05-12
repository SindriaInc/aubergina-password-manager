#!/usr/bin/env python3

import sys
import yaml


x = input('Welcome Dorje, plese enter your password:  ')

config_path = '/Users/dorje/Projects/Sindria/dorjecurreli/aubergina/config.yaml'

with open(config_path, 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

def auth():
    password = config['config']['key']
    if(password == x):
        print('You logged in')
    else:
        print('Try again')
auth() 


def main():
    if __name__ == "__main__":
        main()
