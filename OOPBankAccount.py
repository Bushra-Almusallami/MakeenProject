class BankAccount:
    deposit=0
    def __init__(self,customer_name,account_number,balance,date_of_opening):
        self.customer_name=customer_name
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        
    def print_customer_details(self):
        return "This person name is {} with account {} and balance {}".format(self.customer_name,self.account_number,self.balance)
    
    def set_deposit(self,deposit):
        self.balance += deposit
        
    def set_withdraw(self,withdraw):
        if withdraw > self.balance:
            return "Can not withdraw amount"
        else:
            self.balance -= withdraw
            
    def check_balance(self):
            return "The balance of {} is {}".format(self.customer_name,self.balance)
        
p1= BankAccount("Ahmed","877437",1000,"2021-05-6")
p2= BankAccount("Khalid","12345",5000,"2010-09-2")

p2.set_deposit(100)
p2.set_withdraw(300)
p2.check_balance()
print(p2.print_customer_details())
#print(p3.__str__())
