
# Purpose: Fifth chapter, gives user a riddle to unlock the door

import myglobalvars #imports global variables
import time #imports time module


def main(): #creates main fucntion

    continue_chapter = True #will continue current chapter if true
    print("[CH5] Welcome to chapter 5, the final chapter")
    time.sleep(2) #creates space between lines
    print("[CH5] To unlock the door, you must solve this riddle")
    time.sleep(2)
    print("[CH5] I turn once, what is out will not get in. I turn again, what is in will not get out.") #prints riddle
    time.sleep(3)
    while continue_chapter: #while loop to continue chapter
        word = input("[CH5] What am I? ") #asks user for input

        #if statement based on user response
        if word == 'key':
            print("[CH5] A bright light flashed out the door, whats happening..")
            myglobalvars.ch5_success = True #will go to next chapter
            continue_chapter = False #will stop current chapter
        elif word == 'A key':
            print("[CH5] A bright light flashed out the door, whats happening..")
            myglobalvars.ch5_success = True #will continue to next chapter
            continue_chapter = False #will stop current chapter
        elif word == "I don't know":
            hint = input("[CH5] Would you like a hint?[Enter yes or no]") #asks user if they want a hint
            continue_chapter = True #will continue chapter
            #if statement based on users input for a hint
            if hint == 'yes':
                print("[CH5]I can fit inside your pocket")
            elif hint == 'no':
                print("[CH5]Try again")
                continue_chapter = True #will continue chapter
            else:
                print("[CH5] Invalid, please enter yes or no")
                continue_chapter = True #will continue chapter
        elif word == 'door':
            print("[CH5] Getting warmer, try again")
            continue_chapter = True #will continue chapter
        elif word == 'A door':
            print("[CH5] Getting warmer, try again")
            continue_chapter = True #will continue chapter
        else:
            print("[CH5]Sorry try again")
            continue_chapter = True #will continue chapter

    if __name__ == "__main__": #calls main function
        main()