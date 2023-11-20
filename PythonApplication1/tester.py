import subprocess


r = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
ls = r.split("\n")
ssids = [v.strip() for k,v in (p.split(':') for p in ls if 'SSID' in p)]
print(ssids)

def nmscanner(): 
    
    nm.scan(hosts=IPrange[0] + "." + IPrange[1] + "." + IPrange[2] + "."+ "0" + '/24', arguments= 'n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    
    for host, status in hosts_list:
        print(host,status)