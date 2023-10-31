import subprocess
import psutil
import requests
import platform




def checkWindowsVersion():
    a = platform.system()
    r = requests.get('https://endoflife.date/api/' + a + '.json')
    x = r.json()
    windowsVers = platform.platform()
    windowsVersion = windowsVers.split("-")
    print(windowsVersion,x[0]['latest'])
    if windowsVersion[2] == x[0]['latest']:
        print("your windows version - " + windowsVersion[2] + " is the latest version")
        #return true
    else:
        print("not latest version - link here : " + x[0]['link'])
        #return false
    
checkWindowsVersion()

'''
C = subprocess.check_output(['wmic','product','get','name'])
a = str(C)

v = []

def containsMicrosoft(string,word):
    return (' ' + word + ' ') in ( ' ' + string +' ')

try:
    for i in range(len(a)):
        
        output = (a.split("\\r\\r\\n")[6:][i]) 
        versions = (output.split(" - "))
        if containsMicrosoft(versions[0],'Microsoft') == True:
            v.append(versions[0])
        


            
        
except IndexError as e:
    print("done")
 '''

   

#s = psutil.win_service_get('alg')
#print(s.as_dict())

