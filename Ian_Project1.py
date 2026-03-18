# Coding project by Ian Dube
# For Funnsies but also efficiency


import netmiko
import jinja2
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S %d %b %Y")

config = {
    'switch': {
        'hostname': '',
        'clock_set': current_time,
        'banner_motd': None,
        'ip_lookup': None,
        'credentials': {
            'priv_exec_pw': '',
            'console_pw': '',
            'vty_pw': ''
            },
        'logging synchronous': None,
        'vlans': [],
        'interfaces range': [],
        'interfaces singular': [],
        'password_encryption': None,
    },
    
    'L3 Switch': {
        'hostname:': '',
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

    # Code to Update the clock
    while True:
        update_confirm = input("Would you like to update the current time? \ny/n: ").lower()
        if update_confirm == 'y':
            current_time = datetime.now().strftime("%H:%M:%S %d %b %Y")
            print("Updating to current time...")
            config['switch']['clock_set'] = current_time
            print(config)
            break
        elif update_confirm == 'n':
            print("Skipping clock update...")
            break
        else:
            print("Please Input either y/n")
            continue

    # Code to add a banner motd
    while True:
        banner_confirm = input("Would you like to add a banner motd?\n y/n: ").lower()
        if banner_confirm == 'y':
            banner_motd = input("What would you like the banner MOTD to be?\nFormat inbetween hashtags #___#\n")
            config['switch']['banner_motd'] = banner_motd
            break
        elif banner_confirm == 'n':
            print("Skipping banner motd...")
        else:
            print("Please enter y/n.")
            continue

    # Asks for confirmation of Priviledged Exec Password 
    while True:
        priv_ask = input("Would you like to have a priviledged EXEC password?\ny/n: ").strip().lower()
        if priv_ask == 'n':
            print("Skipping the Priv Exec password...")
            break
        elif priv_ask == 'y':
            priv_exec_pw = input("What would you like the EXEC password to be?: ").strip()
            config['switch']['credentials']['priv_exec_pw'] = priv_exec_pw
            break
        else:
            print("Please enter either Y or n.")
            continue
    
    # Asks for a console password
    while True:
        console_ask = input("Would you like to have a console password?\ny/n: ").strip().lower()
        if console_ask == 'n':
            print("Skipping the console password...")
            break
        elif console_ask == 'y':
            console_pw = input("What would you like the console password to be?: ").strip()
            config['switch']['credentials']['console_pw'] = console_pw
            break
        else:
            print("Please enter either Y or N.")
    
    # Asks for a VTY line password
    while True:
        vty_ask = input("Would you like to have a VTY line password?\ny/n: ").strip().lower()
        if vty_ask == 'n':
            print("Skipping the VTY lines password...")
            break
        elif vty_ask == 'y':
            vty_pw = input("What would you like the VTY password to be?: ").strip()
            config['switch']['credentials']['vty_pw'] = vty_pw
            break
        else:
            print("Please enter either Y or n.")
            continue
    
    # Asks for the vlan count
    while True:
        try:
            number_of_vlans = int(input("Please enter a NUMBER of vlans you would like to create: "))
            if number_of_vlans < 1:
                print("Please enter a number above 0.")
                continue
            break
        except ValueError:
            print("Please enter an integer.")
   
    # Collects the vlans
    vlans = []
    for i in range(number_of_vlans):
        while True:
            try:
                vlan_id = int(input(f"Please enter the VLAN ID For VLAN # {i+1}: "))
                break
            except ValueError:
                print("Please enter a proper vlan ID")
        
        vlan_name = input(f"Please enter a name for VLAN ID {vlan_id}: ")
        vlan_ip = None
        vlan_ip_conf = input(f"Would you like to input an IP address for VLAN ID {vlan_id}? \ny/n: ").lower()
        if vlan_ip_conf == 'n':
            print("Skipping vlan IP...")   
        elif vlan_ip_conf == 'y':
            vlan_ip = input("Please enter the IP address in this format: x.x.x.x x.x.x.x\n")
        else:
            print("Please input either Y/n")
        vlans.append({
            'vlan_id': vlan_id,
            'vlan_name': vlan_name,
            'vlan_ip': vlan_ip
        })
        config['switch']['vlans'] = vlans


    # Interfaces mode Access 
    while True:
        interf_acc_quest = input("Would you like to configure access ports for this switch?\ny/n: ").lower()
        if interf_acc_quest == 'n':
            print("Skipping interface access ports...")
            break
        elif interf_acc_quest == 'y':
            port_range_conf = input("Are you configuring a range of ports? or single port? Type: \nrange/single: ")
            if port_range_conf == 'range':
                port_start = input("What is the START range of ports you would like to configure? (Format: G1/0/1)")
                port_end = input("What is the END port you would like to configure? (Format: Single integer: 1)")
                config['switch']['interfaces range'].append({
                    'mode': 'access',
                    'port_start': port_start,
                    'port_end': port_end
                })
            elif port_range_conf == 'single':
                port_num = input("Please input the singular port number in this format: G1/0/1\n")
                config['switch']['interfaces singular'].append({
                    'mode': 'access',
                    'port_num': port_num
                })
        else: 
            try:
                print("Please enter a valid option")
            except: ValueError
            break
    
    


def main_menu():
    while True:
        print("Networking AutoConfiguration")
        print("What kind of device are you configuring?")
        print("1. Switch\n2. L3 Switch\n3. Router")
        print("4. Print Configurations")
        print("5. Exit")

        choice = input("Please select an option: ").strip()

        if choice == "1":
            switch_config(config)
        
        elif choice == "4":
            print(config)
main_menu()
