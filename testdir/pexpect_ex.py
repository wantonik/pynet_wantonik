#!/usr/bin/env python
'''This is based on Pexpect Video from Kirk's course.'''
import pexpect, sys
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
    print ssh_conn.before    ## This will print the output between both .expect lines
    print ssh_conn.after    ## Will match expected '#' sign from the above line
    
    router_name = ssh_conn.before
    router_name = router_name.strip()
    prompt = router_name + ssh_conn.after
    prompt = prompt.strip()

if __name__ == "__main__":
    main()
