from scapy.all import *
import subprocess
import sys
import netifaces


p_status = []
promisc_check = subprocess.run(['ip','-d','link'],capture_output = True).stdout
p_out = promisc_check.decode('utf-8')
p_format = p_out.split(' ')
for x,var in enumerate(p_format):
    if var == 'promiscuity':
        p_status.append(p_format[x+1])

n_ifaces = netifaces.interfaces()        



for x,p in enumerate(p_status):
    if p == '1':
        print('interface ' + n_ifaces[x] + ' operating in promiscuous mode ' + p +  ' - potential sniffing')
    else:
        pass
