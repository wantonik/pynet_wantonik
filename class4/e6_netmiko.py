#!/usr/bin/env python
'''Simple script to connect to 3 networking devices with Netmiko
and exectuting 'show arp' command them.'''
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': password,
    'port': 22,
    }

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
    'port': 22,
    }

juniper_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': password,
    'port': 22,
    }

pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
srx = ConnectHandler(**juniper_srx)

print 'Show me to which devices am I connected - 3 lines of output are expected:'
print pynet_rtr1, '== pynet1 Cisco 880 router'
print pynet_rtr2, '== pynet2 Cisco 880 router'
print srx, '== Juniper SRX router'

def showArp():
    conn_to_routers = [pynet_rtr1, pynet_rtr2, srx]
    for rtr in conn_to_routers:
        outp = rtr.send_command('show arp')
        print '\n', 20 * '*'
        print 'The output of "show arp" on ', rtr, ' networking device is: '
        print '\n', outp
showArp()
