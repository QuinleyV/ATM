class ATM:

    #initializes the class with bal as parameter
    def __init__(self, bal):
        self.__balance = bal

    #will add amount to initial balance
    def set_deposit(self, amount):
        self.__balance += amount

    #checks to see if amount to withdraw is avaialable
    #if not it will display an error message
    def set_withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else: print('Error: Insufficient Funds')
    
    #tells the user the balance
    def get_balance(self):
        return self.__balance