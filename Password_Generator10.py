#!/usr/bin/env python3

#  Why importin tons of functions when I can import the only 2 I need?

from sys import exit
from random import choice

#
# Using try - except trap to verify if input data is a number
# if no exit with errcode -9
#

try:
    password_length=int(input('\nDigit the lentgh of password to generate: '))
except:
    print("\nA number whas required!!\n")
    exit(-9)

#
# using a static string avoids loading unnecessary libraries at this point (like import string)
#
#password_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
password_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|#$%&*+-.@'

print("")
for k in range(10):
    password = []

    for x in range(password_length):
        password.append(choice(password_characters))
#
# using the f-string is more python in printing in version 3
#
    print(f"{''.join(password)} ")
print("")
