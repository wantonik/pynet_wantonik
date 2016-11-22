#!/usr/bin/env python
'''This is simple script to do the following:
a. Verify that you can import mytest and call the three functions func1(), func2(), and func3().
b. Create an object that uses MyClass. Verify that you call the hello() and not_hello() methods.
'''

from mytest import *

print 'List of available functions provided by mytest package is:'
print dir(), 10 * '#', '\n'

def testing_func():
    '''Here we tests available functions'''
    print 'Testing func1:'
    func1()
    print '\n', 'Testing now func2:'
    func2()
    print '\n', 'and finally testing func3:'
    func3()
    print 40 * '_', '\n'
testing_func()

def testing_class():
    '''Here we test available class'''
    print 'Testing MyClass:'
    my_obj = MyClass('Jimi,', 'Rory,', 'Paul')
    my_obj.hello()
    my_obj.not_hello()
    print 40 * '_'
testing_class()
    
