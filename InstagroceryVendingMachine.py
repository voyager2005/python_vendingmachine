# C:\Users\aksha\PycharmProjects\Travelocity
"""
InstagroceryVendingMachine.py: >>> add description here

__author__   = Akshat G
__credit__   = Yash
__license__  = MIT
__email__    = voyager2005@gmail.com"""

import sys
from colors import bcolors

# declaring global variables
display_bill = False
total_items = 0
termination = "no"
items_in_cart = 0  # variable to keep a count of the number of items in the users cart
users_vending_choice = 0  # variable to store the choice of main category
users_cart = ["nothing here"] * 100
users_cart_category = [0] * 100  # list to hold the category from which the user has picked up items
users_cart_choice = [0] * 100  # list to hold the choice of the user from that category
users_cart_quantity = ["nothing here"] * 100
users_cart_cost = [0] * 100

# declaring global variables for all the vending machine items
name_veggies = ["Onion", "Tomato", "Coriander", "Lemon", "potato", "cabbage"]
cost_veggies = [47, 100, 10, 20, 33, 26]
quantity_veggies = ["1kg", "500g", "1pc.", "250g", "1kg", "1kg"]

# noinspection SpellCheckingInspection
name_dairy = ["Nandini Good life toned milk", "Milky Mist Curd", "Amul Butter Pasteurized", "ID Natural Paneer",
              "Amul Cheese Slices", "Amul Masti Buttermilk"]
cost_dairy = [56, 40, 50, 105, 155, 95]
quantity_dairy = ["1L", "500g", "500g", "200g", "200g", "2L"]

# noinspection SpellCheckingInspection
name_beverage = ["REAL Fruit Juice Guava", "Paper Boat Lychee Ras", "Sprite Soft Drink", "Thumbs Up Soft Drink",
                 "Hershey’s Milk Shake Cookies&Cream", "Bisleri Mineral Water"]
cost_beverage = [100, 20, 40, 45, 35, 27]
quantity_beverage = ["1L", "2150ml", "750ml", "750ml", "200ml", "2L"]

# noinspection SpellCheckingInspection
name_readyToCook = ["MasterChef Chicken Fries", "MasterChef French Fries", "MasterChef Desi Chicken Patty",
                    "MasterChef Vada Pops", "MasterChef Chicken Seekh", "MasterChef Chicken Burger Patty"]
cost_readyToCook = [136, 80, 136, 130, 260, 175]
quantity_readyToCook = ["280g", "500g", "330g", "310g", "260g", "300g"]

# noinspection SpellCheckingInspection
name_snacks = ["Bingo Tedhe Medhe Cocktail mix", "Sunfeast All Rounder", "Sunfeast Trinity Cake",
               "Bingo Mad Angles Achari Masti", "Tasties All in One mix",
               "Lays Potato Chips American Style Cream & Onion Flavour"]
cost_snacks = [50, 25, 10, 40, 49, 76]
quantity_snacks = ["160g", "75g", "27g", "130g", "150g", "190g"]


def users_vending_machine_choice():

    """users_vending_machine_choice():

    defining a function users_vending_machine_choice() is for displaying all the different categories of shopping
    options i.e. veggies, dairy, beverages, ready to cook and snacks

    further on values that the user picks is added to a list called user_cart_category for later user

    based on the category that the user chooses a function is called ie display_veggies, display_dairy,
    display_beverages, display_readyToCook and display_snacks"""

    global users_vending_choice
    global items_in_cart

    print(f"\n\n"
          f"{bcolors.OKGREEN}\t\t\t\t[1]    VEGGIES{bcolors.ENDC}\n"
          f"{bcolors.OKBLUE}\t\t\t\t[2]     DIARY{bcolors.ENDC}\n"
          f"{bcolors.OKCYAN}\t\t\t\t[3]   BEVERAGES{bcolors.ENDC}\n"
          f"{bcolors.FAIL}\t\t\t\t[4] READY TO COOK{bcolors.ENDC}\n"
          f"{bcolors.WARNING}\t\t\t\t[5]    SNACKS{bcolors.ENDC}")
    users_vending_choice = input()
    users_cart_category[items_in_cart] = int(users_vending_choice)

    if int(users_vending_choice) == 1:
        displaying_veggies()
    elif int(users_vending_choice) == 2:
        displaying_dairy()
    elif int(users_vending_choice) == 3:
        displaying_beverages()
    elif int(users_vending_choice) == 4:
        displaying_ready_to_cook()
    elif int(users_vending_choice) == 5:
        displaying_snacks()
    else:
        print("invalid choice")
        users_vending_machine_choice()


