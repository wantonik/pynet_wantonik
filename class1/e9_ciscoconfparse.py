#!/usr/bin/env python
'''
Python script which parses cisco.txt file searching for 'crypto map CRYPTO' lines, which children have the below string in them:
'set pfs group2'.
'''
from ciscoconfparse import CiscoConfParse        # Importing CCP module
file = open('cisco.txt', 'r')                    # Opening text file in read mode
cisco_cfg = CiscoConfParse(file)                 # Loading this file to CCP module for further parsing
cisco_cfg                                        # checking if this variable return summary of a input file
crypto_map = cisco_cfg.find_objects(r'^crypto map CRYPTO')        # Using 'find_objects' method with regex to parse the file
crypto_map                                       # checking if this variable contains a list with elements

# Iterating text file - crypto_map variable - to show only the crypto map CRYPTO lines
print 'Show me only lines with "crypto map CRYPTO" string: '
for obj in crypto_map:
    print obj.text

# Iterating crypto_map variable to show parent-child relationship with the specific string only - 'set pfs group2'
print 'Show me only lines which contain "set pfs gropu2" string: '
for obj in crypto_map:
    print obj
    print 'set pfs group2', obj.text
quit()


'''
From Kirk:
"You have an error in your logic in exercise9 that you need to fix.
You are actually printing out all of the crypto maps regardless of
whether they are using pfs group2 (or not)."
>>I have amended that in _v2 of this file.
'''
