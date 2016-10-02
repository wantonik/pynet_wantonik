#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

def main():
    '''Use Netmiko to change logging buffer size (logging buffered <size>)
    and to disable console logging (no logging console) from a file
    on pynet-rtr1 and pynet-rtr2 routers.'''
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

    routers = [pynet1, pynet2]

    for rtr in routers:
        # Connect to router
        router_conn = ConnectHandler(**rtr)

        # Change config from file
        router_conn.send_config_from_file(config_file='config_commands.txt')

        # Validate changes
        print 10 * '*', router_conn.find_prompt(), 10 *  '*'
        outp = router_conn.send_command("show run | inc logging")
        ## In the above line you can use send_command_expect instead
        print outp, '\n'

        # Close connection
        router_conn.disconnect()


if __name__ == '__main__':
    main()
