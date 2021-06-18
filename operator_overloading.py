# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)
#
#
# p1 = Point(2, 7)
# print(p1)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

#What actually happens is that, when you do p1 + p2, Python will call p1.__add__(p2)
#which in turn is Point.__add__(p1,p2). Similarly, we can overload other operators as well.
#The special function that we need to implement is tabulated below.

    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

p1 = Point(2,3)
p2 = Point(-1,2)
print p1
print p2
p3 = p1+p2
print p3

print p1<p2
print Point(1,1) < Point(0.5,-0.2)