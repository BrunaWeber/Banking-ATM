import os
import user
import menus


users_list = user.users_list
current_user = ""

def clear_screen():
    os.system('cls')
  
def user_login():
    print("===================")
    print("*** USER LOGIN ***")
    print("===================\n")
    
    username=input("Please enter your User ID:  ")#after this read that the access is denied....?????????????
    
    found_user=False

    for user in users_list:
        #print(user) # use it to test if print user info
        if (int(user['user_id'])==int(username)): 
            #print("print step 2") ### used to test
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
        print (f"{user['first_name']} {user['last_name']}, Your access is granted...")
        menus.display_user_menu(current_user)
    else:
        print ("Access Denied. Please Try Again.")
    return
                

user_login() 