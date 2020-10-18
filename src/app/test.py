#!/usr/bin/env python3
import hashlib



#change_fruits = input('Neu fruit name: ')


#fruit = {
#    0: {
#        "banana": 1.00,
#        "apple": 1.53,
#        "kiwi": 2.00,
#        "avocado": 3.23,
#        "mango": 2.33,
#        "pineapple": 1.44,
#        "strawberries": 1.95,
#        "melon": 2.34,
#        "grapes": 0.98
#    },
#    1: {
#        "banana": 1.00,
#        "apple": 1.53,
#        "kiwi": 2.00,
#        "avocado": 3.23,
#        "mango": 2.33,
#        "pineapple": 1.44,
#        "strawberries": 1.95,
#        "melon": 2.34,
#        "grapes": 0.7
#    }
#}


#for k,v in fruit.items():
#    fruit[1]['banana'] = change_fruits
#    print(fruit)





str = hashlib.sha256(b'hash this text')
text_hashed = str.hexdigest()
print(text_hashed)


var = input('Input string: ').encode('utf-8')
hashed_var = hashlib.sha256(var).hexdigest()
print(hashed_var)