from socket import socket
import psutil
from socket import AF_INET, AF_INET6


def get_network_info():

    interfaces = psutil.net_if_addrs()
    networks = []

    for interface, stats in interfaces.items():
        mac = [stat.address for stat in stats if stat.family == psutil.AF_LINK]
        ip = [stat.address for stat in stats if stat.family == AF_INET]
        ip6 = [stat.address for stat in stats if stat.family == AF_INET6]
        networks.append({"nice_name": interface, "mac": mac, "ip": ip, "ip6": ip6})

    return networks