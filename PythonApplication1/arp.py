
import subprocess
from scapy.all import *
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp




def getDefaultGateway():
    CMDcommand = subprocess.check_output(['netsh','interface','ip','show','config','name="Ethernet"'])
    network_output = str(CMDcommand)
    network_array_output = network_output.replace("\\r"," ").replace("\\n"," ").split()
    for i in range(len(network_array_output)):
        if network_array_output[i] == "Default":
            gatewayIP = network_array_output[i+2]
            return gatewayIP


defaultGatewayIP = getDefaultGateway()
interface = "en0"
target_ip = "192.168.0.19"
broadcast_mac = "ff:ff:ff:ff:ff:ff"
packets = 50

def getMac(IP):
    ans, unans = srp(Ether(dst=broadcast_mac)/ARP(pdst = IP), timeout =2,
iface=interface, inter=0.1)
    for send,recieve in ans:
        return recieve.sprintf(r"%Ether.src%")
    return None


gateway_mac = getMac(defaultGatewayIP)
print("gateway max" + gateway_mac)

 




