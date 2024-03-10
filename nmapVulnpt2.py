import subprocess
import nmap 
import json 
import sys
from itertools import chain
victim = sys.argv[1]


tries = 3
for i in range(tries):
    try:
        nm = nmap.PortScanner()
        nmScan = nm.scan(hosts=victim, arguments= '-p 80 --script http-enum')
    except:
        if i < tries - 1:
            continue
        else:
            raise Exception('nmap scan failed - host may to be up, check host       connectivity / IP (Run Again, nmap may fail on occasion')
    break

protos = nm[victim].all_protocols() 



if nm[victim]['tcp'][80]['state'] == 'closed':
    print("no webserver detected")
    quit()

    
  
for proto in protos:
    ports = nm[victim][proto].keys()
    portx = list(ports)
    
   
a = list(nmScan.values())
x = a[1]

Vars = []

for ports in portx:
    Vars.append([x[victim]['tcp'][ports]['script']['http-enum']])



list_vals = list(chain.from_iterable(Vars))
real_vals = list_vals[0]
sem_format = real_vals.split('\n')
full_format = [x for x in sem_format if x]
print('<b> HTTP Directory Enumeration </b> <br/>')
for some in full_format:
        print(some,'<br/>')

