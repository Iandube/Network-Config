import netmiko
import jinja2
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S %d %b %Y")

config = {
    'switch': {
        'hostname': '',
        'clock set': current_time,
        'banner motd': '',
        'credentials': {
            'priv_exec_pw': '',
            'console_pw': '',
            'vty_pw': ''
            },
        'vlans': [],
        'interfaces range': [],
        'interfaces singular': [],
    }
}
print(config)

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
            continue
    
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
            continue
    
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
            continue
    
    # Asks for the vlan count
    while True:
        try:
            number_of_vlans = int(input("Please enter a NUMBER of vlans you would like to create: ")).strip()
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
                vlan_id = int(input(f"Please enter the VLAN ID For VLAN # {i+1}: ").strip())
                break
            except ValueError:
                print("Please enter a proper vlan ID")
        
        vlan_name = input(f"Please enter a name for VLAN ID{vlan_id}: ").strip()
        vlans.append({
            'vlan_id': vlan_id,
            'vlan_name': vlan_name
        })
        config['switch']['vlans'] = vlans


    # Interfaces mode start
    while True:
        interf_acc_quest = input("Would you like to configure access ports for this switch?\nY/N: ")
        if interf_acc_quest == 'N':
            print("Skipping interface access ports...").strip()
            break
        elif interf_acc_quest == 'Y':
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
                config['switch']['interface singular'].append({
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
        print("4. Exit")

        choice = input("Please select an option: ").strip()

        if choice == "1":
            switch_config(config)

main_menu()