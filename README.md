# Data-Analyst-Portfolio

## About

Hello welcome! I am an aspring Data Analyst who loves to tell stories with data. I am an avid learner excited to progress in my career and gain more experience. Feel free to explore my portfolio and view my growth as a Data Analyst! :) 

### Titanic Logistic Regression Model 
[Titanic Dataset Iterative Imputation for Missing Values
](https://github.com/america-m/Data-Analyst-Portfolio/blob/89845e828f7226398ab6035815dcd6f043a704e0/Python/Titanic%20Dataset%20Iterative%20Imputation%20for%20Missing%20Values.ipynb)

**Language:** Python 
**Skills:** Pandas, Scikit-learn, Seaborn, NumPy, Matplotlib

On April 15, 1912, the infamous Titanic Ocean liner on a voyage to New York City struck an iceberg and sank in the middle of the North Atlantic Ocean. There were an estimated 2,200 passengers and crew on board; about 1,500 people died. The ship was only equipped with 20 lifeboats despite the capacity of 48. The impact of the Titanic shipwreck is still felt worldwide. The Titanic spurred major changes to maritime safety regulations along with inspiring many stories and movies to remember the catastrophic event in 1912 and to honor all the lives lost that night.

The purpose of this project was to build a Logistic Regression Model that would predict if a passenger survived the Titanic shipwreck. The datasets consist of record data separated by files: train, test, and gender submission. This includes data on the passengers such as name, sex, age, fare, port of embarkation, siblings on board, number of parents/children on board, cabin, ticket number, and if the passenger survived. The project first involved data preprocessing as there was an extensive amount of missing data for passengers under the 'Age' column, to combat this a multivariate approach was taken. Using Scikit-learn multivariate imputer, a Linear Regression algorithm was applied that would use the entire set of available features to estimate a missing value. After the data was imputed using the iterative imputation method or fill-in approach with the mean, a Logistic Regression algorithm was then used to predict if a passenger survived the Titanic shipwreck

### Bakery Sales March 2020

[Bakery Sales March 2020
](https://github.com/america-m/Data-Analyst-Portfolio/tree/79e224396d9db6c6b0cc7d029b6c076091346ead/Excel)

**Application:** Excel **Skills:** XLOOKUP, IF Function, MAXIFS, SUMIFS, SUM Function, Conditional Formatting 

This project features sales data from a Bakery collected in 2020. Excel is a powerful tool with many features that are incredibly useful for data analysis. My purpose for this project was to practice using these Excel tools to fully analyze a dataset. I chose a relatively small dataset to ensure I would effectively view the analysis results. The first step before analyzing the data was making all values consistent. Some rows contained duplicate data, therefore I made sure to remove the unnecessary data to maintain the integrity of the dataset. I proceeded to use a variety of functions Excel provides. To feature the use of the IF function, I created an additional table that would use the "Quantity" sold for each bakery item and set it to a limit example: IF Quantity < 25 = "Below Sales Goal". This function created a column that would indicate if a sales item was below or above the required criteria - 25. This would be useful if a company wanted to flag down specific days where they did not meet the goals intended for that day. The SUM function is one of the more commonly used functions in Excel and it became very useful for this dataset when calculating the total sold for each bakery item and total revenue. 

The MAXIF function was used to find the highest quantity sold for an item, this function takes in criteria and based on the criteria finds the MAX. In this case, it took the "Cupcake" and the "Quantity" columns to find the highest quantity sold for cupcakes. Additionally, I wanted to view the days the highest quantity was purchased. To do this I applied the XLOOKUP function which would search for the MAX value for each bakery item and find the date purchased. Although this process could have been done by looking only at this small dataset, this function is very useful and should be easily applied to large datasets. To showcase the use of the SUMIFS function, I applied this function to find the total quantity and revenue for each day. Finally, after creating tables and calculating different results I plotted the data to easily showcase the results. 

### Restaurant Menu Management System 

[Restaurant Menu](https://github.com/america-m/Data-Analyst-Portfolio/tree/79fd81e02c92a244b07c7cf41c777186457beb1a/Java/Restaurant%20Menu)

**Language:** Java 
**Skills:** Application of methods, 2D Array's, Inhertiance, Exception Catching 

This Restaurant menu program explores the use of basic Java techniques and methods to create a versatile menu. It provides a simple and effective interface for managing a Restaurant's menu, allowing for easy addition, deletion, and modification of menu items. The program initially displays Lola's Restaurant's menu, including various items and their prices. Users are prompted to select an action: Calculate a total (1), Add an item to the menu (2), Delete an item from the menu (3), Change the price of an item (4). Calculate Total (Action 1): Users can select items from the menu, and the program calculates the total price based on the selected items. Add Item (Action 2): Users can add a new item to the menu by providing the name and price. Delete Item (Action 3): Users can delete an existing item from the menu by selecting its index. Change Price (Action 4): Users can update the price of an existing item by selecting its index and providing the new price. The program validates user input to ensure it falls within appropriate ranges and formats and uses mismatch expetion for inavlid inputs. 


### Storytelling Game
[Storytelling Game
](https://github.com/america-m/Data-Analyst-Portfolio/tree/b0bb964275e0501dcd4b73dfe0dfcd66f376acfc/Python/Storytelling%20Game)

**Language:** Python 
**Skills:** Sequential Execution, Error Handling, Random Library, Time Library, Functions, Global Variables, Looping

The purpose of this program is to practice applying commonly used Python tools and explore the use of global variables across different files. This storytelling game runs through several chapters where the player must complete challenges to win the game. The game begins with a player falling down a hole into an alternate universe. In Chapter 1 of the game, the player must select a weapon based on given choices, once the user selects their weapon, they initialize the second chapter by calling the main function and meeting conditions outlined in the chapter and global variables. In Chapter 2 the player encounters their first challenge which is a game of rock, paper, scissors. With the use of the random library, the computer can play against the user, and only after winning the game, is the main function called and pushed to Chapter 3, if the player fails they are sent back to Chapter 1 declaring the while loop in the main function as False. 
Chapters 3 and 4 are focused on receiving input from the user based on a logical question, the user must choose how to proceed to win the game, and if the user selects the correct answer they proceed to Chapter 5, using an if statement the user has several options to make which will initialize the main function and either send the user back a chapter or to the final chapter. Chapter 5 consists of a riddle the user must solve, the player will have several turns in this chapter to guess the riddle with the use of a while loop. The user will be given a hint and based on the user's answer will be provided with an indication of how close they are to solving the riddle with words such as "getting warmer". Once the player guesses the riddle, they have won and the game ends. 

### Fortune Teller 
[Fortune Teller 
](https://github.com/america-m/Data-Analyst-Portfolio/blob/d8b216a62c7a026cb53b64b1b693c8658cfd3265/Python/Fortune%20Teller.py) 

**Language:** Python 
**Skills:** Random Library, Shuffle Method, For Loops, Lists 

This project was a fun way to practice commonly used Python techniques while at the same time, bringing back the nostalgic charm of the childhood paper fortune-telling game. Inspired by the classic origami game, it offers a dynamic twist using Python's versatility.

Here's how it works: the game unfolds with the user's selection of one out of four colors presented. Subsequently, the virtual paper is shuffled, mirroring the chosen color's letter count. Then, another color is chosen, and the paper undergoes a second shuffle based on the total letter count of both colors combined. Finally, the user picks a number, which unveils their fortune.

Unlike the traditional paper game, where the fortunes are permanently attached to numbers, Python allows us to assign fortunes dynamically. Each time the user makes a choice, the fortunes are shuffled accordingly, ensuring a fresh experience every time. Even if the user chooses the same number repeatedly, the fortune will always be different, adapting to the user's previous choices made. As the position of the fortune is always changing.  In essence, this Python fortune teller version adds a playful touch to the game, making it feel like your destiny is truly in the hands of code. 


### Rock Paper Scissors Game 
[Rock Paper Scissors Game
](https://github.com/america-m/Data-Analyst-Portfolio/blob/aa0683031de9bdab6d6b364f64d4390c3bbe58b8/Python/Rock%20Paper%20Scissors%20Game.py)

**Language:** Python 
**Skills:** Random Library, Time Library, Functions, Global Variables, Counter, Looping 

This Python game was crafted as a practical exercise to hone my Python skills while at the same time offering an engaging gameplay experience. It's based on the classic intransitive hand game commonly played between two individuals. Just like its real-life counterpart: Rock triumphs over Scissors, Scissors defeat Paper, and Paper outwits Rock, this version adheres to the same rules. 
In each round, both the computer and the player make random selections for the first five turns. Subsequently, the computer analyzes these initial choices and identifies the most frequently selected option by the player. Armed with this insight, it strategically decides its subsequent moves to maximize competitiveness, ensuring an engaging experience for the player.

After each round, the player is prompted to decide whether to continue playing or exit the game. If they opt to continue, the game seamlessly loops back to the beginning, ready for another round. Upon choosing to exit the game, a comprehensive summary is displayed, showcasing total rounds played, victories achieved by both the computer and the player, tied rounds, and a detailed history of player and computer choices throughout the game. This version of the game provides an intellectual and intriguing challenge for the player. 






