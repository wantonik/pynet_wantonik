#!/usr/bin/env python
'''
Python script which parses cisco.txt file searching for 'crypto map CRYPTO' lines,
which children have the below string in them: 'set pfs group2'.
'''
from ciscoconfparse import CiscoConfParse    # Importing CCP module

fo = open('cisco.txt', 'r')    # Opening text file as FileObject in read mode
cisco_cfg = CiscoConfParse(fo)  # Loading this file to CCP module for further parsing
cisco_cfg               # checking if this variable returns summary of the input file
crypto_map = cisco_cfg.find_objects(r'^crypto map CRYPTO')
# Using 'find_objects' method with regex to parse the file
crypto_map              # checking if this variable contains a list with elements

# Iterating text file - crypto_map variable - to show only the crypto map CRYPTO lines
print 'Show me only lines with "crypto map CRYPTO" string: '
for obj in crypto_map:
    print obj.text

# Iterating crypto_map variable to show parent-child relationship
# with the specific string only - 'set pfs group2'
print 'Show me only lines which contain "set pfs group2" string: '
for obj in crypto_map:
    for child in obj.re_search_children("set pfs group2"):
        print obj.text, child.text
