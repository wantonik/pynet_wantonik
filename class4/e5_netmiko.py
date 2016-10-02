#!/usr/bin/env python
'''Simple script to connect to pynet-rtr2 with Netmiko.
Use Netmiko to enter into configuration mode on pynet-rtr2.
Also use Netmiko to verify that you are in configuration mode.'''
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
    'port': 22,
    }

pynet_rtr2 = ConnectHandler(**pynet2)

print 10 * '>', 'Show me current prompt:\n', pynet_rtr2.find_prompt(), '\n'
print 10 * '>', 'Enter config mode:\n', pynet_rtr2.config_mode(), '\n'
print 10 * '>', 'Check if you are in config mode:\n', pynet_rtr2.check_config_mode(), '\n'

if pynet_rtr2.check_config_mode() == True:
    print 10 * '_','The config mode prompt is:', 10 * '_', '\n', pynet_rtr2.find_prompt()
else:
   print 'You are not in config mode - try again.'

