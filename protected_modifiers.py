# Protected modifiers

class Protected():

    def __init__(self,firstname,lastname):
        self._protected_variable1 = firstname
        self._protected_variable2 = lastname
        print 'the init method is printing: ' + self._protected_variable1 + ' ' + self._protected_variable2

    def myFunc(self,firstname,lastname):

        print 'My Name is ' + firstname + ' ' + lastname

obj = Protected('Sidd','Sharma')
obj.myFunc('Golu','Sharma')

class Child(Protected):

    def childfunc(self):

        ''' below variables we can access as it is protected and accessible with in the class
         and subclass as well'''
        print 'the childfunc method is printing: ' + self._protected_variable1 + ' ' + self._protected_variable2


obj2 = Child('Rishabh','Sharma')
obj2.childfunc()