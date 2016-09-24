#!/usr/bin/env python
from snmp_helper import snmp_get_oid,snmp_extract
## Script that connects to routers pynet-rtr1 and pynet-rtr2,
## and prints out MIB2: sysName and sysDescr.

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP1 = '184.105.247.70'    #rtr1
OID1 = '1.3.6.1.2.1.1.1.0'    #sysDescr
IP2 = '184.105.247.71'    #rtr2
OID2 = '1.3.6.1.2.1.1.5.0'    #sysName

rtr1 = (IP1, COMMUNITY_STRING, SNMP_PORT)    # this is a tuple
rtr2 = (IP2, COMMUNITY_STRING, SNMP_PORT)    # this is a tuple

snmp_data_rtr1_sysDescr = snmp_get_oid(rtr1, oid=OID1)
snmp_data_rtr1_sysName = snmp_get_oid(rtr1, oid=OID2)

snmp_data_rtr2_sysDescr = snmp_get_oid(rtr2, oid=OID1)
snmp_data_rtr2_sysName = snmp_get_oid(rtr2, oid=OID2)


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
