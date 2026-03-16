

import netmiko
import jinja2

config = {
    'switch': {
        'hostname': '',
        'credentials': {
            'priv_exec_pw': '',
            'console_pw': '',
            'vty_pw': ''
            },
        'vlans': [
            {'vlan_id': None, 'vlan_name': None}
            ],
        'interfaces': [
            {'mode': 'access', 'start': None, 'stop': None},
            {'mode': 'trunk', 'start': None, 'stop': None},
            {'mode': 'etherchannel', 'start': None, 'stop': None}
        ]
    }
}

def switch_config(config):
    
    # Asking for the hostname of the switch
    while True:
        hostname = input("What is the hostname of the switch?: ").strip()
        if hostname == '':
            print("You cannot have an empty string.").strip()
            return
        else: 
            config['switch']['hostname'] = hostname
            break

    # Asks for confirmation of Priviledged Exec Password 
    while True:
        priv_ask = input("Would you like to have a priviledged EXEC password?\nY/N: ").strip()
        if priv_ask == 'N':
            print("Skipping the Priv Exec password...")
            break
        elif priv_ask == 'Y':
            priv_exec_pw = input("What would you like the EXEC password to be?: ").strip()
            config['switch']['credentials']['priv_exec_pw'] = priv_exec_pw
            break
        else:
            print("Please enter either Y or N.")
            break
    
    # Asks for a console password
    while True:
        console_ask = input("Would you like to have a console password?\nY/N: ").strip()
        if console_ask == 'N':
            print("Skipping the console password...")
            break
        elif console_ask == 'Y':
            console_pw = input("What would you like the console password to be?: ").strip()
            config['switch']['credentials']['console_pw'] = console_pw
            break
        else:
            print("Please enter either Y or N.")
            break
    
    # Asks for a VTY line password
    while True:
        vty_ask = input("Would you like to have a VTY line password?\nY/N: ").strip()
        if vty_ask == 'N':
            print("Skipping the VTY lines password...")
            break
        elif vty_ask == 'Y':
            vty_pw = input("What would you like the VTY password to be?: ").strip()
            config['switch']['credentials']['vty_pw'] = vty_pw
            break
        else:
            print("Please enter either Y or N.")
            break
            
        






def main_menu():
    while True:
        print("Networking AutoConfiguration")
        print("What kind of device are you configuring?")
        print("1. Switch\n2. L3 Switch\n3. Router")
        print("4. Exit")

        choice = input("Please select an option: ").strip()

        if choice == "1":
            switch_config(config)

main_menu()