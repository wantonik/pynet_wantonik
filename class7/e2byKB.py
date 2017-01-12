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


def show_current_vlan_config(arista_conn):
    # The below section refers to a list, so no .keys, .values, .items methods apply
    show_vlan = arista_conn.enable('show vlan')
    print 'What is the data type: ', type(show_vlan)
    print 'How many elements it has: ', len(show_vlan)
    pprint(show_vlan)
    print 40 * '1', '\n'

    # ['vlans'] section
    show_vlan = show_vlan[0]['result']['vlans']
    print 'What is the data type: ',type(show_vlan)    # tell me what data type it is
    print 'How many elements it has: ', len(show_vlan)    # tell me how many elements is in this data type
    print 'Dispaly keys: ', show_vlan.keys(), '\n'    # tell me how many keys is in this dictionary
    pprint(show_vlan)
    print 40 * '2', '\n', '\n'
    return show_vlan


def vlan_config_change(arista_conn, vlan_id, vlan_name=""):
    show_vlan = show_current_vlan_config(arista_conn)
    for vlan in show_vlan.keys():
        if int(vlan) == vlan_id:
            print 80 * '!'
            print 20 * '!', 'VlanID {} is already configured.'.format(vlan_id), 20 * '!'
            print 80 * '!', '\n'
            print 'Do you want to remove the existing Vlan? - y/n'
            if raw_input() == 'y':                
                delete_vlan = ['configure terminal','no vlan ' + str(vlan_id),'name ' + str(vlan_name),'write memory']
                outp = arista_conn.config(delete_vlan)
                print 'EXECUTING: ', str(outp)
            if raw_input() == 'n':    ## This part doesnt work - program is not exiting.
                print 'Vlan exists, so nothing to do here'
                exit()
        else:
            add_vlan = ['configure terminal','vlan ' + str(vlan_id),'name ' + str(vlan_name),'write memory']
            outp = arista_conn.run_commands(add_vlan)
            print 'EXECUTING: ', str(outp)


def main():
    # Arista switch definition
    pynet_sw3 = pyeapi.connect_to('pynet-sw3')
    print pynet_sw3, '\n'

    parser = argparse.ArgumentParser(description='Add or remove Vlan depending on the option used')
    parser.add_argument('--name', help='Configure new Vlan', action='store', dest='vlan_name', type=str)
    parser.add_argument('--remove', help='Remove the given Vlan ID', action='store_true')
    parser.add_argument('vlan_id', help='Specify Vlanid i.e. Vlan number', action='store', type=int)

    cli_args = parser.parse_args()
    vlan_id = cli_args.vlan_id
    vlan_name = cli_args.vlan_name
    remove = cli_args.remove

    show_current_vlan_config(pynet_sw3)
    vlan_config_change(pynet_sw3, vlan_id, vlan_name)

if __name__ == "__main__":
    main()
