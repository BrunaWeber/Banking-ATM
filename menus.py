import os
import user
import functions

user_list = user.users_list

def clear_screen():
    os.system('cls')

def display_user_menu(user):
    #clear_screen()
    print("=========================")
    print("*** USER MENU OPTIONS ***")
    print("=========================\n")
    print("1. Change Pin number.")
    print("2. Withdraw money.")
    print("3. Lodge Money.")
    print("4. View Statement.")
    print("5. Onscreen Help Menu.")
    print("6. Exit Menu.")

    option=input("Please choose an option (1-6): ")

    clear_screen()
    if(option == "1"):
        print("You are on Option 1!\n")
        functions.change_pin()
        display_user_menu(user)

    elif(option == "2"):
        print("You selected Option 2!\n")
        #function.withdrawal_money()
        #input("Return to continue...")
        display_user_menu(user)
        
    elif(option == "3"):
        print("You selected Option 3!\n")
        #function.lodge_money()
        input("Return to continue...")
        display_user_menu(user)
            
    elif(option == "4"):
        print("You selected Option 4!\n")
        #functions.view_statement()
        input("Return to continue...")
        display_user_menu(user)

    elif(option == "5"):    
        print("You selected Option 5!\n")
        display_help_menu()
        input("Return to continue...")
        display_user_menu(user)
    
    elif(option == "6"):
        print("Thank you and Bye!")

    else:
        print("Please return to menu and select an option from 1 to 6...")
        input("Return to continue...")
        display_user_menu(user)

        
#display_user_menu(user)    


def display_help_menu():
    print("=========================")
    print("*** HELP MENU OPTIONS ***")
    print("=========================\n")
    print("1. Change Pin number HELP.")
    print("2. Withdraw money HELP.")
    print("3. Lodge Money HELP.")
    print("4. View Statement HELP.")
    print("5. Exit Menu.")

