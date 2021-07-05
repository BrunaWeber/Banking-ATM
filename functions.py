from typing import Match
import user

users_list = user.users_list

####FUNCTION TO CHANGE PIN###
def change_pin():
    #input("Are you sure you want to change your PIN [y/n]? ")
    print("You are going to change your PIN...")
    current_pin=input("First enter your current pin: ")
    for user in users_list:
        if (int(user['pin'])==int(current_pin)): 
            new_pin_1= input("Enter your new PIN - 4 digits: ")###################
            if len(new_pin_1) == 4 and new_pin_1.isdigit():
                new_pin_2 = input("Reenter the same PIN as above: ")
            else:
                print("Error! Enter a Valid PIN...")
                ### test because was repeating line 11

        if new_pin_1 == new_pin_2:
            pin_changed = new_pin_2
            print(f"You have changed your Pin. Your Pin now is {pin_changed}") 
            break  
        else:
            print("The two inputs don't match... Try again...")
                
    else:
        print("You are not allowed to change your pin before you enter your current pin.")
    #for user in users_list:
        
        #user.update(user) 
#change_pin()

###FUNCTION TO CHECK THE BALANCE###
def display_balance():   #after login I can display blance for users to check
    for user in users_list:
        print({user['balance']})
display_balance()    


###FUNCTION TO WITHDRAWAL MONEY###
def withdrawal_money(): #take money but first check if there is funds
###acting weird ----> insted decrease value is increasing
    for user in users_list: 
        print(f"Your Current Balance is: {user['balance']}")

        amount = float(input("Enter amount to be withdrawn: "))
        if (user['balance']) >= amount: #Check Funds
            (user['balance']) -= amount #### <------PROBLEM -----> CHANGE HERE
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
#withdrawal_money() 


###FUNCTION TO LODGE MONEY###
def lodge_money():  #add money
    amount=float(input("Enter amount to be Deposited: "))
    (user['balance']) += amount
    print("\n Amount Deposited:",amount)
#lodge_money()




###FUNCTION TO VIEW STATEMENT###
#def view_statement():
    #pass