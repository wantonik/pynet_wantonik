'''
E1:

a) Initialize Django DB:
$ python manage.py makemigrations net_system    # to generate Django DB
$ python manage.py migrate      # to initialize Django DB

a1) Both commands ran from /home/wantonik/DJANGOX/:
(applied_python)[wantonik@ip-172-30-0-4 djproject]$ python manage.py makemigrations net_system
Migrations for 'net_system':
  0001_initial.py:
    - Create model Credentials
    - Create model NetworkDevice
(applied_python)[wantonik@ip-172-30-0-4 djproject]$ python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, contenttypes, net_system, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying net_system.0001_initial... OK
  Applying sessions.0001_initial... OK
(applied_python)[wantonik@ip-172-30-0-4 djproject]$ 

(applied_python)[wantonik@ip-172-30-0-4 djproject]$ cd ..
(applied_python)[wantonik@ip-172-30-0-4 DJANGOX]$ ll
total 4
drwxr-xr-x 4 wantonik wantonik 4096 Nov 18 02:40 djproject
(applied_python)[wantonik@ip-172-30-0-4 DJANGOX]$ 
At this stage we have blank DB.

Our DB is not yet setup fully so the below command won’t return the list of network devices in our environment:
(applied_python)[wantonik@ip-172-30-0-4 djproject]$ python manage.py shell
Python 2.7.12 (default, Sep  1 2016, 22:14:00) 
[GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from net_system.models import NetworkDevice, Credentials
>>> net_devices = NetworkDevice.objects.all()
>>> net_devices
[]
>>> quit

a2) Add the seven NetworkDevice objects and two Credentials objects into your database.
a) We need to run ./load_devices.py script (I also added #!/usr/bin/env python at the top of the script):
(applied_python)[wantonik@ip-172-30-0-4 net_system]$ python load_devices.py 
(<NetworkDevice: pynet-rtr2>, True)
(<NetworkDevice: pynet-sw1>, True)
(<NetworkDevice: pynet-sw2>, True)
(<NetworkDevice: pynet-sw3>, True)
(<NetworkDevice: pynet-sw4>, True)
(<NetworkDevice: juniper-srx>, True)
(applied_python)[wantonik@ip-172-30-0-4 net_system]$ 

a3) Run load_credentials.py script:
(applied_python)[wantonik@ip-172-30-0-4 net_system]$ vim load_credentials.py 
(applied_python)[wantonik@ip-172-30-0-4 net_system]$ python load_credentials.py 
(<Credentials: pyclass>, True)
(<Credentials: admin1>, True)
(applied_python)[wantonik@ip-172-30-0-4 net_system]$ 

Note, that the permissions don’t allow you to run these scripts with ./<script> but with python <script> command – unless you will change the permissions from 644 to 755 or so.

A4) Once the above are completed successfully we do the following steps:
After this initialization, you should be able to do the following (from the ~/DJANGOX/djproject directory):
$ python manage.py shell

>>> from net_system.models import NetworkDevice, Credentials
>>> net_devices = NetworkDevice.objects.all()
>>> net_devices
[<NetworkDevice: pynet-rtr1>, <NetworkDevice: pynet-sw1>, <NetworkDevice: pynet-sw2>, <NetworkDevice: pynet-sw3>, <NetworkDevice: pynet-sw4>, <NetworkDevice: juniper-srx>, <NetworkDevice: pynet-rtr2>]

>>> creds = Credentials.objects.all()
>>> creds
[<Credentials: pyclass>, <Credentials: admin1>]

Below is the output – all went successfully:
(applied_python)[wantonik@ip-172-30-0-4 djproject]$ python manage.py shell
Python 2.7.12 (default, Sep  1 2016, 22:14:00) 
[GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from net_system.models import NetworkDevice, Credentials
>>> net_devices = NetworkDevice.objects.all()
>>> net_devices
[<NetworkDevice: pynet-rtr1>, <NetworkDevice: pynet-rtr2>, <NetworkDevice: pynet-sw1>, <NetworkDevice: pynet-sw2>, <NetworkDevice: pynet-sw3>, <NetworkDevice: pynet-sw4>, <NetworkDevice: juniper-srx>]
>>> 
>>> 
>>> creds = Credentials.objects.all()
>>> creds
[<Credentials: pyclass>, <Credentials: admin1>]
>>> 
At this stage both – devices and credentials – were loaded to our SQLite DB successfully.

Notice, that now I can iterate over the devices in our network:
>>> for a_device in net_devices:
...     print a_device.device_name
... 
pynet-rtr1
pynet-rtr2
pynet-sw1
pynet-sw2
pynet-sw3
pynet-sw4
juniper-srx
>>> 

Also, I can grab one of the network devices and query its details related to NetworkDevice table:
>>> cisco = net_devices[0]
>>> cisco
<NetworkDevice: pynet-rtr1>
>>> cisco.ip_address
u'184.105.247.70'
>>> cisco.model
>>> cisco.vendor
>>> cisco.username
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'NetworkDevice' object has no attribute 'username'
>>> cisco.device_name
u'pynet-rtr1'
>>> 
Notice, that cisco.username returned error, as this field is not defined in NetworkDevice class in models.py file. It is defined in Credentials class.
Also notice, that there’s no relationship between Credentials and NetworkDevice objects – there’s no mapping between them – this is done by means of .ForeignKey(). This is point b) below.

b) Update the NetworkDevice objects such that each NetworkDevice links to the correct Credentials.
Below we check what credentials are defined in our DB:
>>> creds
[<Credentials: pyclass>, <Credentials: admin1>]
>>> 
We know that two Cisco routers and Juniper device require ‘pyclass’ credentials and 4 Arista switches require ‘admin1’ credentials. Therefore we have to now link those groups of network devices to their corresponding credentials:
>>> 
>>> std_creds = creds[0]
>>> std_creds
<Credentials: pyclass>
>>> creds[0]
<Credentials: pyclass>
>>> 
>>> arista_creds = creds[1]
>>> arista_creds
<Credentials: admin1>
>>> creds[1]
<Credentials: admin1>
>>> 
This is 1st step, on how we link device groups with their corresponding credentials!
2nd step is to iterate over devices again and construct IF statement, which will do the following:
>>> 
>>> a_device.credentials = arista_creds
>>> a_device.credentials = std_creds
>>> 
>>> for a_device in net_devices:
...     if 'pynet-sw' in a_device.device_name:
...         a_device.credentials = arista_creds
...     else:
...         a_device.credentials = std_creds
...     a_device.save()
... 
>>>

Now, let’s iterate through these to check if all is linked correctly:
>>> 
>>> for a_device in net_devices:
...     print a_device, a_device.credentials
... 
pynet-rtr1 pyclass
pynet-rtr2 pyclass
pynet-sw1 admin1
pynet-sw2 admin1
pynet-sw3 admin1
pynet-sw4 admin1
juniper-srx pyclass
>>> 
All looks goog – groups of devices are associated/linked with correct credentials. The link between NetworkDevice and Credentials classes is now established with .ForeignKey.

END
'''
