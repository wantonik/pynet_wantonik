#!/usr/bin/env python
'''Simple script to add VLAN (vlanid and name). Your script should first
check that the VLAN ID is available and only add the VLAN if it doesn't
already exist. Use VLAN IDs between 100 and 999.
Use argparse module for argument processing.

You should be able to call the script from the command line as follows:
python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.
python eapi_vlan.py --remove 100        # remove VLAN100'''

import pyeapi, argparse
from pprint import pprint

if __name__ == "__main__":

    pynet_sw3 = pyeapi.connect_to('pynet-sw3')
    print pynet_sw3, '\n'

    def show_current_vlan_config():
        '''The below section refers to a list, so no .keys, .values, .items methods apply'''
        global show_vlan
        show_vlan = pynet_sw3.enable('show vlan')
        show_vlan = show_vlan[0]['result']['vlans']
        #print 'Dispaly keys: ', show_vlan.keys(), '\n'    # tell me how many keys is in this dictionary
        pprint(show_vlan)
        print 40 * '2', '\n', '\n'
    show_current_vlan_config()


    def CLI_arguments():
        '''Argparse section for entering arguments from CLI'''
        parser = argparse.ArgumentParser(description='Add or remove Vlan depending on the option used')
        parser.add_argument('--name', help='Configure new Vlan', action='store', dest='vlan_name', type=str)
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


    def add_vlan_config():
        for vlan in show_vlan.keys():
            if int(vlan) == vlan_id:
                print 80 * '!'
                print 20 * '!', 'VlanID {} is already configured.'.format(vlan_id), 20 * '!'
                choice = input('Type 0 to ignore action or 1 to remove vlan: ')
                choice = int(choice)
                if choice == 0:
                    print 'Exiting...'
                    exit()
                if choice == 1:
                    delete_vlan = ['configure terminal', 'no vlan ' + str(vlan_id), 'name ' + str(vlan_name), 'write memory']
                    outp = pynet_sw3.config(delete_vlan)
                    print 'REMOVING VLAN: ', str(outp)
                else:
                    exit()
            if int(vlan) != vlan_id:
                add_vlan = ['configure terminal', 'vlan ' + str(vlan_id), 'name ' + str(vlan_name), 'write memory']
                outp = pynet_sw3.run_commands(add_vlan)
                print 'ADDING NEW VLAN: ', str(outp)
    add_vlan_config()

#    def remove_vlan_config():
#        for vlan in show_vlan.keys():
#            if int(vlan) == vlan_id:
#                print 80 * '!'
#                print 20 * '!', 'VlanID {} is already configured.'.format(vlan_id), 20 * '!'
#                print 'You can now remove it from current configuration.'
#                delete_vlan = ['configure terminal', 'no vlan ' + str(vlan_id), 'name ' + str(vlan_name), 'write memory']
#                outp = pynet_sw3.config(delete_vlan)
#                print 'EXECUTING: ', str(outp)
#                exit()
#    remove_vlan_config()
