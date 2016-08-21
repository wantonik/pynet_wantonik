#!/usr/bin/env python
'''
Script using CiscoConfParse to find lines which does not use
AES-SHA encryption method (based on the transform-set name).
Printing these lines along with their corresponding transform-set names.
'''
from ciscoconfparse import CiscoConfParse

fo = open('cisco.txt', 'r')    # Open text as file object in read mode
cisco_cfg = CiscoConfParse(fo) # Loading the text file to CCP module for parsing
print 'Checking if the text file got loaded by CCP module: \n', cisco_cfg
print

'''
Using find_object_wo_child to:
1. Find parents - crypto map CRYPTO lines
2. To find lines other than those which contain 'AES-SHA' string
''' 

crypto_map = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES-SHA')
print 'The crypto map line which does not use AES-SHA encryption is: \n', crypto_map

# Nested 'for' iterating through a crypto_map list to find parent-child lines
print 'Showing details of the lines which does not contain "AES-SHA"\
 encryption method in parent-child format: '
for entry in crypto_map:
    print entry.text
    for child in entry.children:
        print child.text
