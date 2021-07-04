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
    
    username=input("Please enter your User ID:  ")
    
    user_fname='first_name'
    user_lname='last_name'
    found_user=False

    for user in users_list:
        if (user[int('user_id')]==username): #after this read that the access is denied....?????????????
            password=input("Please enter your 4 digits Pin: ")
            if (user[int('pin')]==password): 
                found_user=True
                current_user=user
                continue
            else:
                found_user=False
                break

    if (found_user==True):
        print (f"Welcome to your Bank Account {user['first_name']}!\n Your access is granted...")
        menus.usermenu(current_user)
    else:
        print ("Access Denied. Please Try Again.")
    return
                

user_login() 
   





            
                

