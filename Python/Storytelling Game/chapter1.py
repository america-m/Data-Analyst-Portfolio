
# Purpose: First chapter, welcomes user and asks him to select a weapon

import myglobalvars #imports global vars

def main(): #creates main function

    continue_chapter = True #while condition is true will continue chapter
    name = input("[CH1] Please enter your name: ") #asks user for name
    #gives intro to game
    print("[CH1] Hello {}, you accidentally fell down a hole and landed in another universe. You must figure out how to escape this universe".format(name))

    while continue_chapter: #while loop that will end current chapter if True or False
        #intro to chapter 1
        print("[CH1]Welcome to chapter 1. Your first task is to find a shelter to protect you from the weather")
        #asks user where to find shelter
        shelter = int(input("[CH1] Would you like to search for shelter in the choclate woods[1] or ice cream mountains[2]?[Enter 1 or 2] "))#asks user if they want to find shelter

    #based on users answer
        if shelter == 1:
            print("[CH1] Great, pick out some equipment for your journey!")
            mylist = ["Sword", "Axe", "Hammer", "Bat", "Knife"]  #creates list
            print(mylist) #prints list
            weapon = input("Enter your weapon of choice ")
            weapon = weapon.capitalize()# asks user for weapon
            if weapon in mylist:  # based on users option
                print("[CH1] Yes we have {} in inventory" .format(weapon)) #formats based on user choice
                print("[CH1] Proceed with chapter 2")
                #if user was successful in this chapter to go onto the next chapter
                myglobalvars.ch1_success = True
                #if user will restart this chapter
                continue_chapter = False
            else:
                print("[CH1] Sorry, not in inventory, try again")
                myglobalvars.ch1_success = False #does not goes back to main program
                continue_chapter = True #continues chapter
        elif shelter == 2:
            print("[CH1] Sorry you died a sweet death")
            myglobalvars.ch1_success = False #does not go back to main program
            continue_chapter = True#continues chapter
        else:
            print("[CH1] Please enter 1 or 2...")
            #shelter = int(input("enter your choice "))
            myglobalvars.ch1_success = False #does not go to next level
            continue_chapter = True #continues current chapter

if __name__ == "__main__": #calls main function
     main()


