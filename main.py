#########################################################
# Name: Charlie Cardenas                                #
# Program: Lab 06 - Contact List                        #
# Description: Modified version of Lab 03; This program #
# will read contact lists from files or create a new    #
# one if one does not exist.                            #
#########################################################

import json
from contacts import Contacts

# Default initialization
filename = 'default.dat'
curr_contacts = Contacts(filename = filename)
menu_choice = 1

# Menu
while menu_choice != 6:
    print(" "*5, end=" *** ")
    print("TUFFY TITAN CONTACT MAIN MENU")
    print()
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Set contact filename")
    print("6. Exit the program")
    print()

    menu_choice = int(input("Enter menu choice: "))
    print()

    # Select correct function
    match menu_choice:
        case 1:
            p_n = input("Enter phone number: ")
            f_n = input("Enter first name: ")
            l_n = input("Enter last name: ")

            # See if added or not
            status = curr_contacts.add_contact(id=p_n, first_name=f_n, last_name=l_n)
            if status == "error":
                print("Phone number already exists.")
            else:
                print("Added:", status)
        case 2:
            p_n = input("Enter phone number: ")
            f_n = input("Enter first name: ")
            l_n = input("Enter last name: ")

            # See if modified or not
            status = curr_contacts.modify_contact(id=p_n, first_name=f_n, last_name=l_n)
            if status == "error":
                print("Phone number does not exist.")
            else:
                print("Modified:", status)
        case 3:
            p_n = input("Enter phone number: ")

            # See if deleted or not
            status = curr_contacts.delete_contact(id=p_n)
            if status == "error":
                print("Phone number does not exist.")
            else:
                print("Deleted:", status)

        case 4:
            curr_contacts.print_list()
        case 5:
            filename = input("Enter filename: ")
            curr_contacts = Contacts(filename = filename)
        case 6:
            print("Exiting program...")
        case _:
            print("Invalid menu choice. Try again.")


    print()
