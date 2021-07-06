import os
import user
import menus 

#transactions_list = user.transactions_list 
users_list = user.users_list
current_user = ""

def clear_screen():
    os.system('cls')
  
def user_login():
    print("\nLOGIN ONSCREEN HELP --> The information that is requested for you are:\nUSER ID: 4 digits --> This information you received when you open your account.\nPIN: 4 digits --> You have created it on the day that you open your account, you might change it on the APP.\n")
    print("If you have any problems while on the application, please contact Paramount Programming Customer Service Assistance.\nOur phone is: (88)250-2123 \nEmail: customerhelp@paramountpro.com\n\n")
    print("===================")
    print("*** USER LOGIN ***")
    print("===================\n")
    
    username=input("Please enter your User ID:  ")
    
    found_user=False

    for user in users_list:
        if (int(user['user_id'])==int(username)): 
            password=input("Please enter your 4 digits Pin: ")
            if (int(user['pin'])==int(password)): 
                found_user=True
                global current_user
                current_user=user
                continue
            else:
                found_user=False
                break

    if (found_user==True):
        #clear_screen()
        print (f"{user['first_name']} {user['last_name']}, Account...")
        print(f"\nYour Current Balance is: {user['balance']}")
        menus.display_user_menu(current_user)
    else:
        print ("Access Denied. Please Try Again.")
    return
                

#user_login() 