import random

num = random.randint(1, 50)
tries = 10
win = False
guess_input = input("Enter a number between 1 and 50: ")


def new_random_number():
    global num
    num = random.randint(1, 50)


while tries >= 0 and win is False:
    try:
        int(guess_input)
    except ValueError:
        guess_input = input("Invalid number, choose a number between 1 and 50: ")
    else:
        if int(guess_input) > num:
            tries -= 1
            print(tries)
            guess_input = input("That number is too high: ")
        elif int(guess_input) < num:
            tries -= 1
            print(tries)
            guess_input = input("That number is too low: ")
        elif int(guess_input) == num:
            print("You got it!")
            win = True
            # retry()
    while win is True:
        try_again = input("Try again? (Y)es or (N)o: ")
        if try_again.upper() == 'Y' or try_again.upper() == 'N':
            if try_again.upper() == 'Y':
                tries = 11
                win = False
                new_random_number()
                guess_input = input("Enter a number between 1 and 50: ")
            elif try_again.upper() == 'N':
                print("Thanks for playing!")
                break
        else:
            try_again = input("Invalid response. Enter 'y' for yes or 'n' for no: ")



