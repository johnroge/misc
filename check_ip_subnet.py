#!/usr/bin/evn python3
"""
Simple script for validating an IP address is within a given subnet
Author: JohRoge
Last Updated: 8/7/2019
version: 1.0
"""

from netaddr import IPNetwork, IPAddress


def main():
    """
    Main block for flow control
    :return: Output results to screen
    """
    instructions()
    address, subnet = get_info()
    check_ip(address, subnet)


def instructions():
    """
    Provide examples
    :return: none
    """
    print('IPv4 address example: 10.3.4.20')
    print('IPv6 address example: 2603:10a6:1200:: ')
    print('\nIPv4 subnet example: 10.3.4.0/16')
    print('IPv6 subnet example: 2603:10a6:1200::/39 ')


def get_info():
    """
    Get user input
    :return: IP Address and subnet info
    """
    # TODO: validate input
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
        print(f'YES: {address} is in {subnet}')
    else:
        print()
        print(f'Sorry, but {address} is not a part of the {subnet} subnet...')


if __name__ == '__main__':
    main()
