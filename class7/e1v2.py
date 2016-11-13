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

show_interfaces = pynet_sw3.enable('show interfaces')
#print show_interfaces, '\n', 40 * '*'
#pprint(show_interfaces)
print type(show_interfaces)
print len(show_interfaces)
print 40 * '-', '\n'

show_interfaces = show_interfaces[0]['result']
#pprint(show_interfaces)
print type(show_interfaces)    # tell me what data type it is
print len(show_interfaces)    # tell me how many elements is in this data type
print show_interfaces.keys()    # tell me how many keys is in this dictionary
print 40 * '-', '\n', '\n'
show_interfaces = show_interfaces['interfaces']
#print show_interfaces
print type(show_interfaces)    # tell me what data type it is
print len(show_interfaces)    # tell me how many elements is in this data type
print show_interfaces.keys()    # tell me how many keys is in this dictionary
print 40 * '#'

# inOctets/outOctets are fields inside 'interfaceCounters' dict
data_stats = {}
for interface, int_values in show_interfaces.items():
    int_counters = int_values.get('interfaceCounters', {})
    data_stats[interface] = (int_counters.get('inOctets'), int_counters.get('outOctets'))

# Print output data
print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
for intf, octets in data_stats.items():
    print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])
print
