#!/usr/bin/env python
from snmp_helper import snmp_get_oid,snmp_extract
## Script that connects to routers pynet-rtr1 and pynet-rtr2,
## and prints out MIB2: sysName and sysDescr.

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
OID = ['1.3.6.1.2.1.1.1.0','1.3.6.1.2.1.1.5.0']
IP = [{'184.105.247.70':OID},{'184.105.247.71':OID}]

print IP
print

#i = 0
#print IP[[0][0]]

for ip_addr in IP:
    a_device = (IP(ip_addr), COMMUNITY_STRING, SNMP_PORT)    # this is a tuple
    print a_device

print OID[0]


# Query an OID and return hex data format as output
#snmp_data = snmp_get_oid(a_device, oid=OID[0])

#i = 0
#num = len(IP)
#while i < num:
#    print snmp_data[i]
#    i += 1









'''
output_rtr1_sysDescr = snmp_extract(snmp_data_rtr1_sysDescr)
output_rtr1_sysName = snmp_extract(snmp_data_rtr1_sysName)

output_rtr2_sysDescr = snmp_extract(snmp_data_rtr2_sysDescr)
output_rtr2_sysName = snmp_extract(snmp_data_rtr2_sysName)

print
print IP1, ' is pynet-rtr1 IP address.'
print 'sysDescr OID: ', 10 * '*', '\n', output_rtr1_sysDescr + '\n'
print 'sysName OID = ', output_rtr1_sysName + '\n'
print 40 * '-'
print IP2, ' is pynet-rtr2 IP address.'
print 'sysDescr OID: ', 10 * '*', '\n', output_rtr2_sysDescr + '\n'
print 'sysName OID = ', output_rtr2_sysName + '\n'
'''
