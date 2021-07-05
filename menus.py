import os
import user
import functions

user_list = user.users_list

def clear_screen():
    os.system('cls')

def display_user_menu(user):
    clear_screen()
    print (f"{user['first_name']} {user['last_name']}, Welcome to your Bank Account! Your access is granted...\n")
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
        functions.withdrawal_money()
        #input("Return to continue...")
        display_user_menu(user)
        
    elif(option == "3"):
        print("You selected Option 3!\n")
        functions.lodge_money()
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
        answer=str(input("Invalid Entry..Do you want to try again? [Y/N]"))
        answer=answer.upper()
        if (answer=="Y"):
            display_user_menu(user)
        else:
            print("Thank you...See you soon...")
            exit()
    
        
#display_user_menu(user)    


def display_help_menu():
    clear_screen()
    print("=========================")
    print("*** HELP MENU OPTIONS ***")
    print("=========================\n")
    print("1. Change Pin number HELP.")
    print("2. Withdraw money HELP.")
    print("3. Lodge Money HELP.")
    print("4. View Statement HELP.")
    print("5. Exit Menu.")

#display_help_menu()