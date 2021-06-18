import os
import abc
import keyword

#print (os.listdir('C:\Users\Saurabh\PycharmProjects\Python\myPackage'))

class Abstract(object):
    pass
    @abc.abstractmethod()
    @property
    def load(self):
        print 'Hello'
        pass

obj = Abstract()
obj.load