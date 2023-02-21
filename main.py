'''
Guessing Game
'''

import random
import time

attempt_list = []

def show_score():
    if not attempt_list:
        print("Score table is empty")
    else:
        print(f"The current high score is {min(attempt_list)} attempts")

def start_game():
    attempts = 0 
    random_number = random.randint(1,20)
    print("Let's start guess game !")
    time.sleep(1)
    player_name = input("What is your name ? ")
    time.sleep(1)
    wanna_play = input(f"Good morning {player_name} would you like to play ? '(Enter Yes or No)' ")

    if wanna_play.lower() != 'yes':
        print("Thanks, Bye !")
        exit()
    else:
        show_score()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input("Pick a number beetwen 1 and 20 "))
            if guess < 1 or guess > 20:
                raise ValueError("Please guess a number within the given range")

            attempts += 1
            attempt_list.append(attempts)

            if guess == random_number:
                print("Nice ! You got it")
                print(f"It took you {attempts} attempts ! ")
                wanna_play = input(f"{player_name} would you like to play again ? '(Enter Yes or No)' ")
                if wanna_play.lower() != 'yes':
                    print("Cool, take a brake")
                    break
                else:
                    attempts = 0
                    random_number = random.randint(1,20)
                    show_score()
                    continue
            else:
                if guess >random_number:
                    print("It's too high !")
                elif guess < random_number:
                    print("It's too low !")
            
        except ValueError as error:
            print("It's not a valid number")
            print(error)

if __name__ == '__main__':
    start_game()