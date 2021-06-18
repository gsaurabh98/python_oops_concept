class Shape(object):

    def area_of_dimen(self,width,height):
        self.width = width
        self.height= height
        return self.width * self.height

    def perimeter_two_dimen(self):
        return 2*(self.height + self.width)

    def area_of_dimen(self,width,height,length):
        self.width = width
        self.height = height
        self.length = length
        return (self.length*self.width*self.height)

obj = Shape()
#print obj.area_of_dimen(2,3)
print obj.area_of_dimen(2,3,4)