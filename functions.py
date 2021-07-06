import user

users_list = user.users_list

####FUNCTION TO CHANGE PIN###
def change_pin():
    print("You are going to change your PIN...") #--> ok
    #current_pin=input("First enter your current pin: ")
    new_pin_1= input("Please, enter your new PIN - 4 digits: ")
    for user in users_list:
        if len(new_pin_1) == 4 and new_pin_1.isdigit():
            print("Pin1 is digt and has for digits...")######add to check
            new_pin_2 = input("Reenter the same PIN as above: ") # ----> IT IS BEING REPEATED
            print(f"pin:{new_pin_1} check pin:{new_pin_2} ")#### add to check
            if new_pin_1 == new_pin_2:
                pin_changed = new_pin_2
                print(f"You have changed your Pin. Your Pin now is {pin_changed}") 
                (user['pin'])=(pin_changed) #####check it (I TRY DO IT TO STORE THE NEW PIN (PIN_CHANGED INSIDE OF PIN KEY))
            break  
            #else:
                #print("The two inputs don't match... Try again...")
        else:
            print("Please enter a 4 digit PIN.")
        
#change_pin()

###FUNCTION TO CHECK THE BALANCE###
def display_balance():   #after login I can display blance for users to check
    for user in users_list:
        print({user['balance']})
#display_balance()    


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