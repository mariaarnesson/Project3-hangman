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

  
    while trials > 0:
        failed = 0   

       for letter in word_to_guess:
        if letter in guessing:
            main_word = main_word + letter
        else:
            main_word = main_word + '_'

        if main_word == word:
            print(main_word)
            print('congratulations! You won!')
            break   

            print('try to guess the word' main_word)
            guess = input()

        if guess in inscription:
            guessing = guessing + guess
        else:
            print('enter valid character')
            guess = input()

    
          if guess not in word:
            trials = trials -1
            if trials == 10
               print('Yoy have 10 chances left')
               print('                      ((  (( ))  ))              ')
            if trials == 9
               print('Yoy have 10 chances left')
               print('                      ((  (( ))  ))              ')
               print('                    (((( ( (    )) ))       ')
            if trials == 8
               print('Yoy have 10 chances left')
               print('                      ((  (( ))  ))              ')
               print('                    (((( ( (    )) ))       ')
               print('                  ((/   ( (     ))|) ))     ') 
            if trials == 7
               print('Yoy have 10 chances left')
               print('                      ((  (( ))  ))              ')
               print('                    (((( ( (    )) ))       ')
               print('                  ((/   ( (     ))|) ))     ')
               print('                 (( | _  \/  _  \/| )) ))    ')
            if trials == 6
               print('Yoy have 10 chances left') 
               print('                      ((  (( ))  ))              ')
               print('                    (((( ( (    )) ))       ')
               print('                  ((/   ( (     ))|) ))     ')
               print('                 (( | _  \/  _  \/| )) ))    ')
               print('                ))  | 0      0    |  ))((    ') 
            if trials == 5
               print('Yoy have 10 chances left')
               print('                      ((  (( ))  ))              ')
               print('                    (((( ( (    )) ))       ')
               print('                  ((/   ( (     ))|) ))     ')
               print('                 (( | _  \/  _  \/| )) ))    ')
               print('                ))  | 0      0    |  ))((    ')
               print('                ))) )     _      / (((( ))    ')
            if trials == 4
               print('Yoy have 10 chances left') 
               print('                      ((  (( ))  ))              ')
               print('                    (((( ( (    )) ))       ')
               print('                  ((/   ( (     ))|) ))     ')
               print('                 (( | _  \/  _  \/| )) ))    ')
               print('                ))  | 0      0    |  ))((    ')
               print('                ))) )     _      / (((( ))    ')
               print('               ((  ( (    __    /((((((((     ')
            if trials == 3
               print('Yoy have 10 chances left')
               print('                      ((  (( ))  ))              ')
               print('                    (((( ( (    )) ))       ')
               print('                  ((/   ( (     ))|) ))     ')
               print('                 (( | _  \/  _  \/| )) ))    ')
               print('                ))  | 0      0    |  ))((    ')
               print('                ))) )     _      / (((( ))    ')
               print('               ((  ( (    __    /((((((((     ')
               print('                (( ) )  \ ___ / )) ))((\/     ') 
            if trials == 2
               print('Yoy have 10 chances left')
               print('                      ((  (( ))  ))              ')
               print('                    (((( ( (    )) ))       ')
               print('                  ((/   ( (     ))|) ))     ')
               print('                 (( | _  \/  _  \/| )) ))    ')
               print('                ))  | 0      0    |  ))((    ')
               print('                ))) )     _      / (((( ))    ')
               print('               ((  ( (    __    /((((((((     ')
               print('                (( ) )  \ ___ / )) ))((\/     ')
               print('                \/ \/ ( ( |  |  )) \/((       ')
            if trials == 1
               print('Yoy have 10 chances left')
               print('                      ((  (( ))  ))              ')
               print('                    (((( ( (    )) ))       ')
               print('                  ((/   ( (     ))|) ))     ')
               print('                 (( | _  \/  _  \/| )) ))    ')
               print('                ))  | 0      0    |  ))((    ')
               print('                ))) )     _      / (((( ))    ')
               print('               ((  ( (    __    /((((((((     ')
               print('                (( ) )  \ ___ / )) ))((\/     ')
               print('                \/ \/ ( ( |  |  )) \/((       ')
               print('                       \/ |  |      \/    ') 
               break 

hangman()            





