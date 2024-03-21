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
        nmScan = nm.scan(hosts=victim, arguments= '-p 80 --script http-csrf')
    except:
        if i < tries - 1:
            nmScan = nm.scan(hosts=victim, arguments= '-p 80 --script http-csrf')
        else:
            raise Exception('nmap scan failed - host may to be up, check host       connectivity / IP (Run Again, nmap may fail on occasion')
    break
    

    

    
    
    
a = list(nmScan.values())
x = a[1]

try:
    Vars = x[victim]['tcp'][80]['script']['http-csrf']
except:
    print('<b>No Cross Site Request Forgery Vulnerabilities Detected </b>')
    quit()








sem_format = Vars.split('\n')
full_format = [x for x in sem_format if x]
print('<b> Cross Site Request Forgery Vulnerabilities </b> <br/>')
for real_vals in full_format:
    print(real_vals,'<br/>')
    

