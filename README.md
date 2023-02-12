 _ _       _                
| (_)     | |               
| |_ ____ | |  _ ____  ____ 
| | |  _ \| | / ) _  )/ ___)
| | | | | | |< ( (/ /| |    
|_|_|_| |_|_| \_)____)_|    
                            
A simple script to automate scanning

About:
This script is built using the scapy module, argparse module, subprocess module and colorama module. The script is designed to allow for cidr representation. Once given a range, the script will scan all ip active addresses .

Requirements:
This script requires sudo privileges to be run and built with python3 in mind

Usage
sudo python3 linker.py -i "ip address"
You can use --help to see manual

Example:
sudo python3 linker.py -i 10.0.2.1/24
To scan a range

sudo python3 linker.py -i 10.0.2.67
To scan a single host


