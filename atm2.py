import atm

#begins user with starting balance of $100,000
starting_balance = 100000

#creates and object of ATM class
#passes the starting_balance variable to the bal parameter
savings = atm.ATM(starting_balance)

#sets global constants for menu
WITHDRAW = 1
BALANCE = 2
DEPOSIT = 3
QUIT = 4


def main():

    #initializes the users choice to 0
    choice = 0 

    while choice != QUIT:
        #gets the users choice
        choice = menu()
        
        #processes the users choice
        if choice == WITHDRAW:
            withdraw()
        elif choice == BALANCE:
            balance()
        elif choice == DEPOSIT:
            deposit()


def menu():
    
    #Creates a menu for the user to select operations from
    print()
    print('What would you like to do?')
    print('Press 1 to Withdraw')
    print('Press 2 to Check Balance')
    print('Press 3 to Deposit')
    print('Press 4 to Quit')
    print()

    #user enters their choice here
    choice = int(input('Enter choice here: '))

    #validates the users choice
    while choice < WITHDRAW or choice > QUIT:
        choice = int(input('Please enter a valid choice'))

    #returns the users choice
    return choice

def withdraw():
    #sets the constants for quick withdraw
    twenty = 1
    fourty = 2
    sixty = 3
    eighty = 4
    hundred = 5
    other = 0


    #sets a limit for how much the user can withdraw
    limit = 800

    #initializes users choice to 0
    withdrw_choice = 0

    #quick withdraw menu
    print()
    print('Quick withdraw')
    print('1: $20')
    print('2: $40')
    print('3: $60')
    print('4: $80')
    print('5: $100')
    print('0: Other amount')
    withdrw_choice = int(input('Enter choice here: '))
    print()

    
    #processes the users withdraw choice
    if withdrw_choice == 0:
        print('Daily limit is $800')
        print('Withdraw amount should be in multiples of ten')
        amount = int(input('How much would you like to withdraw: '))
        if amount > limit or amount <= 0:
            amount = int(input('Enter a valid amount: '))
        savings.set_withdraw(amount)
    elif withdrw_choice == 1:
        savings.set_withdraw(20)
    elif withdrw_choice == 2:
        savings.set_withdraw(40)
    elif withdrw_choice == 3:
        savings.set_withdraw(60)
    elif withdrw_choice == 4:
        savings.set_withdraw(80)
    elif withdrw_choice == 5:
        savings.set_withdraw(100)

    #returns the users choice
    return withdrw_choice

    


def deposit():
    #asks user how much they want to deposit
    cash = int(input('How much did you want to deposit?: '))

    print('Okay, I will deposit that')

    #passes the cash variable to the amount parameter in the set_deposit function
    savings.set_deposit(cash)


def balance():
    #prints the balance when the user calls this function
    print('Your balance is $', format(savings.get_balance(), ',.2f'), sep="")


#calls the main function 
main()

input('Press ENTER key to exit')