#Bank Account 💵

class Bank_account:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance += amount
        return self.balance
    
    def display_balance(self):
        print("Your balance is: " + str(self.balance) + " reais.")

paulolos_account = Bank_account("Paulo", "Souza", 333444, "Savings Account", 2115, 100.0)

print(vars(paulolos_account))

paulolos_account.deposit(96.0)
paulolos_account.withdraw(-25.0)
paulolos_account.display_balance()