def displaying_veggies():
    """This function displays all the items in the category of [veggies]"""
    global name_veggies
    global cost_veggies
    global quantity_veggies
    global users_cart_category

    # displaying Veggies
    for i in range(0, len(name_veggies)):
        print(f"{i+1}.{bcolors.OKBLUE}{quantity_veggies[i]}{bcolors.ENDC}"
              f" {bcolors.OKCYAN}{name_veggies[i]}{bcolors.ENDC}"
              f" ₹{bcolors.OKGREEN}{cost_veggies[i]}{bcolors.ENDC}", end="\t")
        if (i + 1) % 3 == 0:
            print(end="\n")
    users_shopping_cart()


def displaying_dairy():
    """This function displays all the items in the category [dairy]"""
    global name_dairy
    global cost_dairy
    global quantity_dairy
    global users_cart_category

    # displaying Dairy
    for i in range(0, len(name_dairy)):
        print(f"{i+1}.{bcolors.OKBLUE}{quantity_dairy[i]}{bcolors.ENDC}"
              f" {bcolors.OKCYAN}{name_dairy[i]}{bcolors.ENDC}"
              f" ₹{bcolors.OKGREEN}{cost_dairy[i]}{bcolors.ENDC}", end="\t")
        if (i + 1) % 3 == 0:
            print(end="\n")
    users_shopping_cart()


def displaying_beverages():
    """This function displays all the items in the category of [beverages]"""
    global name_beverage
    global cost_beverage
    global quantity_beverage
    global users_cart_category

    # displaying Beverages
    for i in range(0, len(name_beverage)):
        print(f"{i+1}.{bcolors.OKBLUE}{quantity_beverage[i]}{bcolors.ENDC}"
              f" {bcolors.OKCYAN}{name_beverage[i]}{bcolors.ENDC}"
              f" ₹{bcolors.OKGREEN}{cost_beverage[i]}{bcolors.ENDC}", end="\t")
        if (i + 1) % 3 == 0:
            print(end="\n")
        users_shopping_cart()


def displaying_ready_to_cook():
    """This function displays all the items in the category [ready to cook]"""
    global name_readyToCook
    global cost_readyToCook
    global quantity_readyToCook
    global users_cart_category

    # displaying Ready To Cook Items
    for i in range(0, len(name_readyToCook)):
        print(f"{i+1}.{bcolors.OKBLUE}{quantity_readyToCook[i]}{bcolors.ENDC}"
              f" {bcolors.OKCYAN}{name_readyToCook[i]}{bcolors.ENDC}"
              f" ₹{bcolors.OKGREEN}{cost_readyToCook[i]}{bcolors.ENDC}", end="\t")
        if (i + 1) % 3 == 0:
            print(end="\n")
    users_shopping_cart()


def displaying_snacks():
    """This function displays all the items in the category [snacks]"""
    global name_snacks
    global cost_snacks
    global quantity_snacks
    global users_cart_category

    # displaying Snacks
    for i in range(0, len(name_snacks)):
        print(f"{i+1}.{bcolors.OKBLUE}{quantity_snacks[i]}{bcolors.ENDC}"
              f" {bcolors.OKCYAN}{name_snacks[i]}{bcolors.ENDC}"
              f" ₹{bcolors.OKGREEN}{cost_snacks[i]}{bcolors.ENDC}", end="\t")
        if (i + 1) % 3 == 0:
            print(end="\n")
    users_shopping_cart()


