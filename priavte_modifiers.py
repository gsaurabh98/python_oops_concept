# private modifiers

class Private():

    def __init__(self,firstname,lastname):
        self.__private_variable1 = firstname
        self.__private_variable2 = lastname
        print 'the init method is printing: ' + self.__private_variable1 + ' ' + self.__private_variable2

    def myFunc(self,firstname,lastname):

        print 'My Name is ' + firstname + ' ' + lastname

obj = Private('Sidd','Sharma')
obj.myFunc('Golu','Sharma')

# below is called name mangling as obj.__private_variable1 was not accessible,
# we can call variable by putting _<classname>variablename
# as below variable is outside the class, so we can not access directly
print obj._Private__private_variable1

class Child(Private):

    def childfunc(self):
        ''' below variables we can not access as it is private and accessible with in the class
         where it is declared'''
       # print 'the childfunc method is printing: ' + self.__private_variable1 + ' ' + self.__private_variable2

obj2 = Child('Rishabh','Sharma')
obj2.childfunc()