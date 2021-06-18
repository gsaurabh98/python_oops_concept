
# Constructor is used to initialize the variable

class Constructor():

    x = 5
    y = 6

    def __init__(self, m ,n):

        self.value = 10
        self.a = m
        self.b = n
        sum1 = self.a+self.b
        #sum = m+n

        print 'this is constructor returns: ' , sum
      #  return sum1

    # this constructor will override the value of first constructor
    def __init__(self,x,y):

       # not initializing the x and y variable value
       # self.x = x
       # self.y = y

        self.value = 15
        new_sum = self.x + self.y

        ''' it will print new_sum where x =5 and y =6, because we have not initialize the x and y value wiih metho
        aguements'''

        print  'this constructor overrides the sum value, new_sum =' , new_sum

    def getValue(self):
        return self.value

obj = Constructor(2,3)
print obj.getValue()