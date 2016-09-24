#!/usr/bin/env python
'''Script based on Paramiko-Part2 video from Kirk Byers course.
'''
import paramiko
from getpass import getpass

ip_addr = '184.105.247.71'
username = 'pyclass'
password = getpass()
port = 22

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.load_system_host_keys()
remote_conn_pre.connect(ip_addr, username=username, password=password, port=port, look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
outp = remote_conn.recv(5000)
print outp
