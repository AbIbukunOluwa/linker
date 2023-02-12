#!/usr/bin/env python3

import scapy.all as scapy
import colorama
import argparse
import subprocess
from colorama import Fore, Style


colorama.init(autoreset=True)


def user_collector():
    user = argparse.ArgumentParser()
    user.add_argument("-i", "--ip", dest="address", help="Ip range to scan")
    args = user.parse_args()
    if not args.address:
        user.error(f"{Fore.RED}{Style.BRIGHT}[-] Kindly specify the ip range to scan")
    return args


def get_ip_range(ip):
    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combine_packet = broadcast/request
    online_addresses = scapy.srp(combine_packet, verbose=False, timeout=1)[0]
    # print(online_addresses.show())
    return online_addresses


def sift_ip(responded):
    for online_ips in responded:
        listened = online_ips[1].psrc
        print(f"{Fore.YELLOW}{Style.BRIGHT}\n\n----------------------------------")
        print(f"{Fore.CYAN}{Style.BRIGHT}Scanning " + Fore.CYAN + Style.BRIGHT + listened + f"{Fore.YELLOW}{Style.BRIGHT}\n----------------------------------")
        subprocess.call(["nmap", "-A", "-T4", "-p-", listened])
        # print("\n")


get = user_collector()
response = get_ip_range(get.address)
sift_ip(response)
