#!/usr/bin/env python
'''This is based on Pexpect Video from Kirk's course.
This version is with catching timeouts'''
import pexpect, sys, re
from getpass import getpass

def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = 22
    password = getpass()
    
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #ssh_conn.logfile = sys.stdout ## requires sys module to import
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')    ## Expects to see line with this string on router
    ssh_conn.sendline(password)   ## We then send the password to log in on router
    
    ssh_conn.expect('#')    ## Now, we expect to see the prompt on the router
    
    ssh_conn.sendline('show ip int brief')    ## Send a command to router
    ssh_conn.expect('#')    ## We expect to see '#' prompt on the router
    #print ssh_conn.before    ## Print the output between last .expect lines
     
    ssh_conn.sendline('terminal length 0')    ## Disable 'more' paging
    ssh_conn.expect('#')    ## Expecting to see '#' prompt on the router
    
    ssh_conn.sendline('show version')    ## Another command ran on router
    ssh_conn.expect('pynet-rtr2#')    ## Expecting to see the full router prompt
    #print ssh_conn.before    ## Print the output between last .expect lines

    try:
        ssh_conn.sendline('show version')
        ssh_conn.expect('zzz')  ## This regex will not be found, hence timeout of 3s
    except pexpect.TIMEOUT:
        print 'Found timeout'

    router_name = ssh_conn.before
    router_name = router_name.strip()
    prompt = router_name + ssh_conn.after
    prompt = prompt.strip()

if __name__ == "__main__":
    main()
