from abc import ABCMeta,abstractmethod
from random import randint

# testing onec again
class Account(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def createAccount(self):
        return 0

    @abstractmethod
    def authentication(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def displayBalance(self):
        return 0

class SavingsAccount(Account):

    def __init__(self):
        self.savingsAccount = {}

    def createAccount(self,name, initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccount[self.accountNumber]=[name,initialDeposit]
        print 'Account has been created successfully. Your account number is {}'.format(self.accountNumber)

    def authentication(self,name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if name == self.savingsAccount[accountNumber][0]:
                print 'Authentication Successful.'
                self.accountNumber = accountNumber
                return True
            else:
                print 'You have entered the wrong name.'
                return False
        else:
            print '{} account number does not exist.'.format(accountNumber)
            return False


    def withdraw(self,withdrwalAmount):
        if withdrwalAmount > self.savingsAccount[self.accountNumber][1]:
            print 'You have insufficient balance.'
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrwalAmount
            print 'Successful! You have withdrwan {} amount.'.format(withdrwalAmount)
            self.displayBalance()
    def deposit(self,depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print 'Deposit has been successful.'
        self.displayBalance()
    def displayBalance(self):
        print 'Available balance is:{}'.format(self.savingsAccount[self.accountNumber][1])

savingsAccount = SavingsAccount()

while True:
    print 'Press 1 to Create a New Account.'
    print 'Press 2 to Use Existing Account.'
    print 'Press 3 to Exit.'
    userChoice = int(raw_input('Enter the number of your choice.'))
    if userChoice == 1:
        name = raw_input('Enter your name:')
        deposit = int(raw_input('Enter the initial deposit amount:'))
        savingsAccount.createAccount(name,deposit)
    elif userChoice == 2:
        name = raw_input('Enter your name:')
        accountId = int(raw_input('Enter the account number:'))
        autenticationStatus=savingsAccount.authentication(name,accountId)
        if autenticationStatus is True:
            while True:
                print 'Enter 1 to Withdraw Amount.'
                print 'Enter 2 to Deposit Amount.'
                print 'Enter 3 to Show Available Balance.'
                print 'Enter 4 to go back to previous menu.'
                userChoice = int(raw_input('Enter the number'))
                if userChoice == 1:
                    withdrawnAmount = int(raw_input('Please enter the amount to be withdrawn'))
                    savingsAccount.withdraw(withdrawnAmount)
                elif userChoice == 2:
                    depositAmount = int(raw_input('Please enter the amount to be deposited'))
                    savingsAccount.deposit(depositAmount)
                elif userChoice == 3:
                    savingsAccount.displayBalance()
                elif userChoice == 4:
                    break
    elif userChoice == 3:
        print 'GoodBye!'
        quit()

