# Update the User class __init__ method

# Update the User class make_deposit method

# Update the User class make_withdrawal method

# Update the User class display_user_balance method

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

class BankAccount:
    def __init__(self, intRate, balance=0):
        self.balance = balance
        self.intRate = intRate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self

    def displayAccountInfo(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        if(self.balance >= 0):
            self.balance += self.balance*self.intRate
        return self

# --------------------------------------------------------------------------

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.01)

    def makeDeposit(self, amount):
        self.account.deposit(amount)
        return self

    def makeWithdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def displayUserBalance(self):
        print(f'User: {self.name}')
        self.account.displayAccountInfo()
        return self

    def transferMoney(self, otherUser, amount):
        otherUser.makeDeposit(amount)
        self.makeWithdrawl(amount)
        print('\n')
        return self



denisse = User('Denisse', 'djlove@1.com').makeDeposit(10000).makeDeposit(500).makeDeposit(27).makeWithdrawl(363)
denisse.account.yield_interest()
denisse.displayUserBalance()

jojo = User('Jojo', 'jham@23.com').makeDeposit(2000).makeDeposit(300).makeWithdrawl(108).makeWithdrawl(40)
jojo.account.yield_interest()
jojo.displayUserBalance()

abby = User('Abby', 'abby@ham.com').makeDeposit(3000).makeWithdrawl(15).makeWithdrawl(50).makeWithdrawl(150)
abby.account.yield_interest()
abby.displayUserBalance()

abby.transferMoney(jojo,50).displayUserBalance()
jojo.displayUserBalance()