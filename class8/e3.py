#!/usr/bin/env python
'''
Create two new test NetworkDevices in the database. Use both direct object creation
and the .get_or_create() method to create the devices.
'''

from net_system.models import NetworkDevice, Credentials
import django

net_devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()   # not really needed in this script

# Listing all network devices, their type and their vendor
def list_all_devices():
    print '\n', 'Listing all devices with their: \device name, device type and device vendor...'
    for a_device in net_devices:
        print a_device.device_name, 2 * '|', a_device.device_type, 2 * '|', a_device.vendor
        print '...End of listing', '\n'
list_all_devices()
print 40 * '.'

# A function to add 2 new devices to existing network using two different methods
def add_new_device():
    django.setup()

    wanet_rtr3 = NetworkDevice(
        device_name='wanet-rtr3',
        device_type='cisco_ios',
        ip_address='184.105.247.90',
        port=22,
    )
    wanet_rtr3.save()

    wanet_rtr4 = NetworkDevice.objects.get_or_create(
        device_name='wanet-rtr4',
        device_type='cisco_ios',
        ip_address='184.105.247.91',
        port=22,
    )
add_new_device()
print 40 * '-'

# Checking if new devices have been created and added in DB
print 'See below if the devices you specified are now added in your network: '
net_devices = NetworkDevice.objects.all()   #as suggested by Kirk to list new devices too
list_all_devices()
