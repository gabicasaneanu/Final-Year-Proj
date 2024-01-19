import subprocess
import wget
url = 'https://raw.githubusercontent.com/The-Z-Labs/linux-exploit-suggester/master/linux-exploit-suggester.sh'
LesScript = wget.download(url)
output=subprocess.run(['bash',LesScript],check=True,text=True,stdout=subprocess.PIPE).stdout
print(output)
