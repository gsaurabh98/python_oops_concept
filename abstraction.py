#abc = abstract base class
from abc import ABCMeta, abstractmethod
# Shape is a metaclass by using of __metaclass__ = ABCMeta
#shape class is an interface
#we dont create instance of this class
class Shape():
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

# this is also as multilevel inheritance as we are calling square by rectange.
class Rectangle(Shape):

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width+self.height)
    
class Square(Rectangle):
    
    def __init__(self,sides):
        # as Rectangle has two parameter, so in below super method, we need to pass two parameter in init
        super(Square, self).__init__(sides,sides)
        self.sides = sides

    #Override the rectangle area
    # def area(self):
    #     print 'this must be called'
    #     return self.sides**2
    #
    # def perimeter(self):
    #     return 4*(self.sides)

rect = Rectangle(6,5)
sq = Square(5)
print 'area of square is:', sq.area()
print 'perimeter of square is:' ,sq.perimeter()


