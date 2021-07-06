import os
import user
import functions

user_list = user.users_list

#transactions_list = user.transactions_list

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

    option=input("\nPlease choose an option (1-6): ")

    clear_screen()
    if(option == "1"):
        print("You are on Option 1!\n")
        functions.change_pin(user)
        input("Return to continue...")
        display_user_menu(user)

    elif(option == "2"):
        print("You selected Option 2!\n")
        functions.withdrawal_money(user)
        input("Return to continue...")
        display_user_menu(user)
        
    elif(option == "3"):
        print("You selected Option 3!\n")
        functions.lodge_money(user)
        input("Return to continue...")
        display_user_menu(user)
            
    elif(option == "4"):
        print("You selected Option 4!\n")
        functions.view_statement(user)
        #functions.view_last_transactions()
        #functions.display_balance(user) # just use it to test...
        input("Return to continue...")
        display_user_menu(user)

    elif(option == "5"):    
        print("You selected Option 5!\n")
        display_help_menu(user)
        input("Return to continue...")
        display_user_menu(user)
    
    elif(option == "6"):
        print(f"Thank you {user['first_name']}, and Bye!")
    
    else:
        answer=str(input("Invalid Entry..Do you want to try again? [Y/N]"))
        answer=answer.upper()
        if (answer=="Y"):
            display_user_menu(user)
        else:
            print(f"Thank you {user['first_name']}...See you soon...")
            exit()
    
#display_user_menu(user)    

def display_help_menu(user):
    clear_screen()
    print("=========================")
    print("*** HELP MENU OPTIONS ***")
    print("=========================\n")
    print("1. Change Pin number HELP.")
    print("2. Withdraw money HELP.")
    print("3. Lodge Money HELP.")
    print("4. View Statement HELP.")
    print("5. Exit Menu.")

    option=input("\nPlease choose an option (1-6): ")
    clear_screen()

    if(option == "1"):
        print("You are on Option 1!\n")
        print("You are logged in... To change your pin enter '1'. The APP will request that you enter a Pin (4 digits) and repeat the same (4 digits). Make sure to reenter the same 4 digits in the second time.")
        input("Return to continue...")
        display_help_menu(user)

    elif(option == "2"):
        print("You selected Option 2!\n")
        print("You are logged in... To withdraw money enter '2'. Now enter the value of the amount that you would like to withdraw. Just remember that you need to have at least this amount in your account. Enter a number.")
        input("Return to continue...")
        display_help_menu(user)
        
    elif(option == "3"):
        print("You selected Option 3!\n")
        print("You are logged in... To lodge money enter '3'. Now enter the value that you would like to deposit in your account. Enter a number.")
        input("Return to continue...")
        display_help_menu(user)
            
    elif(option == "4"):
        print("You selected Option 4!\n")
        print("You are logged in... To check your statement enter '4'. Here will be displayed your information: First Name, User ID, Current Balance, Overdraft Facilit (FALSE--> you do not have overdraft money.) (TRUE --> you have overdraft money.)")
        input("Return to continue...")
        display_help_menu(user)

    elif(option == "5"):
        print(f"Thank you {user['first_name']}, and Bye!")
    
    else:
        answer=str(input("Invalid Entry..Do you want to try again? [Y/N]"))
        answer=answer.upper()
        if (answer=="Y"):
            display_help_menu(user)
        else:
            print(f"Thank you {user['first_name']}...See you soon...")
            exit()


#display_help_menu()