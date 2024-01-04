
import subprocess
import requests
import platform



if platform.system() == 'Linux':
    subprocess.run(['apt','safe-upgrade'])
    quit()
else:
    #subprocess.popen(['choco','upgrade','all','-y'])
    pass



CMDcommand = subprocess.check_output(['wmic','product','get','name'])
Programs = str(CMDcommand)
APIrequest = requests.get('https://endoflife.date/api/all.json')
x = APIrequest.json()
ProgramsList = []
InstalledJuicers = {}


def checkInstalledProgramsVersionValidity(Input,FullProgramName):
    print(Input)
    APIJuicer = requests.get('https://endoflife.date/api/' +Input+ '.json')
    if str(APIJuicer.status_code) == "200":
        Program = ('"' + FullProgramName + '"')
        version = subprocess.check_output(['wmic','product','where','name='+Program,'get','version'])
        AG = (str(version))
        Versionjuicer = AG.replace("\\r"," ").replace("\\n"," ").split()
        InstalledJuicers.update({FullProgramName:Versionjuicer[1]})
        print(InstalledJuicers)
    else:
        print("unluky")
    

try:
    for i in range (len(Programs)):
        output = ((Programs.split("\\r\\r\\n")[6:][i]).lower()) 
        ProgramsList.append(output.split())
except IndexError as e:
    print("")
    
            

for A1 in ProgramsList:
    for words in A1:
        if words in x:
            FullProgramName = ' '.join(A1)
            checkInstalledProgramsVersionValidity(words,FullProgramName)
                



    
