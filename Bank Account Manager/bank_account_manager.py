# Establish an abstract Account class with features shared by all accounts.
class Account:
    # Define an __init__ constructor method with attributes shared by all accounts:
    def __init__(self, acct_nbr, opening_deposit):
        self.acct_nbr = acct_nbr
        self.balance = opening_deposit

    # Define a __str__ mehthod to return a recognizable string to any print() command
    def __str__(self):
        return f'${self.balance: .2f}'

    # Define a universal method to accept deposits
    def deposit(self, dep_amt):
        self.balance += dep_amt

    # Define a universal method to handle withdrawals
    def withDraw(self, wd_amt):
        if wd_amt <= self.balance:
            self.balance -= wd_amt
        else:
            print('Funds Unavailable')

# Establish a Checking Account class that inherits from Account, and adds Checking-specific traits.


class CheckingAccount(Account):
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)

    def __str__(self):
        return f'Checking Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'


"""
@ TEST setting up a Checking Account object

x = CheckingAccount(54321, 654.33)
print(x)
x.withDraw(1000)
x.withDraw(300)
print(x.balance)
"""

# Set up similar Savings and Business account classes


class SavingAccount(Account):
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)

    def __str__(self):
        return f'Savings Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'


class BusinessAccount(Account):
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)

    def __str__(self):
        return f'Bussiness Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'

# Create a Customer class¶
# set up a Customer class that holds a customer's name and PIN and can contain any number and/or combination of Account objects.


class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN

        # Create a dictionary of accounts, with lists to hold multiple accounts
        self.accts = {'C': [], 'S': [], 'B': []}

    def __str__(self):
        return self.name

    def open_checking(self, acct_nbr, opening_deposit):
        self.accts['C'].append(CheckingAccount(acct_nbr, opening_deposit))

    def open_saving(self, acct_nbr, opening_deposit):
        self.accts['S'].append(SavingAccount(acct_nbr, opening_deposit))

    def open_bussiness(self, acct_nbr, opening_deposit):
        self.accts['B'].append(BusinessAccount(acct_nbr, opening_deposit))

    def get_total_deposit(self):
        print(f'Customer: {self.name}')
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f'Combined Deposits: ${total: .2f}\n')


#  functions for making deposits and withdrawals.


def make_dep(cust, acct_type, acct_num, dep_amt):
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.deposit(dep_amt)


def make_wd(cust, acct_type, acct_num, wd_amt):
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.withDraw(wd_amt)


if __name__ == "__main__":
    # @ TEST setting up a Customer, adding accounts, and checking balances

    vuong = Customer('Vuong', 123456)
    vuong.open_checking(321, 666.666)
    vuong.open_saving(124, 333.333)
    vuong.get_total_deposit()

    long = Customer('Long', 654321)
    long.open_checking(456, 123.456)
    long.open_saving(789, 567.890)
    long.get_total_deposit()
    make_dep(long, 'C', 456, 100)
    make_wd(long, 'C', 456, 200)
    long.get_total_deposit()
    make_wd(long, 'S', 789, 600)
