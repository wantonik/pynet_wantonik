#!/usr/bin/env python
'''Simple script to connect to 3 networking devices with Netmiko.
Based on Kirk Byers' course'''
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
    'secret': '',
    'port': 22,
    }

pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
srx = ConnectHandler(**juniper_srx)

print pynet_rtr1
print pynet_rtr2
print srx
