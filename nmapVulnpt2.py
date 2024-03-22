import subprocess
import nmap 
import sys
from itertools import chain

#retrieve IP from CLI
victim = sys.argv[1]

#attempt NM scan 3 times - throw error if failed
tries = 3
for i in range(tries):
    try:
        nm = nmap.PortScanner()
        nmScan = nm.scan(hosts=victim, arguments= '-p 80 --script http-enum')
    except:
        if i < tries - 1:
            continue
        else:
            print('nmap scan failed - host may to be up, check host connectivity / IP (Run Again, nmap may fail on occasion')
            quit()
    break



   
a = list(nmScan.values())
x = a[1]



try:
    Vars = x[victim]['tcp'][80]['script']['http-enum']
except:
    print('<b> No HTTP Enumeration Vulnerabilities Detected </b>')
    quit()


#format and output

sem_format = Vars.split('\n')
full_format = [x for x in sem_format if x]
print('<b> HTTP Directory Enumeration </b> <br/>')
for some in full_format:
        print(some,'<br/>')