def users_shopping_cart():
    """users_shopping_cart():

    line 168 to line 182 *
        line x to line y is used to add the item selected by the user into the shopping cart
        separate variables are used to add flexibility to the program and to not make it dependent on only a
        certain number of items in the list... any changes made to the original list of items in a certain category
        will be implemented into different parts of a program without causing any issues

    line 189 to line 192 *
        line z to line z2 is used to ask the user if he wants to continue the program or terminate it.
         on deciding to terminate the program the final shopping cart and the bill is displayed. If the user wants to
         continue shopping then he is taken to the beginning of the program where he can continue to shop
    """
    global display_bill
    global items_in_cart
    global users_cart_choice
    global users_cart_cost
    global users_cart_category
    global users_cart_quantity
    global users_cart
    global termination

    print("Choice: ")
    users_cart_choice[items_in_cart] = input()
    if int(users_cart_category[items_in_cart]) == 1:
        users_cart_quantity[items_in_cart] = quantity_veggies[int(users_cart_choice[items_in_cart]) - 1]
        users_cart[items_in_cart] = name_veggies[int(users_cart_choice[items_in_cart]) - 1]
        users_cart_cost[items_in_cart] = cost_veggies[int(users_cart_choice[items_in_cart]) - 1]
    elif int(users_cart_category[items_in_cart]) == 2:
        users_cart_quantity[items_in_cart] = quantity_dairy[int(users_cart_choice[items_in_cart]) - 1]
        users_cart[items_in_cart] = name_dairy[int(users_cart_choice[items_in_cart]) - 1]
        users_cart_cost[items_in_cart] = cost_dairy[int(users_cart_choice[items_in_cart]) - 1]
    elif int(users_cart_category[items_in_cart]) == 3:
        users_cart_quantity[items_in_cart] = quantity_beverage[int(users_cart_choice[items_in_cart]) - 1]
        users_cart[items_in_cart] = name_beverage[int(users_cart_choice[items_in_cart]) - 1]
        users_cart_cost[items_in_cart] = cost_beverage[int(users_cart_choice[items_in_cart]) - 1]
    elif int(users_cart_category[items_in_cart]) == 4:
        users_cart_quantity[items_in_cart] = quantity_readyToCook[int(users_cart_choice[items_in_cart]) - 1]
        users_cart[items_in_cart] = name_readyToCook[int(users_cart_choice[items_in_cart]) - 1]
        users_cart_cost[items_in_cart] = cost_readyToCook[int(users_cart_choice[items_in_cart]) - 1]
    elif int(users_cart_category[items_in_cart]) == 5:
        users_cart_quantity[items_in_cart] = quantity_snacks[int(users_cart_choice[items_in_cart]) - 1]
        users_cart[items_in_cart] = name_snacks[int(users_cart_choice[items_in_cart]) - 1]
        users_cart_cost[items_in_cart] = cost_snacks[int(users_cart_choice[items_in_cart]) - 1]

    items_in_cart = items_in_cart + 1

    print(f"{bcolors.BOLD}Do you want to continue shopping (yes/no): {bcolors.ENDC}")
    if input() == "no":
        display_bill = True
        display_shopping_cart()
    else:
        print(f"{bcolors.BOLD}Do you want to view or alter your shopping cart? "
              f"(yes/no) {bcolors.ENDC}")
        choice = input()
        if choice == "yes":
            print(f"\nTo view your shopping cart press {bcolors.FAIL}[1]{bcolors.ENDC}\n"
                  f"To remove items from your shopping cart press {bcolors.FAIL}[2]{bcolors.ENDC}")
            choice = input()
            if choice == "1":
                display_shopping_cart()
            elif choice == "2":
                alter_shopping_cart()
            else:
                users_vending_machine_choice()
        else:
            users_vending_machine_choice()


def display_shopping_cart():
    global display_bill
    global users_cart
    global users_cart_quantity
    global users_cart_cost

    print(f"{bcolors.HEADER}\t\t\t\t\tSHOPPING CART{bcolors.ENDC} ")
    for i in range(0, items_in_cart):
        print(f"{i+1}. "
              f"{bcolors.OKCYAN}Quantity{bcolors.ENDC}: {users_cart_quantity[i]}\t"
              f"{bcolors.OKBLUE}Item Name{bcolors.ENDC}: {users_cart[i]}\t"
              f"{bcolors.OKGREEN}Cost of Item{bcolors.ENDC}: {users_cart_cost[i]}")

    if display_bill:
        display_users_bill()

    users_vending_machine_choice()


