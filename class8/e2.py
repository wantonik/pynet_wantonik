#!/usr/bin/env python
'''
Set the vendor field of each NetworkDevice to the appropriate vendor.
Save this field to the database.
'''
from net_system.models import NetworkDevice, Credentials
import django

net_devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

# Listing all network devices, their type and if they have vendor specified already
print '\n', 'Listing device name, device type and device vendor...'
for a_device in net_devices:
    print a_device.device_name, 2 * '|', a_device.device_type, 2 * '|', a_device.vendor

for a_device in net_devices:
    if 'cisco' in a_device.device_type:
        a_device.vendor = 'cisco'
    elif 'arista' in a_device.device_type:
        a_device.vendor = 'arista'
    else:
        a_device.vendor = 'juniper'
    a_device.save()
print '\n', 'Saving changes to DB now - not verbose'

# Checking if the changes have been made in Django
print '\n', 'Listing device name, device type and device vendor...'
for a_device in net_devices:
    print "{} || {} || {}".format(a_device.device_name, a_device.device_type, a_device.vendor)
    #print a_device.device_name, 2 * '|', a_device.device_type, 2 * '|', a_device.vendor
