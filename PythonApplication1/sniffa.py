from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.dns import *
import sys

interface = "en0"

def Parseg(packet):
    if IP in packet:
        sourceIP = packet[IP].src
        destinationIP = packet[IP].dst
        if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
            print ("Source : " + str(sourceIP) + "to - " + str(destinationIP) + "-" + str(packet.getlayer(DNS).qd.qname))
            
sniff(iface= "en0", prn=Parseg)

            
        