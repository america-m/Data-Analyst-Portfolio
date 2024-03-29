
# Purpose: Fourth chapter, makes user select an option from the list provided to escape
import myglobalvars #imports global variables
import time #imports time

def main(): #creates main function
    continue_chapter = True #if true will continue chapter
    #explains to user what is happening
    print("[CH4] Welcome to chapter 4")
    print("[CH4] It looks like there is a castle in a distance")
    print("[CH4] Let's enter it...")
    time.sleep(2)
    print("[CH4] Oh no, you're locked in, find the exit door")
    #list of options below
    print("[CH4] 1. Search for exit upstairs")
    print("[CH4] 2. Search for exit in North wing")
    print("[CH4] 3. Search for exit in South wing")
    print("CH4] 4. Search for exit downstairs")
    while continue_chapter: #while loop to continue chapter
        choice = int(input("Please chose an option from the list above[#1-4] ")) #asks user to input from a choice above
        #based on user choice
        if choice == 1:
            print( "[CH4] You selected to search upstairs, oh no you had a run in with a large snake, try again")
            continue_chapter = True #will continue chapter
        elif choice == 2:
            print("[CH4] You selected to to search the North wing and found a golden door, now you have to unlock it")
            continue_chapter = False #will continue chapter
            myglobalvars.ch4_success = True #goes to next chapter
        elif choice == 3:
            print("[CH4] You selected to search the South wing and ran into an evil wizard")
            continue_chapter = True#will continue chapter
        elif choice == 4:
            print("[CH4] You selected to search downstairs and fell down another hole!")
            continue_chapter = True #will continue current chapter
        else:
            print("[CH4] Invalid, try again")
            continue_chapter = True #will continue current chapter

    if __name__ == "__main__": #calls main function
        main()