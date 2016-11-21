#!/usr/bin/env python
'''
Remove the two objects (devices) created in the exercise 3 (e3.py) from the database.
'''

from net_system.models import NetworkDevice, Credentials
import django

net_devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

# Listing all network devices, their type and their vendor
def list_all_devices():
    '''Notice, device_type and vendor fields are not required for this script to work.
    It only gives you better understanding of the devices in your network. '''
    
    print '\n', 'Listing all devices with their: \device name, device type and device vendor...'
    for a_device in net_devices:
        print a_device.device_name, 2 * '|', a_device.device_type, 2 * '|', a_device.vendor

list_all_devices()
print 40 * '_', '\n', '\n'


# A function to remove 2 devices from the network/DB created in e3.py
def del_a_device():
    django.setup()
    net_devices = NetworkDevice.objects.all()

    for a_device in net_devices:
        #print type(a_device.device_name)
        if 'wanet' in a_device.device_name:
            a_device.delete()
            print 'Device %s has been now deleted!' % a_device
        else:
            pass #exit()
del_a_device()

# Checking if new devices have been deleted now from DB
print '\n', 'See below if the devices you specified are now removed from your network: '
net_devices = NetworkDevice.objects.all()
list_all_devices()
