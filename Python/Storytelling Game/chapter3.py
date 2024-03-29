# Author: America Munoz
# Date 12/13/2022
# Version 1.0
# Final Project
# Purpose: Third chapter, asks user to make a selection from the options provided

import time
import myglobalvars

def main():
    continue_chapter = True #if true will continue this chapter
    print("[CH3] Welcome to chapter 3")
    time.sleep(2) #pause before next line
    print("[CH3] It looks like you've come across a lake, you must cross it to move to chapter 4")
    #list of options for user
    print("[CH3] 1. Try to go around the lake")
    print("[CH3] 2. Build a raft to get across")
    print("[CH3] 3. Swim across lake")
    while continue_chapter: #while loop to continue current chapter
        choice = int(input("[CH3] Please chose an option from the list above[#1-3] ")) #user must select which option

        if choice == 1:
            print( "[CH3] You selected to go around the lake, oh no theres a pack of wolves")#back to chapter 1
            continue_chapter = True #continues current chapter
        elif choice == 2:
            print("[CH3] You selected to build the raft and have successfully crossed the lake") #successfully go to chapter 4
            myglobalvars.ch3_success = True #goes on to next chapter
            continue_chapter = False #stops current chapter
        elif choice == 3:
            print("[CH3] You selected to swim across the lake, but accidentally drowned") #back to chose options
            continue_chapter = True #continues current chapter
        else:
            print("[CH3] Invalid")
            myglobalvars.ch3_success = False #does not go on to next chapter
            continue_chapter = True #continues current chapter

if __name__ == "__main__":
    main()