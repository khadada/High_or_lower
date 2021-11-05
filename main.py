# TODO: 01
# import the modules that we need for this project
# ------------------------------------------------
import game_data
import art
from functions import *
# TODO: 02
# print the logo of the game
# ------------------------------------------------
# TODO: 03
# create global variables
# ------------------------------------------------

def game():
    score = 0
    possib_answer = ["a", "b"]
    task_in_level = 2
    while task_in_level > score:
        computer_selects = cpu_choices(game_data.data)
        print(computer_selects) # to delete later
        print_compare(computer_selects,"a")
        print(art.vs)
        print_compare(computer_selects,"b")
        correct_answer = answer_checker(computer_selects).lower()
        print(f"The correct answer is : {correct_answer}") # to delete later
        is_correct_value = False
        while not is_correct_value:
            user_answer = input('Who has more followers? type [a] or [b]:  ').lower()
            if user_answer in possib_answer:
                if user_answer == correct_answer: # is correct answer
                    print('Correct answer ')
                    score += 1
                    if score >= task_in_level:
                        if restart():
                            game()

                else:                             # is incorrect answer
                    if score > 1:
                        print(f"Your score in the game is: {score}")
                    else:
                        print("You didn't get any score in our game")
                is_correct_value = True
            else:
                print('Invalid answer check your answer a or b ')
# game start
game()