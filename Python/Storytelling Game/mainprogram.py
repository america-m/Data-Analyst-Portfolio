
# Purpose: Main program, runs all chapters

#imports chapters 1-5 & global vars
import chapter1
import chapter2
import chapter3
import chapter4
import chapter5
import myglobalvars


def main(): #main function

    myglobalvars.gvars() # print(myglobalvars.ch1_success)
    continue_playing = True #will continue playing if true

    while continue_playing:
        answer = input("[Main] Would you like to continue playing? ") #asks user if they want to play
        if answer.lower() == "no": #if user answers no
            continue_playing = False #stops game if user enters no
            print("Goodbye")
        else:
            print("Great, welcome to the game")
            chapter1.main()
            if myglobalvars.ch1_success: #if chapter is successful, it goes to next chapter
                chapter2.main()
                if myglobalvars.ch2_success:  #if chapter is successful, it goes to next chapter
                    chapter3.main()
                    if myglobalvars.ch3_success:  #if chapter is successful, it goes to next chapter
                        chapter4.main()
                        if myglobalvars.ch4_success:  #if chapter is successful, it goes to next chapter
                            chapter5.main()
                            if myglobalvars.ch5_success:  #if chapter is successful, it goes to next chapter
                                print("It looks like you're back to the real world!!!!") #prints statement for chapter 5
                            else:
                                print("Sorry chapter 5 did not work out!!!") #prints statement for chapter 5
                        else:
                            print("Sorry chapter 4 did not work out!!!") #prints statement for chapter 4
                    else:
                        print("Sorry chapter 3 did not work out!!!") #prints statement for chapter 3
                else:
                    print("Sorry chapter 2 did not work out!!!") #prints statement for chapter 2
            else:
                print("Sorry chapter 1 did not work out!!!") #prints statement for chapter 1


if __name__ == "__main__": #completes main function
    main()
