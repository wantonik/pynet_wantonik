#!/usr/bin/env python
'''Use Netmiko to connect to each of the devices in the database. Execute
'show version' on each device. Record the amount of time required to do this.'''

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()
    
    start_time = datetime.now()    
    creds = Credentials.objects.all()
    net_devices = NetworkDevice.objects.all()
    for a_device in net_devices:
        device_type = a_device.device_type
        port = a_device.port
        secret = ''
        ip = a_device.ip_address
        creds = a_device.credentials
        username = creds.username
        password = creds.password
        remote_conn = ConnectHandler(device_type=device_type, port=port,
                                    ip=ip, username=username, password=password)
        print 'Establishing connection via Netmiko to all net devices ', '\n', remote_conn
        print 80 * '_'
        print remote_conn.send_command_expect('show version')
        #break ## Use this statement to run the command only on one device
        
        elapsed_time = datetime.now() - start_time
        print 'Elapsed time: {}'.format(elapsed_time)
 

if __name__ == "__main__":
    main()
