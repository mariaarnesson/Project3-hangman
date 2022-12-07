# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def menu():
    print('WELCOME TO HANGMAN GAME \n')

print('________________________________________________________')
print('         Hello and welcome to Hangman Game')
print('_________________________________________________________')
input('Press Enter to continue') 

menu()   

print(' _______________')
print('|   Hangman     | ')
print(' _______________')

def hangman():
    word_to_guess = ['attraction']
    trials = 10
    guessing = ''
    inscription = set('abcdefghijklmnopqrstuvwxyz')

    while len(word) > 0
       main_word = ' '

       for letter in word:
        if letter in guessing:
            main_word = main_word + letter
        else:
            main_word = main_word + '_'

        if main_word == word:
            print(main_word)
            print('congratulations! You won!')
                    




