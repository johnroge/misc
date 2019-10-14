#!/usr/bin/evn python3
"""
Simple script for validating an IP address is within a given subnet
Author: JohRoge
Last Updated: 8/7/2019
version: 1.1
Notes: 1.1 creating simple user menu and looking to add new features
"""

from netaddr import IPNetwork, IPAddress


def main():
    """
    Main block for flow control; may need to create a better menu soon
    :return: Output results to screen
    """
    # show user instructions, get their info and then show results
    instructions()
    address, subnet = get_info()
    check_ip(address, subnet)
    get_ip_range(subnet)

    # now give user chance to exit or try another ip/range
    exit_menu = user_menu()
    if exit_menu is True:
        main()
    else:
        raise SystemExit


def instructions():
    """
    Provide user examples
    :return: none
    """
    print('Examples')
    print('*' * 60)
    print('IPv4 address: 10.3.4.20')
    print('IPv4 subnet: 10.3.4.0/16')
    print('IPv6 address: 2603:10a6:1200:: ')
    print('IPv6 subnet: 2603:10a6:1200::/39 ')
    print('*' * 60)


def user_menu():
    """
    create user menu for exit and try another subnet
    :return: True or False
    """
    print()
    print()
    print()
    user_input = input('Please R to check another IP, any other key'
                       ' to exit: ')
    user_input = user_input.lower()
    if user_input == 'r':
        return True
    else:
        return False


def get_info():
    """
    Get user input
    :return: IP Address and subnet info
    """
    print()
    address = input('Please enter ip address: ')
    subnet = input('Please enter subnet: ')

    return address, subnet


def check_ip(address, subnet):
    """
    Check if address in given subnet
    :param address: IP address
    :param subnet: IP subnet
    :return: Results of test
    """
    if IPAddress(address) in IPNetwork(subnet):
        print()
        print(f'YES: {address} is in {subnet} subnet!')
    else:
        print()
        print(f'*** {address} is not in the {subnet} subnet ***')


def get_ip_range(subnet):
    """
    Take user subnet and list out logical range
    :param subnet: subnet range provided by user
    :return: n/a - show result of subnet check
    """
    ip_info = IPNetwork(subnet)

    print()
    print(f'Range for the {subnet} subnet is:\n {ip_info.network} - '
          f'{ip_info.broadcast}')


if __name__ == '__main__':
    main()
