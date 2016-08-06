#!/usr/bin/env pytho
'''
This script parses cisco.txt file and searches for 'crypto map CRYPTO' lines using CCP module.
Then it displays childrens indented multiple times for each element of crypto_map variable (list).

'''
import pprint
from ciscoconfparse import CiscoConfParse

file = open('cisco.txt', 'r')        # Opening text file wiht open() function
parse = CiscoConfParse(file)         # Loading the file to CCF module as argument for parsing later
crypto_map = parse.find_all_children(r'^crypto map CRYPTO')       # Using find_all_children method with regex (parsing)

print 'Show the content of crypto_map variable: \n',crypto_map
print

print 'Show me parent-child relationships for crypto map CRYPTO lines in cisco.txt file: '
# Iterate over elements of crypto_map list and display in a nice human readable format
for line in crypto_map:
    pprint.pprint(line)
quit()
