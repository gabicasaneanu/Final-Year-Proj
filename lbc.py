import subprocess 
import re
import sys

victim = sys.argv[1]


    
   
output = subprocess.run(['/usr/bin/lbd' ,victim, '80'],capture_output = True).stdout
ansi_escape_8bit = re.compile(
    br'(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])'
)
formatted = ansi_escape_8bit.sub(b'', output)

he = str(formatted)
load = he.split('\\n')
loadsformatted =  [x for x in load if x] 
finalout = loadsformatted[-2]
print('<b>'+finalout+'</b>')
if 'NOT' in finalout:
    print('no load balancing detected for specified connection')
