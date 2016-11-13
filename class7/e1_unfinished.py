#!/usr/bin/env python
'''
Simple script to run 'show interfaces' from Arists eAPI. Then parsing the
output to botain 'inOctets' and 'outOctets' fields for each of the interfaces.
Use Arista's pyeapi.
'''
import pyeapi
from pprint import pprint

pynet_sw3 = pyeapi.connect_to('pynet-sw3')
print pynet_sw3, '\n'

# The below section refers to a list, so no .keys, .values, .items methods apply
show_interfaces = pynet_sw3.enable('show interfaces')
print type(show_interfaces)
print len(show_interfaces)
print show_interfaces
#pprint(show_interfaces)
print 40 * '1', '\n', '\n'


# ['result'] section
show_interfaces = show_interfaces[0]['result']
print type(show_interfaces)    # tell me what data type it is
print len(show_interfaces)    # tell me how many elements is in this data type
print show_interfaces.keys()    # tell me how many keys is in this dictionary
print show_interfaces.values()
#print show_interfaces
#pprint(show_interfaces)
print 40 * '2', '\n', '\n'


# ['interfaces'] section
show_interfaces = show_interfaces['interfaces']
#print show_interfaces
print type(show_interfaces)    # tell me what data type it is
print len(show_interfaces)    # tell me how many elements is in this data type
print show_interfaces.keys()    # tell me how many keys is in this dictionary
#print show_interfaces.values()
#print show_interfaces
#pprint(show_interfaces)
print 40 * '3', '\n', '\n'


# For loop which list the same as above ['interfaces'] section
for k in show_interfaces.items():
    print 'Data type of k is: ', type(k)
    #pprint(k), '\n'
    print 'Printing k[0]: ', k[0], 10 * '_', '\n'
    #print type(k[1])
    #print type(k[1].items()), '\n'
    #print k[1].keys(), '\n'
    #pprint(k[1].keys()), '\n'
    print 'Printing k[1] - type, len and print: '
    interfaceCounters = k[1].items()
    print type(interfaceCounters)
    print len(interfaceCounters)
    pprint(interfaceCounters)
    print '\n', 'Searching for interfaceCounters in the output: '
    print type(interfaceCounters[12][0])
    print(interfaceCounters[12][0])
    print 40 * '@', '\n'
