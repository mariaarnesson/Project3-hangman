import random
def main_menu():
    print("WELCOME TO BATTELSHIP GAME \n")
    
print("________________________________________________________")
print("            Hello and Welcome to Battelship game")
print("________________________________________________________")

print("\n")
print("             /||                                        ")
print("            / ||_\                                      ")
print("           /  ||__\                                     ")
print("          /   ||___\                                    ")
print("         /    ||____\                                   ")
print("        /     ||_____\                                  ")
print("       /      ||______\                                 ")
print("      /       ||_______\                                ")
print("     /        ||        \                               ")
print("   _/_________||_________\________                      ")
print("   \_____________________________/                      ")
print("    \___________________________/                       ")
print("     \_________________________/                      \n")
print("                                                      \n")
print("                                ____||__  _____||__     ")
print("                       ____||_ )________( )_________(   ")
print("                      )_______( ____||__  _____||__     ")
print("                       ____||_ )________( )_________(   ")
print("                      )_______()________( )_________(   ")
print("                       ____||_  ____||__  _____||__     ")
print("                      )_______()________( )_________(   ")
print("                           ||  )________( )_________(   ")
print("                         __||______||__________||_____  ")
print("                         \ // ///  /////   /////  // /  ")
print("                          \                         /   ")
print("                           \_______________________/    ")
print("                        /                                    ")
print("                       / |                                   ")
print("                      /  |\                                  ") 
print("             _______ /  /| \                                 ")
print("            /______//  / |  \                                 ")
print("           /______//  /  |   /\\                              ")
print("                  /  /   | //  \ \                             ")
print("                 /  /    ///    \  \                           ")
print("                /  /   ////      \  \                           ")
print("               /  /  /////        |  \                          ")
print("              /  / /////|         |\  \                         ")
print("             /  //////// |       /  \ |                          ")
print("            /  //_____/  |      /    \                           ")
print("           /  /  _______ |_____/    /                            ")
print("       ___/__/___| |__\ |_____/__  /                              ") 
print("       \_____\____________________/                              ")
print("        \_____\__________________/                               ")
print("          \____\_______________/                                  \n")
print("                                                                  \n")

input("Press Enter to continue")
main_menu()


print("    ____________________________________")
print("    ____________________________________")      
print("                   BATTLESHIP           ")
print("    ____________________________________")
print("    ____________________________________\n")


from itertools import zip_longest

number = ['   ','  1','  2','  3']
boats = ['SHIP NAME','  Carrier','  Battleship','  Destroyer']
scale = ['    SIZE','     |5|','  |4|','   |2|']


for number,boats, scale,  in zip_longest(number,boats,scale):
    
    print('______________________________')
    print(number, boats, scale)
    print('______________________________')
    
    
LENGTH_OF_SHIPS = [5,4,2] 
board = [
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
]

# We want to refer to columns by letter, but Python accesses lists by number. So we define
# a dictionary to translate letters to the corresponding number. Note that Python lists start in
# zero, not in one!
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
}


# By writing this as a function, we don't have to repeat it later. It's less code, it makes
# the rest easier to read, and if we improve this, we have to do it only once!
def ask_user_for_board_position():
    column = input("column (A to F):")
    while column not in "ABCDEF":
        print("That column is wrong! It should be A, B, C, D, E or F")
        column = input("column (A to E):")

    row = input("row (1 to 7):")
    while row not in "1234567":
        print("That row is wrong! it should be 1, 2, 3, 4, 5, 6, 7")
        row = input("row (1 to 7):")

    # The code calling this function will receive the values listed in the return statement below
    # and it can assign it to variables
    return int(row) - 1, letters_to_numbers[column]


def print_board(board):
    # Show the board, one row at a time
    print("__ A_ B_ C_ D_ E_ F_")
    
    row_number = 1
    for row in board:
        print("%d%s" % (row_number, "|_".join(row)))
        
        row_number = row_number + 1


# We want 5 battleships, so we use a for loop to ask for a ship 5 times!
for n in range(5):
    print("Where do you want ship ", n + 1, "?")
    row_number, column_number = ask_user_for_board_position()

    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("That spot already has a battleship in it!")

    board[row_number][column_number] = 'X'
    print_board(board)


# Now clear the screen, and the other player starts guessing
print("\n"*50)

guesses_board = [
   ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
    ['|_','|_','|_','|_','|_','|_'],
]


# Keep playing until we have 5 right guesses
guesses = 0
while guesses < 5:
    print("Guess a battleship location")
    row_number, column_number = ask_user_for_board_position()

    if guesses_board[row_number][column_number] != ' ':
        print("You have already guessed that place!")
        continue

    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("HIT!")
        guesses_board[row_number][column_number] = 'X'
        guesses = guesses + 1
    else:
        guesses_board[row_number][column_number] = '.'
        print("MISS!")

    print_board(guesses_board)
print("GAME OVER!")
print('              _______________________ ')
print('              |      GAME OVER!      |')   
print('              | Thank you for plaing |')
print('              _______________________\n  ')
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
               