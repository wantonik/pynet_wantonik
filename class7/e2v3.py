#!/usr/bin/env python
'''Simple script to add VLAN (vlanid and name). The script first checks that
the VLAN ID is available and only adds the VLAN if it doesn't already exist.
Use VLAN IDs between 100 and 999. Use argparse module for argument processing.
Script shows Arista vlan configuration before and after the change.

You should be able to call the script from the command line as follows:
python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.
python eapi_vlan.py --remove 100        # remove VLAN100'''

import pyeapi, argparse
from pprint import pprint

print 'BEFORE THE CHANGE...'
def show_current_vlan_config():
    '''The below section refers to a list, so no .keys, .values, .items methods apply'''
    pynet_sw3 = pyeapi.connect_to('pynet-sw3')
    global show_vlan
    show_vlan = pynet_sw3.enable('show vlan')
    show_vlan = show_vlan[0]['result']['vlans']
    pprint(show_vlan)
    print '\n'
show_current_vlan_config()


def check_vlan_exists(pynet_sw3, vlan_id):
    '''Check if the given VLAN exists
    Return either vlan_name or False'''
    vlan_id = str(vlan_id)
    cmd = 'show vlan id {}'.format(vlan_id)
    try:
        check_vlan = show_vlan
        return check_vlan[vlan_id]['name']
    except (pyeapi.eapilib.CommandError, KeyError):
        pass
    return False


def configure_vlan(pynet_sw3, vlan_id, vlan_name=None):
    '''Add the given vlan_id to the switch. Set the vlan_name (if provided)
    Note, if the vlan already exists, then this will just set the vlan_name'''
    command_str1 = 'vlan {}'.format(vlan_id)
    cmd = [command_str1]
    if vlan_name is not None:
        command_str2 = 'name {}'.format(vlan_name)
        cmd.append(command_str2)
    return pynet_sw3.config(cmd)


def main():
    '''Add/remove vlans from Arista switch in an idempotent manner'''
    pynet_sw3 = pyeapi.connect_to('pynet-sw3')
    print pynet_sw3, '\n'

    def CLI_arguments():
        '''Argparse section for entering arguments from CLI'''
        parser = argparse.ArgumentParser(description='Add or remove Vlan')
        parser.add_argument('--name', help='Name new Vlan', action='store', dest='vlan_name', type=str)
        parser.add_argument('--remove', help='Remove the given Vlan ID', action='store_true')
        parser.add_argument('vlan_id', help='Specify Vlanid i.e. Vlan number', action='store', type=int)
        cli_args = parser.parse_args()
        global vlan_id
        vlan_id = cli_args.vlan_id
        global vlan_name
        vlan_name = cli_args.vlan_name
        global remove
        remove = cli_args.remove
    CLI_arguments()

    
    # Check if VLAN already exists
    print '\n', 80 * '#', '\n'
    check_vlan = check_vlan_exists(pynet_sw3, vlan_id)

    # check if action is remove or add    
    if remove:
        if check_vlan:
            print "VLAN exists, removing it"
            command_str = 'no vlan {}'.format(vlan_id)
            pynet_sw3.config([command_str])
        else:
            print "VLAN does not exist, no action required"
    else:
        if check_vlan:
            if vlan_name is not None and check_vlan != vlan_name:
                print "VLAN already exists, setting VLAN name"
                configure_vlan(pynet_sw3, vlan_id, vlan_name)
            else:
                print "VLAN already exists, no action required"
        else:
            print "Adding VLAN including vlan_name (if present)"
            configure_vlan(pynet_sw3, vlan_id, vlan_name)
    print '\n', 80 * '#', '\n'
    
    
    # Check if the change has been applied
    print 'AFTER THE CHANGE...'
    show_current_vlan_config()


if __name__ == "__main__":
    main()