def alter_shopping_cart():
    """alter_shopping_cart():

    This function first displays the cart and then prompts the user to enter number so that an item in that position
    in the cart can be removed

    This is done by taking the value of i and removing the elements in that location

    Later all the elements that were in succession of that position will be brought down by 1 slot to create the new
        cart and the user can later choose to continue shopping, remove more elements or checkout"""
    global users_cart
    global users_cart_cost
    global users_cart_category
    global users_cart_quantity
    global users_cart_choice
    global items_in_cart

    while True:
        # displaying users cart
        for i in range(0, items_in_cart):
            print(f"{i + 1}. "
                  f"{bcolors.OKCYAN}Quantity{bcolors.ENDC}: {users_cart_quantity[i]}\t"
                  f"{bcolors.OKBLUE}Item Name{bcolors.ENDC}: {users_cart[i]}\t"
                  f"{bcolors.OKGREEN}Cost of Item{bcolors.ENDC}: {users_cart_cost[i]}")

        # prompting a user to enter the Serial Number of the element to be removed
        item_to_be_removed = input("Please enter the serial number of the item to be removed from the cart: ")
        print(f"{bcolors.WARNING}{users_cart[int(item_to_be_removed)-1]} has been removed from your cart{bcolors.ENDC}")
        item_to_be_removed = int(item_to_be_removed)
        index_of_element_to_be_removed = item_to_be_removed - 1

        # removing the element in index item_to_be_removed
        users_cart[index_of_element_to_be_removed] = "nothing here"
        users_cart_quantity[index_of_element_to_be_removed] = "nothing here"
        users_cart_choice[index_of_element_to_be_removed] = 0
        users_cart_cost[index_of_element_to_be_removed] = 0
        users_cart_category[index_of_element_to_be_removed] = 0

        # checking if the removed element was the last element
        if item_to_be_removed == items_in_cart:
            print(f"\n{bcolors.OKBLUE}        WHAT WOULD YOU LIKE TO DO NEXT     {bcolors.ENDC} \n"
                  f"1. Remove another item from the cart\n"
                  f"2. Continue Shopping\n"
                  f"3. Checkout\n")
            choice = input()

            if int(choice) == 1:
                alter_shopping_cart()
            elif int(choice) == 2:
                users_vending_machine_choice()
            elif int(choice) == 3:
                display_users_bill()
            break
            # the last element had been removed from the list

        # re-arranging the elements in the list
        for i in range(index_of_element_to_be_removed, items_in_cart):
            users_cart[i] = users_cart[i+1]
            users_cart_category[i] = users_cart_category[i+1]
            users_cart_choice[i] = users_cart_choice[i+1]
            users_cart_cost[i] = users_cart_cost[i+1]
            users_cart_quantity[i] = users_cart_quantity[i + 1]

        items_in_cart = items_in_cart - 1

        # prompting the user for the next course of action
        print(f"\n{bcolors.OKBLUE}        WHAT WOULD YOU LIKE TO DO NEXT     {bcolors.ENDC} \n"
              f"1. Remove another item from the cart\n"
              f"2. Continue Shopping\n"
              f"3. Checkout\n")
        choice = input()
        choice = int(choice)
        if choice == 1:
            alter_shopping_cart()
        elif choice == 2:
            users_vending_machine_choice()
        elif choice == 3:
            display_users_bill()


def display_users_bill():
    """display_users_bill():

    This function is used to display the users shopping cart.

    The option to view the shopping cart has not been added for this program, but it can be achieved by adding code
        between lines 214 and 219 in a different function and this function can be called when the user types
        -h (--help): Helps the users with a certain short-key manual
        -l (--list): Displays teh users shopping cart in between each input statement
    """
    global total_items
    global items_in_cart
    global users_cart
    global users_cart_cost
    global users_cart_quantity

    print(f"{bcolors.BOLD}Thank you for shopping with us today! {bcolors.ENDC}\n")

    # calculating the cost of all the items the user has added to his cart
    sum_cart = sum(users_cart_cost)
    print(f"Bill Amount: ₹{bcolors.OKBLUE}{sum_cart}{bcolors.ENDC}")
    print(f"Bill Amount: ₹{bcolors.OKBLUE}{sum_cart * 118/100}{bcolors.ENDC} (inc. GST)")

    sys.exit(0)
