#!/usr/bin/env python
'''This is simple script to connect to lab router - pynet-rtr2,
and change the logging buffered size on the router.'''
import paramiko, time
from getpass import getpass

ip_addr = '184.105.247.71'
username = 'pyclass'
password = getpass()
timeout = 10
port = 22


def connect_to_host():
    global remote_conn_pre
    remote_conn_pre = paramiko.SSHClient()
    #remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    global add_host_key_policy
    add_host_key_policy = paramiko.AutoAddPolicy
    if add_host_key_policy == False:
        print 'Are you sure you want to accept unknown host key? - Enter y or n'
        if input() == 'y':
            print 'New host key is now accepted.'
            remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if input() == 'n':
            print 'New host key (unknown host key) is now rejected.'
            print 'No conneciton will be established.'
            exit()

    remote_conn_pre.load_system_host_keys()
    remote_conn_pre.connect(ip_addr, username=username, password=password, port=port, timeout=timeout, look_for_keys=False, allow_agent=False)
    print remote_conn_pre.get_transport(), '\n'

    global remote_conn
    remote_conn = remote_conn_pre.invoke_shell()
    outp = remote_conn.recv(5000)
    print '\n', 40 * '*', '\n'
    print 'If prompt received below, you are connected...', '\n', outp
    remote_conn.settimeout(6.0)    ## Wait for the data 6sec
    print 40 * '*'
    remote_conn.send("terminal length 0\n")
    time.sleep(1)
    outp = remote_conn.recv(5000)
    time.sleep(1)


def show_logging_size():
    ''' Send 'show version' to router and display on screen.'''
    remote_conn.send("\n")
    time.sleep(1)
    remote_conn.send('show logging | inc Log Buffer')
    time.sleep(3)
    remote_conn.send("\n")
    time.sleep(1)
    outp = remote_conn.recv(65535)
    time.sleep(3)
    print outp, '\n'


def check_output():
    ''' Verify if there's anything else to receive from the router.'''
    print 80 * '.'
    outp = remote_conn.recv_ready()
    if outp == False:
        print 'No more data is expected from ', ip_addr
    else:
        print "There's still some data to be received from ", ip_addr


def change_logging_buffered_size():
    '''Send 'conf t' and 'logging buffered <size> debugging' commands
    to router.'''
    # Run 'conf t' command on router
    remote_conn.send("\n")
    time.sleep(1)
    remote_conn.send('conf t')
    time.sleep(3)
    remote_conn.send('\n')
    time.sleep(1)
    outp = remote_conn.recv(5000)
    time.sleep(3)
    
    # Run 'logging buffered <size>' command on router
    remote_conn.send("\n")
    time.sleep(1)
    remote_conn.send('logging buffered 20480 debugging')
    time.sleep(3)
    remote_conn.send('\n')
    time.sleep(1)
    outp = remote_conn.recv(65535)
    time.sleep(3)
    print outp, '\n'
    
    # Exit config mode on router to run later 'show logging' command again
    remote_conn.send('\n')
    time.sleep(1)
    remote_conn.send('exit')
    time.sleep(1)
    

### CODE RUN ORDER ###
connect_to_host()
show_logging_size()
check_output()
change_logging_buffered_size()
show_logging_size()
check_output()
