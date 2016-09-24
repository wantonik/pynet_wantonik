#!/usr/bin/env python
'''This is simple script to connect to lab router - pynet-rtr2,
and run 'show version' command.'''
import paramiko, time
from getpass import getpass

ip_addr = '184.105.247.71'
username = 'pyclass'
password = getpass()
timeout = 10
port = 22

remote_conn_pre = paramiko.SSHClient()
#remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#add_host_key_policy = paramiko.AutoAddPolicy
remote_conn_pre.load_system_host_keys()
remote_conn_pre.connect(ip_addr, username=username, password=password, port=port, timeout=timeout, look_for_keys=False, allow_agent=False)
print remote_conn_pre.get_transport(), '\n'
remote_conn = remote_conn_pre.invoke_shell()
outp = remote_conn.recv(5000)
print '\n', 40 * '*', '\n', 'If prompt received below, you are connected.', '\n', outp
remote_conn.settimeout(6.0)    ## Wait for the data 6sec
print 40 * '*'
remote_conn.send("terminal length 0\n")
time.sleep(1)
outp = remote_conn.recv(5000)
time.sleep(1)

## Send 'show version' to router and display on screen
remote_conn.send("\n")
time.sleep(1)
remote_conn.send('show version')
time.sleep(1)
remote_conn.send("\n")
time.sleep(1)
outp = remote_conn.recv(65535)
time.sleep(1)
print outp, '\n'    ## outp.readlines() method doesn't work here

## Verify if there's anything else to receive from the router
print 80 * '.'
outp = remote_conn.recv_ready()
if outp == False:
    print 'No more data is expected from ', ip_addr
else:
    print "There's still some data to be received from ", ip_addr
