import random

#INPUT NAME
name = input('Enter your name ')

#INPUT FIRST PICK
colors = ['red', 'pink', 'blue', 'orange']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
print(colors)
first_pick = input('Pick a color: ')
first_pick = first_pick.lower()
print('.....')


#RANDOMIZE BASED ON FIRST PICK LENGTH

for i in range(len(first_pick)):
    random.shuffle(numbers)

#INPUT SECOND PICK
print(colors)
second_pick = input('Pick another color: ')
print('.....')

#RANDOMIZE BASED ON SECOND PICK LENGTH

for i in range(len(second_pick)):
    shuffled_list = sorted(numbers, key=lambda x: random.random())

#SELECT A NUMBER
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers1)
number_selection = input('Now pick a number ')
number_selection = number_selection.lower()

#BASED ON COLOR SWITCH STATEMENT TO PREDICT FORTUNE

if number_selection == shuffled_list[0]:
    print(name, 'You will finish all your homework early this week')
elif number_selection == shuffled_list[1]:
    print(name, 'You need to visit Career Bridge')
elif number_selection == shuffled_list[3]:
    print(name, 'You are destined to be a Software Developer')
elif number_selection == shuffled_list[2]:
    print(name, 'You will be the 56th president of the United States')
elif number_selection == shuffled_list[4]:
    print(name, 'You will land your dream job soon :)')
elif number_selection == shuffled_list[5]:
    print(name, 'You will get an important phone call tomorrow at 9:03am')
elif number_selection == shuffled_list[6]:
    print(name, "You're destined to be a Data Analyst")
elif number_selection == shuffled_list[7]:
    print(name, "You will get all A's this quarter")
else:
    print("Enter Valid Number!!")
