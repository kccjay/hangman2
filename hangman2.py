import os
import random


def get_puzzle():
    path = "puzzle"

    names = os.listdir(path)

    starting()
    for i, f in enumerate(names):
        print(str(i + 1) + ": " + f)

    choice = input("Type one number: ")
    choice = int(choice)- 1
        
    print()
    file = path + "/" + names[choice]
    print(file)

    with open (file, 'r') as f:
        lines = f.read().splitlines()

    #category = lines[0]
    word = random.choice( lines[1:] )
    
    return word.lower()

def art_text():
    file = open('end_screen.txt', 'r')

    picture = file.read()
    print(picture)

    file.close()

def starting():
    file = open('splash.txt', 'r')

    image = file.read()
    print(image)

    file.close()

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    while True:
        letter = input("Guess a letter: ")
        if letter.isalpha() or letter == "_":
            return letter
        else:
            print()
            print("*Not a letter*")
            print()

def display_board(solved, guesses, body_parts):
    print(str(solved) + " (" + str(guesses) + ") " + "*" + str(body_parts) + "*")

def show_result(puzzle, guesses):
    
    if puzzle == guesses:
        print()
        print("Are you a robot??")
        print()
    else:
        print()
        print("Try harder come on!")
        print()
        art_text()
        print()
    
def play():
#splash screen somewhere
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    
    body_parts = 0
    human = 10
    
    display_board(solved, guesses, body_parts)

    while solved != puzzle and body_parts < human:
        letter = get_guess()
        guesses += str(letter)
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses, body_parts)

        body_parts += 1
        
    show_result(puzzle, guesses)

def play_again():
    while True:
        print()
        decision = input("Would you like to play again? (y/n) ")
        print()
        #case-insensitive for decision
        decision = decision.lower()

        if decision == 'y' or decision == 'yes' or decision == 'yepper':
            return True
        elif decision == 'n' or decision == 'no' or decision == 'nope':
            return False
        else:
            print()
            print("Please enter 'y' or 'n'!!!")
            print()

            
playing = True

while playing:
    play()
    playing = play_again()

