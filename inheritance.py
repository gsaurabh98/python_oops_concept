class Vehicle(object):
    comfort = 'Luxurios'
    def __init__(self,name,color,wheel):
        self.name = name
        self.color = color
        self.wheel = wheel
        print 'this is parent class'

    def bus(self):
        print 'this' + ' ' + self.color + ' ' + self.name + ' has ' + str(self.wheel) + ' wheels.'

class Car(Vehicle):
    def porshe(self):
        print 'this' + ' ' +self.color +' '+ self.name + ' has ' + str(self.wheel) + ' wheels.'

class MotorCycle(Vehicle):

    def __init__(self,name,color,wheel,kick):
        super(MotorCycle,self).__init__(name, color, wheel)

        # we can also pass like below
        #Vehicle.__init__(self,name,color,wheel)

        self.kick = kick
    def pulsar(self):

        print 'this' + ' ' + self.color + ' ' + self.name + ' has ' + str(self.wheel) + ' wheels ' + 'without' , self.kick

obj1 = Vehicle('BMW','White',12)
obj2 = Car('Jaguar', 'Black',4)
obj3 = MotorCycle('PulasrNS', 'Matt Black',2,'kick')
#obj1.bus()
obj2.porshe()
obj3.pulsar()
print obj3.color
print obj3.comfort

print (isinstance(obj2,Vehicle))
print (issubclass(Car,MotorCycle))