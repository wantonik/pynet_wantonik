#!/usr/bin/env python
'''Script which connects a network device remotely via telnet protocol.
And executes IOS-type of commands.'''

import telnetlib, time

# Declare global variables
ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'
TELNET_PORT = 23
TELNET_TIMEOUT = 6    # in seconds

# Connection details
remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
rtr_login = remote_conn.read_until("sername: ",TELNET_TIMEOUT)
remote_conn.write(username + '\n')
rtr_password = remote_conn.read_until("assword: ",TELNET_TIMEOUT)
remote_conn.write(password + '\n')
print rtr_login, rtr_password
time.sleep(1)

# Disabling more paging
remote_conn.write("terminal length 0" + '\n')
time.sleep(1)

# 'show ip int brief' to return by rtr-1
remote_conn.write("show ip int brief" + '\n')
time.sleep(1)
output = remote_conn.read_very_eager()
print output

# Closing remote connection
remote_conn.close()
