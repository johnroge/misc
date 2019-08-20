#!/usr/bin/env python3
"""
Get basic info from an F5 device
Author: JohnR
Last Touched: 8/19/2019
Version .01
"""
from f5.bigip import ManagementRoot


def main():
    """
    basic flow control, set some common variables
    :return: device info
    """
    partition = 'Common' # not sure where or what this is used for
    login, pwd, device = get_device_data()
    mgmt = ManagementRoot(login, pwd, device)
    ltm = mgmt.tm.ltm
    pools = ltm.pools.get_collection()
    nodes = ltm.nodes.get_collection()
    display_nodes(nodes)
    display_pools(pools)
    virtuals = ltm.virtuals.get_collection()
    display_virtuals(virtuals)


def get_device_data():
    """
    get device info from user
    :return: tuple of user input
    """
    user = input('Username: ')
    password = input('Password: ')
    device_name = input('FQDN or IP of device: ')

    return user, password, device_name


def display_nodes(nodes):
    """
    Print out nodes and associated IPs
    :param nodes: node collection
    :return: None
    """
    for node in nodes:
        print(f'{node.name} has an IP address of {node.address}.')


def display_pools(pools):
    """
    Display pool info
    :param pools: pools collection
    :return: None
    """
    for pool in pools:
        # print(pool.raw)  # If you want to learn about the objects
        print(pool.name)


def display_virtuals(virtuals):
    """
    Display virtuals
    :param virtuals: virtuals collection
    :return: None
    """
    for virtual in virtuals:
        print(f'VS {virtual.name} enabled? {virtual.enabled}')


"""
# code for checking specific nodes
my_node = 'TESTNODE5'
test = ltm.nodes.node.exists(partition=partition, name=my_node)
print("Is {} on the F5? {}".format(my_node, test))

# Is my node in a pool?
for pool in ltm.pools.get_collection():
    # Take note of how this call works
    for member in pool.members_s.get_collection():
        if my_node in member.name:
            print("{} is in the pool {}".format(my_node, pool.name))

"""

if __name__ == '__main__':
    main()