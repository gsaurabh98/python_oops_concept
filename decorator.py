# object is being inherited to access all the properties
class Employee(object):

    def __init__(self,first,last):
        self.first = first
        self.last = last

# by adding the property decorator, email and fullname method will act as attribute, see line 37 and 38
    @property
    def email(self):
        return 'email addess is: {}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return 'Full Name is: {} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        print 'this will be called first: Setter Property'
        print 'splitting name using split() function...'
        self.first, self.last = name.split(' ')
        print 'now first name is:', self.first
        print 'now last name is:', self.last

    @fullname.deleter
    def fullname(self):
        print 'this will be called at last: Deleter Property'
        self.first = None
        self.last = None

obj = Employee('Saurabh','Sharma')
obj.fullname = 'John Smith'

#name.firstname = 'John'
# in below method call we have not used '()' because we have define @property decorator for email and fullname

print obj.email
print obj.fullname

del obj.fullname