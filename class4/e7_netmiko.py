#!/usr/bin/env python
'''Simple script to connect to pynet-rtr2 with Netmiko
and to change logging buffer size'''
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

def main():
    '''Use Netmiko to change logging buffer size'''
    pynet_rtr2 = ConnectHandler(**pynet2)
    
    print 'Current prompt is: ', pynet_rtr2.find_prompt(), '\n'
    
    print 'Current logging buffer size is: ','\n'
    outp = pynet_rtr2.send_command('show run | inc logging')
    print outp, '\n'
    ## Or use 'show logging' command instead:
    ## outp = pynet_rtr2.send_command('show logging | inc Log Buffer')
    ## print outp
    
    ## print 'Changing logging buffer size: '
    config_commands = ['logging buffered 20000']
    outp = pynet_rtr2.send_config_set(config_commands)
    ## print outp, '\n'
    
    print 'Checking if logging buffer size has been changed: '
    outp = pynet_rtr2.send_command('show run | inc logging')
    print outp

if __name__ == "__main__":
    main()
