#!/usr/bin/env python
'''
Simple script to connect to pynet_sw3 Arista vEOS switch via jsonrpclib module
'''

import ssl,jsonrpclib, pprint
ssl._create_default_https_context = ssl._create_unverified_context

ip_addr = '184.105.247.74'
port = '443'
username = 'eapi'
password = 'ZZteslaX'

switch_url = 'https://{}:{}@{}:{}'.format(username, password, ip_addr, port)
switch_url = switch_url + '/command-api'
print switch_url
print
remote_connect = jsonrpclib.Server(switch_url)
print remote_connect
print
response = remote_connect.runCmds(1, ['show version'])
print response
print
print
pprint.pprint(response)
