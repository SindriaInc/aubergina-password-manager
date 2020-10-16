#!/usr/bin/env python3

change_fruits = input('Neu fruit name: ')


fruit = {
    0: {
        "banana": 1.00,
        "apple": 1.53,
        "kiwi": 2.00,
        "avocado": 3.23,
        "mango": 2.33,
        "pineapple": 1.44,
        "strawberries": 1.95,
        "melon": 2.34,
        "grapes": 0.98
    },
    1: {
        "banana": 1.00,
        "apple": 1.53,
        "kiwi": 2.00,
        "avocado": 3.23,
        "mango": 2.33,
        "pineapple": 1.44,
        "strawberries": 1.95,
        "melon": 2.34,
        "grapes": 0.7
    }
}


for k,v in fruit.items():
    fruit[1]['banana'] = change_fruits
    print(fruit)