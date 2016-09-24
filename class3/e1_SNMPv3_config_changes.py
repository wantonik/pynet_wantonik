#!/usr/bin/env python
import snmp_helper
'''
If the running configuration has changed, then send email notification to yourself
identifying the router that changed and the time that it changed.
In this exercise, you will possibly need to save data to an external file.
E.g. to pickle.
'''

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP = '184.105.247.71'
OID = '1.3.6.1.4.1.9.9.43.1.1.1.0'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr2 = (IP, SNMP_PORT)

snmp_data_rtr2 = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=OID)
print snmp_data_rtr2

output_rtr2 = snmp_helper.snmp_extract(snmp_data_rtr2)

print
print 40 * '-'
print pynet_rtr2, ' is pynet-rtr2 IP address.'
print 'Running configuration has changed: ', output_rtr2, '\n'
print 'It has changed at TIME.'
