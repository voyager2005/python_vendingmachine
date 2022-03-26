# C:\Users\aksha\PycharmProjects\Travelocity
"""
InstagroceryMain.py: Instagrocery.py is the main execution file for the Insta_grocery program which includes
                InstagroceryVendingMachine.py

__author__   = Akshat G
__credit__   = Yash
__license__  = MIT
__email__    = voyager2005@gmail.com
"""

from InstagroceryVendingMachine import *
from Subway import *

from colors import bcolors
import time

users_name = ""
users_phoneNumber = 0000000000

display_text1 = "Accessing system files"
display_text2 = "......"
display_text3 = "Starting Insta_Grocery"
display_text4 = "......"


def display_welcome():
    """displays the welcome message at the beginning of the program file"""
    # displaying welcome
    print('''
     *       *   * * * *   *         * * *    * * * *    *     *   * * * *
     *       *   *         *        *        *       *   * * * *   *       
     *   *   *   * * * *   *       *        *         *  *  *  *   * * * *  
     * *   * *   *         *        *        *       *   *     *   *      
     *       *   * * * *   * * * *   * * *    * * * *    *     *   * * * *  
    ''')


def user_information():
    """ user_information():

    Takes information from the user such as their name and their phone number
    The while loop is a fail-safe method to make sure that the phone number is 10 digits long and does not have special
        alphabets or special characters

    line60 - line69:
        The code between line 56 and line 65 is for printing the text with a certain delay to simulate the loading
        effect when using real life applications
    """
    global users_name
    global users_phoneNumber
    global display_text1
    global display_text2
    global display_text3
    global display_text4

    print(f"{bcolors.HEADER}WELCOME TO OUR INSTA-GROCERY WEBSITE{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}We would like to take your name and phone number "
          f"to verify with our accounts system{bcolors.ENDC}")
    users_name = input(f"Please enter your {bcolors.OKBLUE}name{bcolors.ENDC}\n")
    users_phoneNumber = input(f"Please enter your {bcolors.OKBLUE}Phone Number{bcolors.ENDC}\n")

    while True:
        if not users_phoneNumber.isdigit():
            users_phoneNumber = input(f"{bcolors.WARNING}Hey {users_name}! "
                                      f"Looks like your phone number has alphabets... "
                                      f"Please enter the correct value: {bcolors.ENDC}")
        else:
            break

    print(f"{bcolors.OKGREEN}Thank you for providing us with the requested information{bcolors.ENDC}\n\n")

    # creative display for Accessing system files and Starting Insta-Groceries
    time.sleep(0.5)
    print(display_text1, end='')
    for i in range(0, len(display_text2)):
        print(display_text2[i], end='')
        time.sleep(0.4)
    time.sleep(0.5)
    print("\n" + display_text3, end='')
    for i in range(0, len(display_text4)):
        print(display_text4[i], end='')
        time.sleep(0.4)

    print("", end="\n\n")

    # prompting and accepting users input for execution of either InstagroceryVendingMachine.py or Subway.py
    print(f"Do you want to use the {bcolors.OKBLUE}[1]Insta-Grocery Machine{bcolors.ENDC} or "
          f"{bcolors.OKBLUE}[2]SubWay{bcolors.ENDC} {bcolors.FAIL}[1] or [2]{bcolors.ENDC}")
    if input() == '1':
        # starting the vending machine for the user
        str1 = "Starting Vending Machine"
        for i in range(0, len(str1)):
            print(str1[i], end='')
            time.sleep(0.10)
        time.sleep(0.8)
        print("\n", end="\n\n")
        print(f"\t\t\t   WELCOME\n\t\t\t\t\t TO \n\t\t\t\t\t  INSTAGROCERY")
        users_vending_machine_choice()
    else:
        # starting the subway program for the user
        print("\n", end="\n\n")
        print(f"\t\t\t   WELCOME\n\t\t\t\t\t TO \n\t\t\t\t\t  SUBWAY")
        add_bread()


display_welcome()
user_information()
