import subprocess
import os
import re
import wget

url = 'https://raw.githubusercontent.com/The-Z-Labs/linux-exploit-suggester/master/linux-exploit-suggester.sh'
LesScript = wget.download(url)

output = subprocess.run(['bash',LesScript],capture_output = True).stdout
ansi_escape_8bit = re.compile(
    br'(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])'
)
formatted = ansi_escape_8bit.sub(b'', output)

xx1= str(formatted)
xx = xx1.split('\\n')

ct = 0
bug = []
for words in xx:
    if words == 'Possible Exploits:':
        bug = xx[ct:]
    else:
        ct+=1
        

bugformatted = [x for x in bug if x]     

print(bugformatted)
quit()
