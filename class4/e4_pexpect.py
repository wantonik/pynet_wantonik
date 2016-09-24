#!/usr/bin/env python
'''
Simple script to execute shell command on lab router with Pexpect module.
'''
import pexpect, sys, re
from getpass import getpass

def main():
    ## Define variables
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = 22
    password = getpass()

    ## Set up connection with router
    def connect_to_host():
        global ssh_conn
        ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
        ssh_conn.timeout = 3
        ssh_conn.expect('ssword:')    ## Expects to see line with this string on router
        ssh_conn.sendline(password)   ## We then send the password to log in on router
        ssh_conn.expect('pynet-rtr2#') ## To see the prompt on the server

        ssh_conn.sendline('terminal length 0')    ## Disable 'more' paging
        ssh_conn.expect('pynet-rtr2#')
        print ssh_conn.before
        print ssh_conn.after
   
    def show_run_command():
        # 'show run' before changing 'logging buffered <size> debugging'
        ssh_conn.sendline('show run\n')
        ssh_conn.expect('pynet-rtr2#')
        print ssh_conn.before

    def change_logging_buffered_size():
        # Changing the size of logging buffer
        ssh_conn.sendline('conf t')
        ssh_conn.expect('config')
        ssh_conn.sendline('logging buffered 20480 debugging')
        ssh_conn.expect('config')
        print ssh_conn.before
        print ssh_conn.after
        ssh_conn.sendline('exit')
        ssh_conn.expect('pynet-rtr2#')
        print ssh_conn.before


    ### RUN CODE ORDER ###
    connect_to_host()
    show_run_command()
    change_logging_buffered_size()
    show_run_command()


if __name__ == "__main__":
    main()
