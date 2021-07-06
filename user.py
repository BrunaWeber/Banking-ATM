# Data Types:
# user_id - integer
# pin - integer
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
                       "balance": 950.00, 
                       "overdraft": False})
#add_users()

transactions_list = []

def add_transactions():  
    transactions_list.append({"Date":"2021-05-11", 
                       "user_id": 1111, 
                       "transaction": "withdrawal",
                       "amount": 100.00,  
                       "balance_before": 780.50, 
                       "balance_after": 680.50}) 
    transactions_list.append({"Date":"2021-05-21", 
                       "user_id": 1111, 
                       "transaction": "change pin",
                       "amount": 0.00,  
                       "balance_before": 580.50, 
                       "balance_after": 580.50})                    
    transactions_list.append({"Date":"2021-04-11", 
                       "user_id": 2222, 
                       "transaction": "lodgment",
                       "amount": 200.00,  
                       "balance_before": 650.00, 
                       "balance_after": 850.00})  
    transactions_list.append({"Date":"2021-04-11", 
                       "user_id": 3333, 
                       "transaction": "withdrawal",
                       "amount": 300.00,  
                       "balance_before": 1500.00, 
                       "balance_after": 1800.00})                    
    transactions_list.append({"Date":"2021-04-11", 
                       "user_id": 3333, 
                       "transaction": "withdrawal",
                       "amount": 300.00,  
                       "balance_before": 9800.00, 
                       "balance_after": 9500.00}) 
    transactions_list.append({"Date":"2021-06-11", 
                       "user_id": 4444, 
                       "transaction": "lodgment",
                       "amount": 200,  
                       "balance_before": 750.00, 
                       "balance_after": 950.00})   
    transactions_list.append({"Date":"2021-04-11", 
                       "user_id": 5555, 
                       "transaction": "change_pin",
                       "amount": 0.00,  
                       "balance_before": 1050.00, 
                       "balance_after": 950.00})  

add_transactions()                       
