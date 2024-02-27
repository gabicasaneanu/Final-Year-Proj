from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.dns import *
import sys
import webbrowser
import time



interface = "ens33"
path = '/usr/lib/firefox-esr/firefox-esr %s'

def Parseg(packet):
    if IP in packet:
        sourceIP = packet[IP].src
        destinationIP = packet[IP].dst
        if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
            print ("Source : " + str(sourceIP) + "to - " + str(destinationIP) + "- " + str(packet.getlayer(DNS).qd.qname))
        
def sniffla():
    sniff(iface= "ens33", prn=Parseg,timeout = 5)
    
sniffla()
 
