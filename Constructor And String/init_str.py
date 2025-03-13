

class bank_account:
    
    def __init__(self,customer_name, balance, account_number):
        self.customer_name = customer_name
        self.balance = balance
        self.account_number = account_number
        
    def __str__(self):
        return self.customer_name
    
bank1 = bank_account("Logu", 100000, 12345)

print(bank1.customer_name, bank1.balance, bank1.account_number)

print(bank1)