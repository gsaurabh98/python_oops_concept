class Myclass(object):

    __firstName = 'Saurabh' # protected variable
    __lastName = '' # private variable

    # def __init__(self,firstName,lastName):
    #    self.firstName = firstName
    #    self.lastName = lastName
    #    print self.firstName + " " + self.lastName
    #    print 'Calling first init'

    def setFirstName(self,firstName):
        self.__firstName =  firstName

    def getFirstName(self):
        return self.__firstName
    # test

    def __init__(self,firstName,lastName):
        print 'fistname is:', self.firstName
        print  'In Parent'


#     def myfunc(self,x,y):
#         var3 = 'xyz'
#
#         self._var1 = x
#         self.__var2 =y
#         print self._var1 + ' ' + self.__var2
#
#obj = Myclass('Sidd','Sharma')
#obj2 = Myclass ('Rishabh','Sharma')
#obj.myfunc('Sidd','Sharma')


class Second(Myclass):
    firstName = 'xyz'


    def secondfun(self):

        print self.firstName
        print Myclass.firstName
        print 'second class'


obj3 = Second('Sidd','Sharma')
obj3.secondfun()