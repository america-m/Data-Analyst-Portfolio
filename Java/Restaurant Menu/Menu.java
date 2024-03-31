import java.util.InputMismatchException;
import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.

public class Menu {
    private static String[][] updatedMenu;

    public static String[][] option2(String[][] menu){
        Scanner input = new Scanner(System.in); //defining input
        System.out.println("Current Menu ");
        for (int i = 0; i < menu.length; i++) { //prints current array
            System.out.println((i + 0) + ": " + menu[i][0] + " - $" + menu[i][1]);
        }

        System.out.println("Enter new item: "); //asks user for input
        String newItem = input.next();
        System.out.println("Enter new price: "); //asks user for input
        String newPrice = input.next();

        String[][] updatedMenu = new String[menu.length + 1][2]; //new array is created with one more space

        for (int i = 0; i < menu.length; i++) {
            updatedMenu[i][0] = menu[i][0]; // transfers menu items to new array
            updatedMenu[i][1] = menu[i][1];// transfers prices to new array
        }
        updatedMenu[menu.length][0] = newItem; // takes new item
        updatedMenu[menu.length][1] = newPrice; //takes new price

        System.out.println("Updated Menu: ");
        for (int i = 0; i < updatedMenu.length; i++) { //prints new array
            System.out.println((i + 1) + ": " + updatedMenu[i][0] + " - $" + updatedMenu[i][1]);
        }
        return updatedMenu;
    }
    public static String[][] option3(String[][] menu) {
        Scanner input = new Scanner(System.in); //defining input
        System.out.println("Enter item to delete");
        for (int i = 0; i < menu.length; i++) { //prints current array
            System.out.println((i + 1) + ": " + menu[i][0] + " - $" + menu[i][1]);
        }

        System.out.println("Enter item number to delete:"); //asks user for input

        int delete = input.nextInt();

        if (delete >= 1 && delete <= menu.length) { //ensures user input is between 1-9
            String[][] updatedMenu = new String[menu.length - 1][2]; //empty array is created shorter than original array
            for (int i = 0, j = 0; i < menu.length; i++) {
                if (i != delete - 1) { //ensures item user entered is deleted
                    updatedMenu[j++][0] = menu[i][0]; //transfers array to updatedmenu

                }
            }


            System.out.println("Successfully Deleted, Updated Menu:"); //prints updated menu
            for (int i = 0; i < updatedMenu.length; i++) {
                System.out.println((i + 1) + ": " + updatedMenu[i][0] + " - $" + menu[i][1]);
                
            }
        }
        return updatedMenu;
        //else {
          //  System.out.println("Invalid Entry"); //if another number is entered
       // }
        
    }
    public static void main(String[] args) {

        //assign variable type
        int action;
        int items;


        Scanner input = new Scanner(System.in); //defining input

        System.out.println(""" 
                Welcome to Lola's Restaurant! \s
                Take a look at our menu items. \s"""); //asks user for action

        MenuItem starter1 = new MenuItem();
        starter1.setMenuItem("Fried Pickles $", 7, " - Crispy Breading with Ranch Dressing");
        MenuItem starter2 = new MenuItem();
        starter2.setMenuItem("Wings $", 7, " - Spicy Chicken Wings with Celery");
        MenuItem entree1 = new MenuItem();
        entree1.setMenuItem("Burger and Fries $", 8, " - Large Burger with Hanful of Fries");
        MenuItem entree2 = new MenuItem();
        entree2.setMenuItem("Steak with Potatoes $", 8, " - Savory Steak with Roasted Potatoes");
        MenuItem drink1 = new MenuItem();
        drink1.setMenuItem("Soda $", 5, " - Icy Soda Refreshement ");

starter1.display();
starter2.display();
entree1.display();
entree2.display();
drink1.display();

        System.out.println("""
                      
        Please select an action.\s
        To Calculate a Total Enter 1\s
        To Add an Item Enter 2 \s
        To Delete an Item from the Menu enter 3\s
        To Change the Price of an Item Enter 4\s""");
        action = input.nextInt(); // takes user input


        int[] array = new int[20];
        String[][] menu = {
                {"Fried Pickles ", "7"},
              //  {"Nuggets ", "7"},
                {"Wings ", " 7"},
                {"Burger and Fries ", "10"},
                {"Steak with Potatoes ", "10"},
               // {"Pasta Alfredo ", "10"},
               // {"Water ", "5"},
                {"Soda ", "5"},
              //  {"Lemonade ", "5"}
        };
        // String[] array2 = {"Fried Pickles $7", "Nuggets $7", "Wings $7", "Burger and Fries $10", "Steak with Potatoes $10", "Pasta Alfredo $10", "Water $5", "Soda $5", "Lemonade $5"};
        // int[] food = {7, 10, 5};

        int starter = 7;
        int main = 10;
        int drinks = 5;


        if (action == 1) { //if statement based on action
            int count = 0;

            System.out.println("\nItems offered include: " +
                    "\nPlease select from the list of items offered when done enter 99 >>");
            
            for (int x = 0; x < menu.length; x++) {
                System.out.println((x + 0) + ": " + menu[x][0] + " - $" + menu[x][1]);
            }
                items = input.nextInt(); //if action 1 is selected, further input is collected from user

            //will change user input into item price based on variable
            if (items == 0 || items == 1 )
                items = starter;
            else if (items == 2 || items == 3 )
                items = main;
            else
                items = drinks;
            array[0] = items; //adds first user input to array
            count++; //from first input counts up

            while (items < 99) { //based on input from user, they are entered into a while loop. Programs stops when 99 is entered
                System.out.println("Would you like to enter another item? To quit enter 99 >>");
                items = input.nextInt(); //items accepted based on user selection
                //will change user input into item price based on variable
                if (items != 99) { //if user input is not 99, items will continue to be added to array
                    if (items == 0 || items == 1 )
                        items = starter;
                    else if (items == 2 || items == 3 )
                        items = main;
                    else
                        items = drinks;
                    array[count] = items; //adds user input to array
                    count++; //proceeds to add user input
                }

            }
            //calculates sum of items
            int sum = 0;
            for (int i = 0; i < count; i++) {
                sum += array[i];
            }
            System.out.println("Thank you for visiting Lola's your total is: $" + sum); //prints total sum **/

        } else if (action == 2) { // based on user input action

            option2(menu);

        } else if (action == 3) { // based on user input action
            //System.out.println("Select what item to delete: ");
            option3(menu);

        } else if (action == 4) { // based on user input action

           for (int x = 0; x < menu.length; x++) { //prints menu
                System.out.println((x + 0) + ": " + menu[x][0] + " - $" + menu[x][1]);
            }
            //asks user for item
            System.out.println("Select the item you would like to change the price of: ");
           try
           {
               int update = input.nextInt();


            //ensures item is between 0 and 9
            if (update >= 0 && update <= menu.length) {
                System.out.println("You selected " + update + "\nPlease enter the updated price: ");
                String update1 = input.next();

                int updatedPrice = Integer.parseInt(update1);

                menu[update][1] = String.valueOf(updatedPrice);
            }
            //prints updated menu
            System.out.println("Updated Menu: ");
            for (int x = 0; x < menu.length; x++) {
                System.out.println((x + 1) + ": " + menu[x][0] + " - $" + menu[x][1]);
            }

        } //else {
           catch (InputMismatchException e) { //catches exception for input mismatch
               System.out.println("There was a problem with your entry. Type a valid number." ); //prints out message for user after exception 
           }
            //System.out.println("Invalid Entry."); }
        }
    }
}