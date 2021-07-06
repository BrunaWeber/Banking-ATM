# Data Types:
# user_id - string
# pin - strin
# first_name - string
# last_name - string
# balance - float
# overdraft - boolean 
users_list = []
def add_users():    
    users_list.append({"user_id": 1111, 
                       "pin": 1234, 
                       "first_name": "Bruna", 
                       "last_name": "Weber", 
                       "balance": 680.50, 
                       "overdraft": True})
    users_list.append({"user_id": 2222, 
                       "pin": 4321, 
                       "first_name": "Bianca", 
                       "last_name": "Konrath", 
                       "balance": 850.00, 
                       "overdraft": True})
    users_list.append({"user_id": 3333, 
                       "pin": 1234, 
                       "first_name": "Carol", 
                       "last_name": "Brien", 
                       "balance": 1800.00, 
                       "overdraft": False})
    users_list.append({"user_id": 4444, 
                       "pin": 5678, 
                       "first_name": "Eva", 
                       "last_name": "Thompson", 
                       "balance": 9500.00, 
                       "overdraft": False})
    users_list.append({"user_id": 5555, 
                       "pin": 8765, 
                       "first_name": "Alex", 
                       "last_name": "Cooper", 
                       "balance": 850.00, 
                       "overdraft": False})
#add_users()