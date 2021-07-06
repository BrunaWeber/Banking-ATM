import user

users_list = user.users_list
transactions_list = user.transactions_list 

####FUNCTION TO CHANGE PIN###
def change_pin(user):
    print(f"This is my currrent pin: {user['pin']}")#Check if this is the current user and its pin
    print("You are going to change your PIN...\n") 
    new_pin_1= input("Please, enter your new PIN - 4 digits: ")
    
    if len(new_pin_1) == 4 and new_pin_1.isdigit():
        print("The entered PIN has 4 digits...(CHECKED)")######Add it to check
        new_pin_2 = input("Reenter the same PIN as above: ") 
        print(f"PIN:{new_pin_1}, Checked PIN: {new_pin_2}")
        if new_pin_1 == new_pin_2:
            pin_changed = new_pin_2
            print(f"You have changed your Pin. Your Pin now is {pin_changed}") 
            (user['pin'])=(pin_changed) 
        
        if new_pin_1 != new_pin_2: 
            print("The two inputs don't match... Try again...")
        
    else:
        print("Error, try again...")
        return(input)
        
#change_pin(user)

###FUNCTION TO CHECK THE BALANCE###
def display_balance(user):   
    print(f"Balance: €{user['balance']}")
 


###FUNCTION TO WITHDRAWAL MONEY###
def withdrawal_money(user): #take money but first check if there is funds
    
    print(f"Your Current Balance is: {user['balance']}")
    amount = float(input("\nEnter amount to be withdrawn: "))
    if (user['balance']) >= amount: #Checking Funds
        after_withdrawal_balance=(user['balance']) - amount
        print("\nYou Withdrew:", amount)
        print(f"\nYour new balance is: €{after_withdrawal_balance}\n")
        return(after_withdrawal_balance)
    else:
        print("Insufficient balance...\n")
        return(withdrawal_money)
#withdrawal_money() 


###FUNCTION TO LODGE MONEY###
def lodge_money(user):  #add money
    
    print(f"Your Current Balance is: {user['balance']}")
    amount=float(input("\nEnter amount to be Deposited: "))
    after_lodge_balance=(user['balance']) + amount
    print("\nAmount Deposited: ",amount)
    print(f"\nYour new balance is: €{after_lodge_balance}\n")
    return(after_lodge_balance)
#lodge_money()

###FUNCTION TO VIEW STATEMENT###
def view_statement(user):
    print("Statement:")
    print("======================================================================================")
    print(f"First Name".ljust(15), "User ID".ljust(15), "Current Balance".ljust(20), "Overdraft Facility".ljust(20))
    print("======================================================================================")
      
    print(f"{str(user['first_name']).ljust(15)} {str(user['user_id']).ljust(15)} €{str(user['balance']).ljust(19)} {str(user['overdraft']).ljust(20)}") 
    print("\n")
#view_statement()

def view_last_transactions(transaction):
    print("Last Transactions Statement:")
    print("======================================================================================")
    print(f"Date".ljust(15), "Transaction".ljust(15), "Amount".ljust(20), "Balance".ljust(20))
    print("======================================================================================")
    
    for transaction in transactions_list:  
        print(f"{transaction['Date'].ljust(15)} {transaction['transaction'].ljust(15)} €{str(transaction['amount']).ljust(19)} €{transaction(user['balance_after']).ljust(19)}") 
        print("\n")

    
        
   