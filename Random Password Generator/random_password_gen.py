#!/bin/python3

#!/bin/python3
import string
import random

print('''
Password Generator
==================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('number of passwords?')
number = int(number)

length = input('password length?')
length = int(length)

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
         
characterList = ""


while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
         
        # Adding letters to possible characters
        characterList += string.digits
    elif(choice == 2):
         
        # Adding digits to possible characters
        characterList += string.ascii_letters
    elif(choice == 3):
         
        # Adding special characters to possible
        # characters
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")

print('\nhere are your passwords:')



for pwd in range(number):
  password = []

  for c in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
  print("".join(password))