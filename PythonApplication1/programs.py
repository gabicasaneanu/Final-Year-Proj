
import subprocess
import requests
import platform



CMDcommand = subprocess.check_output(['wmic','product','get','name'])
Programs = str(CMDcommand)
APIrequest = requests.get('https://endoflife.date/api/all.json')
x = APIrequest.json()
ProgramsList = []
InstalledJuicers = []


def checkInstalledProgramsVersionValidity(Input,FullProgramName):
    print(Input)
    APIJuicer = requests.get('https://endoflife.date/api/' +Input+ '.json')
    print(APIJuicer.status_code)
    if str(APIJuicer.status_code) == "200":
        version = subprocess.check_output(['wmic','product','where','"name=\'',FullProgramName,'\'"','get','version'])
        print (str(version))
    else:
        print("unluky")
    

try:
    for i in range (len(Programs)):
        output = ((Programs.split("\\r\\r\\n")[6:][i]).lower()) 
        ProgramsList.append(output.split())
except IndexError as e:
    print("done")
    
            

for A1 in ProgramsList:
    for words in A1:
        if words in x:
            FullProgramName = ' '.join(A1)
            checkInstalledProgramsVersionValidity(words,FullProgramName)
                



    