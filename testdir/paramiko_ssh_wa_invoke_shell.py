import paramiko, time
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
print 'If prompt received, you are connected: ', '\n', outp

# For more data wait 6 seconds
remote_conn.settimeout(6.0)
print 'Timeout set is: ', remote_conn.gettimeout()

print 20 * '*'
outp = remote_conn.send("\n")
outp = remote_conn.send("terminal length 0\n")
outp = remote_conn.recv(65535)
time.sleep(5)
print outp
time.sleep(5)

print 20 * '-'
outp = remote_conn.send("\n")
outp = remote_conn.send("show version")
outp = remote_conn.send("\n")
outp = remote_conn.recv(65535)
time.sleep(5)
print outp
time.sleep(5)
