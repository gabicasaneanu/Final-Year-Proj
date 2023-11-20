import subprocess
from scapy.all import *

interface = "en0"


def getDefaultGateway():
    CMDcommand = subprocess.check_output(['netsh','interface','ip','show','config','name="Ethernet"'])
    network_output = str(CMDcommand)
    network_array_output = network_output.replace("\\r"," ").replace("\\n"," ").split()
    for i in range(len(network_array_output)):
        if network_array_output[i] == "Default":
            gatewayIP = network_array_output[i+2]
            return gatewayIP


defaultGatewayIP = getDefaultGateway()

target_ip = "192.168.0.63"
broadcast_mac = "ff:ff:ff:ff:ff:ff"
packets = 50

def getMac(mac_ip):
    a,b = srp(Ether(dst=broadcast_mac)/ARP(pdst = IP)






