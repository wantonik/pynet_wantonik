#!/usr/bin/env python
import snmp_helper
'''
If the running configuration has changed, then send email notification to yourself
identifying the router that changed and the time that it changed.
In this exercise, you will possibly need to save data to an external file.
E.g. to pickle.
'''

if True:
#COMMUNITY_STRING = 'galileo'
    SNMP_PORT = 161
    IP_rtr1 = '184.105.247.70'
    IP_rtr2 = '184.105.247.71'
    OID = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (IP_rtr1, SNMP_PORT)    # 7961 returns error
    pynet_rtr2 = (IP_rtr2, SNMP_PORT)    # 8061 returns error

for rtr in (pynet_rtr1, pynet_rtr2):
    ip = rtr[0]
    snmp_data = snmp_helper.snmp_get_oid_v3(rtr, snmp_user, oid=OID)
    print rtr, snmp_data
    output = snmp_helper.snmp_extract(snmp_data)
    print rtr, output
    print '\n', 40 * '-'

