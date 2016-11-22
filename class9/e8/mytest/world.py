#!/usr/bin/env python
'''Excercise_8 - class9 - Reusable Code'''

def func1():
    '''func1 to print simple statement'''
    print 'Excercise_8 from class9 - world.py'


class MyClass(object):
    '''Test class'''
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def hello(self):
        '''Test method 1 named "hello2"'''
        print 'Hello using 3 variables: {} {} {}'.format(self.var1, self.var2, self.var3)

    def not_hello(self):
        '''Test method 2 named "not_hello"'''
        print 'Not_hello using 3 variables: {} {} {}'.format(self.var1, self.var2, self.var3)

class MyChildClass(MyClass):
    '''This is child class'''
    def hello(self):
        print 'My favourite bands: {} {} {}'.format(self.var1, self.var2, self.var3)


if __name__ == "__main__":
    print 'This is main program from world.py file.'
    print 'This is executable code...'
    my_obj = MyClass('Paul Kossof,', 'Jimi Hendrix,', 'Tadeusz Nalepa')
    print '\n', my_obj.var1, my_obj.var2, my_obj.var3
    my_obj.hello()
    my_obj.not_hello()
    print 40 * '_', '\n'

    print 'This relates to MyChildClass...'
    my_obj2 = MyChildClass('FREE', 'Rory Gallagher', 'Led Zeppelin')
    my_obj2.hello()
    my_obj2.not_hello()
