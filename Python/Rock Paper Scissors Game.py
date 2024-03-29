
import random
import time

#Stores Global Variables for the program to access
def score():
    global player_score
    global computer_score
    global computer_choice
    global rounds
    global weapon
    global rounds_tied
score()

#Variables set to 0, counter then adds 1 per round, wins, and ties
rounds = 0
computer_score = 0
player_score = 0
rounds_tied = 0

#List to store weapons chosen by the user and computer
opponent_history = []
computer_history = []

#Display prompt to play
name = input("Please enter your name: ")
print("Hello", name, "Let's Play Rock, Paper, Scissors")

#Program lags for 2 seconds before the next statement pops us
time.sleep(2)
#Rules of the game
print("\nThe objective of Rock, Paper, Scissors is to defeat your opponent by selecting a weapon that defeats their choice"
"\n1. Rock smashes Scissors, so Rock wins"
"\n2. Scissors cut Paper, so Scissors win"
"\n3. Paper covers Rock, so Paper wins"
"\n4. If players choose the same weapon, neither win and the game is played again")
time.sleep(5)
print("\n Your're allowed to choose a weapon from the following options:"
                   "\n  \n Rock(r) \n Paper(p) \n Scissors(s), \n Quit(q) \n ")


#Function to chose the computer's next weapon
def history(opponent_history):
    global computer_choice
    global most_common

    #if opponent history less than 5, computer will make a random choice using ranom import
    possible = ["r", "p", "s"]
    if len(opponent_history) < 5:
        computer_choice = random.choice(possible)
    else:
        #Using opponent history, the computer will chose the most frequent weapon entered by user and play the answer to win
        most_common = max(set(opponent_history), key=opponent_history.count)
        if (str(most_common) == 'r'):
            computer_choice = 'p'
        elif (str(most_common) == 'p'):
            computer_choice = 's'
        elif (str(most_common) == 's'):
            computer_choice = 'r'

def main():
    #The while loop, loops the program back when the user enter y for yes
    while True:
        continue_playing = input('Do you want to keep playing enter y for yes or q for quit: ').lower()

        global player_score
        global computer_score
        global computer_choice
        global rounds
        global weapon
        global rounds_tied
        global most_common

        #Will ask user to continue playing
        if (continue_playing == 'y'):

            #Add a round if user selects y
            rounds += 1
            print('Welcome to round', rounds)

            #User selects weapon( R, S, P ) and will add it to the opponent history
            weapon = str(input("Select your weapon: ")).lower()
            opponent_history.append(weapon)

            #Call history function
            history(opponent_history)

            #Nested loop to grab user and computer history 
            if ((weapon== 'r' and computer_choice == 's')) or ((weapon == 's' and computer_choice == 'p')) or ((weapon == 'p') and (computer_choice == 'r')):
                print('You selected:', weapon, 'Computer selected:', computer_choice, '\n You Win')
                #increase the player score
                player_score += 1

            elif ((weapon == 's' and computer_choice == 'r')) or ((weapon == 'p' and computer_choice == 's')) or ((weapon == 'r' and computer_choice == 'p')):
                print('You selected:', weapon, 'Computer selected:', computer_choice, '\n You Lose')
                #increases computer score
                computer_score += 1

            elif ((weapon == 'p' and computer_choice == 'p')) or ((weapon == 'r' and computer_choice == 'r')) or ((computer_choice == 's' and computer_choice == 's')):
                print('You selected:', weapon, 'Computer selected:', computer_choice, '\n You tied')
                #increases the tied score, no one won
                rounds_tied += 1
            else:
                print('Please enter an appropriate value.')
                main()
        #Will show stats for user and computer if the user quits game
        elif(continue_playing == 'q'):
            print(name, ', You selected to Quit:',
                  "\nYour Score", player_score,
                  "\nComputer Score", computer_score,
                  "\nRounds Tied", rounds_tied,
                  "\nRounds Played", rounds,
                  "\nUser history", opponent_history,
                  "\nComputer History", computer_history,
                  "\nUser choice most frequent weapon", most_common,
                  "\nComputer choice most frequent weapon", computer_history_common)
            exit()
        else:
            print('Please enter an appropriate value.')

        #Adds computer choices to computer history list
        computer_history.append(computer_choice)
        #Finds the most frequent weapon selected by the computer
        computer_history_common = max(set(computer_history), key=computer_history.count)



if __name__ == "__main__":
    main()
