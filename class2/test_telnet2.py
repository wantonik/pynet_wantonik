#!/usr/bin/env python
import telnetlib, time, socket, sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

# Creating a function which establishes remote telnet connection
def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

# Creted a login function to connect to rtr1
def login(remote_conn, username, password):
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until('ssword:', TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

# Creating functin for telnet connection with exception handling
def telnet_connect(ip_addr):
# also as arguments there should be here TELNET_PORT and TELNET_TIMEOUT, so that these values are not hardcoded.
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    # return connection if it can be established
    except socket.timeout:
    # if connection fails, display the below message
        sys.exit("Connection timed-out")    # sys.exit() to exist the program

def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    password = '88newclass'
    
    remote_conn = telnet_connect(ip_addr)    # added line with this variable
    output = login(remote_conn, username, password)
    time.sleep(1)
    output = remote_conn.read_very_eager()
    output = send_command(remote_conn, 'terminal length 0')
    output = send_command(remote_conn, 'show version')
    print output
    
    remote_conn.close()

if __name__ == "__main__":
    main()
