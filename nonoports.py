#ports sourced from https://support.huawei.com/enterprise/en/doc/EDOC1100297670
import nmap
import sys


victim = sys.argv[1]
command = '-p 20,21,23,39,3389,5900-5902,512-514,873,53,111,2049,135-139,445,161,389,25,110,143,80,8000,8080,8888,1433,1521,3306,5000,5432,6379,27017-27018 -d -d'
ports = [20,21,23,39,3389,5900,5901,5902,512,513,514,873,53,111,2049,135,136,137,138,139,445,161,389,25,110,143,80,8000,8080,8888,1433,1521,3306,5000,5432,6379,27017,27018]

rms_ports = [20,21,22,23,69,3389,5900,5901,5902,512,513,514]
lan_ports = [53,111,2049,135,137,138,139,445,161,389]
internet_ports = [25,110,143,80,8000,8080,8888]
database_ports = [1433,1521,3306,5000,5432,6379,27017,27018]

tries = 3
for i in range(tries):
    try:
        nm = nmap.PortScanner()
        nmScan = nm.scan(hosts = victim, arguments = command)
    except:
        if i < tries - 1:
            continue
        else:
            raise Exception('nmap scan failed - host may to be up, check host       connectivity / IP (Run Again, nmap may fail on occasion')
    break
     

scan_vals = list(nmScan.values())
act_scan = scan_vals[1]
open_p = []

for ports_no in ports:
    ports_status = nm[victim]['tcp'][ports_no]
    if ports_status['state'] == 'open':
        open_p.append(ports_no)

if open_p == 'None':
    print('no bad ports open')
    quit()
    
def pattern_check(port):
    for port_int in port:
        if port_int in rms_ports:
            print('port :' ,port_int, ' is <b>open</b> - Disable always. Use SSHv2 or deploy the O&M audit system.<br/> ')
        if port_int in lan_ports:
            print('port :',port_int,' is <b>open</b> - Disable always<br/>')
        if port_int in internet_ports:
            if port_int == 25:
                print('port :',port_int,' is <b>open</b> - Disable always. Use SMTPS instead<br/>') 
            if port_int == 110:
                print('port :',port_int,' is <b>open</b> - Disable always. Use POP3S instead<br/>')
            if port_int == 143:
                print('port :',port_int,' is <b>open</b> - Disable always. Use IMAPS instead<br/>')
            if port_int == 80 or port_int == 8000 or port_int == 8080 or port_int == 8888:
                print('port :',port_int,' is <b>open</b> - Disable recommended. Use HTTPS instead<br/>')
        if port_int in database_ports:
            print('port :',port_int,' is <b>open</b> - Disable always<br/>')
            
            
pattern_check(open_p)
            






