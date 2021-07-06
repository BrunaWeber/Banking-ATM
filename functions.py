import user

users_list = user.users_list

####FUNCTION TO CHANGE PIN###
def change_pin(user):
    print("You are going to change your PIN...\n") 
    #current_pin=input("First enter your current pin: ")
    new_pin_1= input("Please, enter your new PIN - 4 digits: ")
    for user in users_list:
        if len(new_pin_1) == 4 and new_pin_1.isdigit():
            print("The entered PIN has for digits...(CHECKED)")######add to check
            new_pin_2 = input("Reenter the same PIN as above: ") 
            print(f"PIN:{new_pin_1}, checked PIN: {new_pin_2}")
            if new_pin_1 == new_pin_2:
                pin_changed = new_pin_2
                print(f"You have changed your Pin. Your Pin now is {pin_changed}") 
                (user['pin'])=(pin_changed) #todo#####check it (I TRY DO IT TO STORE THE NEW PIN (PIN_CHANGED INSIDE OF PIN KEY))
            return(pin_changed) 
            #if new_pin_1 != new_pin_2: ###errors because I am not putting it
                #print("The two inputs don't match... Try again...")
            
        else:
            print("Please enter a 4 digit PIN.")
            return(input)
        
#change_pin(user)

###FUNCTION TO CHECK THE BALANCE###
def display_balance():   #after login I can display blance for users to check
    for user in users_list:
        print({user['balance']})
#display_balance()    


###FUNCTION TO WITHDRAWAL MONEY###
def withdrawal_money(): #take money but first check if there is funds
    for user in users_list: 
        print(f"Your Current Balance is: {user['balance']}")
        amount = float(input("\nEnter amount to be withdrawn: "))
        if (user['balance']) >= amount: #Checking Funds
            after_withdrawal_balance=(user['balance']) - amount
            print("\nYou Withdrew:", amount)
            print(f"\nYour new balance is:{after_withdrawal_balance}\n")
            return(after_withdrawal_balance)
        else:
            print("Insufficient balance...\n")
            return(withdrawal_money)
#withdrawal_money() 


###FUNCTION TO LODGE MONEY###
def lodge_money():  #add money
    for user in users_list:
        print(f"Your Current Balance is: {user['balance']}")
        amount=float(input("\nEnter amount to be Deposited: "))
        after_lodge_balance=(user['balance']) + amount
        print("\nAmount Deposited: ",amount)
        print(f"\nYour new balance is: {after_lodge_balance}\n")
        return(after_lodge_balance)
#lodge_money()




###FUNCTION TO VIEW STATEMENT###
#def view_statement():
    #pass