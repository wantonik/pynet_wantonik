#!/usr/bin/env python
'''
Use threads and Netmiko to connect to each of the devices in DB. Execute
'show version' on each device. Record the amount of time required to do this.
'''

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django
import threading
import time

def main():
    django.setup()
    start_time = datetime.now()    
    
    # Establish connection and run 'show version'
    net_devices = NetworkDevice.objects.all()
    creds = Credentials.objects.all()
    
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
        print 
        show_version = remote_conn.send_command_expect('show version')
        #print show_version
    
        # Use threads
        my_thread = threading.Thread(target=None, args=(a_device,))
        my_thread.start()

        main_thread = threading.currentThread()
        for some_thread in threading.enumerate():
            if some_thread != main_thread:
                print some_thread
                some_thread.join() 
    
    elapsed_time = datetime.now() - start_time
    print 'Elapsed time: {}'.format(elapsed_time)
 
if __name__ == "__main__":
    main()
