import subprocess
import nmap 
import json 
import re
from itertools import chain
from pprint import pprint
victim = '10.10.11.242'

nm = nmap.PortScanner()
nmScan = nm.scan(hosts=victim, arguments= '-sSV -sC --script vuln')

protos = nm[victim].all_protocols()    
for proto in protos:
    ports = nm[victim][proto].keys()
    portx = list(ports)
    
    
a = list(nmScan.values())
x = a[1]

Vars = []

for ports in portx:
    Vars.append([x[victim]['tcp'][ports]['script']])



lol = list(chain.from_iterable(Vars))
for x in lol:
    pprint(x)
