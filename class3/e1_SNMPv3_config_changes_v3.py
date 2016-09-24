#!/usr/bin/env python
import snmp_helper
from email_helper import send_mail
from getpass import getpass
import cPickle as pickle
from datetime import datetime
'''
If the running configuration has changed, then send email notification to yourself
identifying the router that changed and the time that it changed.
In this exercise, you will possibly need to save data to an external file.
E.g. to pickle.
'''

if True:
#COMMUNITY_STRING = 'galileo'
    #DEBUG = True
    #RELOAD_WINDOW = 300 * 100
    #OIDS = [{'RUN_LAST_CHANGED' :'1.3.6.1.4.1.9.9.43.1.1.1.0'}, {'SYS_NAME' :'1.3.6.1.2.1.1.5.0'}, {'SYS_UPTIME' :'1.3.6.1.2.1.1.3.0'}]
    OIDS = ['1.3.6.1.4.1.9.9.43.1.1.1.0', '1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.3.0']
    SNMP_PORT = 161
    IPADDR = ['184.105.247.70', '184.105.247.71']
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtrs = (IPADDR, SNMP_PORT)
    print '\n', 'These are IP addresses of lab network ', '\n', pynet_rtrs
    print 40 * '-'

## 'for' loop traverses each element of 'ipaddr' list as input for pynet_rtrs variable
for my_ip in IPADDR:
    pynet_rtrs = (my_ip, SNMP_PORT)
    for my_oid in OIDS:
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtrs, snmp_user, oid=my_oid)
        print '\n', my_oid, '\n', snmp_data,'\n'
        output = snmp_helper.snmp_extract(snmp_data)
    current_time = datetime.now()
    print
    print 10 * '*', ' Run last changed: ', output
    print 10 * '*', ' at date_time: ', current_time
    print 10 * '*', ' on device ip address: ', my_ip
    print '\n', 40 * '-'

def send_email():
    pass

send_email()
