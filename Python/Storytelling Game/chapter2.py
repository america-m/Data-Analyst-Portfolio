
# Purpose: Second chapter, challenges user to a rock paper scissors game.

import time
import random
import myglobalvars


def main():
    print("[CH2] Welcome to chapter 2 ")
    # myglobalvars.ch2_success = True
    # return

    continue_chapter = True
    time.sleep(2)
    while continue_chapter:
        fight = input("Oh no! There's a gremlin, to defeat it, you must play rock, paper, scissors. Do you want to play [Yes or No]? ")

        if fight.casefold() == 'yes':
            print("[CH2]Let's begin")
            user = input("Enter: rock, paper, scissors ")  # user must select an option
            user = user.casefold()  # asks user for weapon
            possible = ["rock", "paper", "scissors"]
            computer = random.choice(possible)  # computer selects random choice

            print(f"\nYou chose {user}, computer chose {computer}.\n")  # prints the user and computer choice

            # shows if user wins against computer based on choice
            if user == computer:
                print(f"[CH2]Both players selected {user}. It's a tie! Let's try again")
                myglobalvars.ch2_success = False # does not go back to main program
            elif user == "rock":
                if computer == "scissors":
                    print("[CH2]Rock smashes scissors!! You win, go to chapter 3")
                    myglobalvars.ch2_success = True #goes back to main program
                    continue_chapter = False #stops current chapter
                else:
                    print("[CH2]Paper covers rock. You lose, try again.")
                    continue_chapter = True #continues current chapter
            elif user == "paper":
                if computer == "rock":
                    print("[CH2] Paper covers rock!! You win, go to chapter 3!")
                    myglobalvars.ch2_success = True # goes back to main program
                    continue_chapter = False #stops current chapter
                else:
                    print("[CH2] Scissors cuts paper. You lose, try again.")
                    continue_chapter = True #continues current chapter
            elif user == "scissors":
                if computer == "paper":
                    print("[CH2] Scissors cuts paper! You win, go to chapter 3")
                    myglobalvars.ch2_success = True #goes back to main program
                    continue_chapter = False # stops current chapter
            else:
                    print("[CH2] Inavlid, try again")
                    continue_chapter = True #continues chapter
        elif fight.casefold() == 'no':
            print("[CH2] OK thanks for tyring....")
            continue_chapter = False #stops current chapter
            myglobalvars.ch2_success = False #goes back to main program but ends game

    if __name__ == "__main__":
        main()