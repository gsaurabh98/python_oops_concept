class BankAccount(object):

    def __init__(self,account_name = 'Saving Account',balance=2000):
        self.__account_name = account_name
        self.__balance = balance

    def get_method(self):

       # print 'after set_method, get_method will be called '
        print 'your current balance is: ' , self.__balance
        #return self.__balance

    def set_method(self,value):

       # print 'set_method will be called first'
        if self.__balance > value:
           self.__balance = self.__balance - value
           print 'Your current balance is:' , self.__balance
           return self.__balance
        else:
            print 'you dont have enough funds'

def main():
    obj = BankAccount()
    #obj.set_method(input('how much you want to withdraw: '))
    #obj.get_method()
    while True:
        #print 'select options from 1 and 2 '
        print ('1. Check account funds')
        print ('2. Withdraw Funds')
        menu_options = int(input())

        if menu_options ==1:
            obj.get_method()
        elif menu_options ==2:
            print 'how much you want to withdraw ?' , obj.set_method(int(input()))
        else:
            print 'Wrong menu choice!'
            exit()

if __name__ == '__main__':
    main()