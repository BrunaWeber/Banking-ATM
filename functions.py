import user
users_list = user.users_list

####FUNCTION TO CHANGE PIN###
def change_pin():
    #input("Are you sure you want to change your PIN [y/n]? ")
    print("You are going to change your PIN...")
    ###users_list.user.update
    new_pin_1= input("Enter a 4 digit number: ")
    if len(new_pin_1) == 4 and new_pin_1.isdigit():
        new_pin_2 = input("Reenter the same PIN as above: ")
    else:
        print("Error! Enter a Valid PIN...")

    if new_pin_1 == new_pin_2:
        pin_changed = print(repr(new_pin_2))
        print(f"You have changed your Pin. Your Pin now is {pin_changed}")   
     
#change_pin()

###FUNCTION TO WITHDRAWAL MONEY###
def withdrawal_money():
    pass 




###FUNCTION TO LODGE MONEY###
def lodge_money():
    pass

###FUNCTION TO VIEW STATEMENT###
def view_statement():
    pass