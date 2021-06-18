class Animal(object):

    def __init__(self,name,type,qualities,size):
        self.name = name
        self.type = type
        self.qualities = qualities
        self.size = size

    def small(self):
        return self.name

    def big(self):
        return self.size


class Bird(Animal):

    def __init__(self,name,type,qualties,size,color):
        super(Bird, self).__init__(name,type,qualties,size)
        self.color = color
        print self.color

    def small(self):
       return self.name

    def big(self):
        return self.size

def main():
    obj1 = Animal('tiger','animal','fast runs','medium')
    obj2 = Bird('Eagle','bird','sharp eyes','small','black')
    #print obj2.color
    print obj1.small()
    print obj1.big()

if __name__ == '__main__':
    main()