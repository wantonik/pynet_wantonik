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
    try:
        ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
        ssh_conn.timeout = 3
        ## Expects to see line with 'ssword' string on router
        ssh_conn.expect('ssword:')
        ## We then send the password to log in on router
        ssh_conn.sendline(password)
        ## To see the prompt on router
        ssh_conn.expect('pynet-rtr2#')
        
        ## Execute 'show ip int brief' command to router
        ssh_conn.sendline('show ip int brief\n')
        ssh_conn.expect('pynet-rtr2#')
        print ssh_conn.before

        ## Disable 'more' paging
        ssh_conn.sendline('terminal length 0')
        ssh_conn.expect('pynet-rtr2#')
        print ssh_conn.before
        print ssh_conn.after
    
    ## Catching timeout and other errors from the above section
    except pexpect.TIMEOUT:
        print 'Found timeout or other error - check your code: variables, args.'

    host_name = ssh_conn.before
    host_name = host_name.strip()
    prompt = host_name + ssh_conn.after
    prompt = prompt.strip()

if __name__ == "__main__":
    main()
