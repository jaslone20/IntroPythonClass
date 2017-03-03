#!/usr/bin/env python3

""" 
This script creates a dictionary of names and user names. A menu is presented to the user
with options for adding items, removing items, and so on. 

Each menu item is attached to a function that performs the requested operation.
"""

# Import SortedDict class
from sortedcontainers import SortedDict

# Function to print the user input menu
def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a User')
    print('5. Quit')
    print()

# Create dictionary with key = Name, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# Initialize counter to store menu choice
menu_choice = 0

# Call function to display input menu
print_menu()

# As long as the menu choice isn't "quit" get user options
while menu_choice < 5:
    # Get menu choice from user
    menu_choice = int(input("Type in a number (1-5): "))
    
    # View current entries
    if menu_choice == 1:
        print("Current Users:")
        for key,value in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(key,value))
            
    # Add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = str.capitalize(username)

    # Remove an entry
    elif menu_choice == 3:
        # what do I do here?
        print("Remove User")
        # get name of user to delete 
        input_name = input("Name: ")
        #check if input name in dict
        if input_name in usernames:
            del usernames[input_name]

    # Find a user name      
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name or username: ")
        for key, value in usernames.items():
            if (name == key):
                print(usernames[name])
            if (name == value):
                print([item[0] for item in usernames.items() if item[1] == name])
        else:
            print("User not found.")

    # Find a user name      
    elif menu_choice >= 6:
        try:
            break
        except IOError:
            print("Your menu choice is not valid")

    # If user enters something strange, show them the menu
    else:
        print_menu()