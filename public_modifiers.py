# Protected modifiers

class Protected():

    def __init__(self,firstname,lastname):
        self.public_variable1 = firstname
        self.public_variable2 = lastname
        print 'the init method is printing: ' + self.public_variable1 + ' ' + self.public_variable2

    def myFunc(self,firstname,lastname):

        print 'My Name is ' + firstname + ' ' + lastname

obj = Protected('Sidd','Sharma')
obj.myFunc('Golu','Sharma')

class Child(Protected):

    def childfunc(self):

        ''' below variables we can access as it is private and accessible with in the class,
        outside the class and subclass within the package'''
        print 'the childfunc method is printing: ' + self.public_variable1 + ' ' + self.public_variable2


obj2 = Child('Rishabh','Sharma')
obj2.childfunc()