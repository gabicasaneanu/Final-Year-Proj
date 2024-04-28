import subprocess
import sys

victim = sys.argv[1]
output = subprocess.run(['nbtscan',victim,'-v','-q'], capture_output = True).stdout
p_out = output.decode('utf-8')
if 'NetBIOS' in p_out:
    split_out = p_out.split('\n')
    for x,fields in enumerate(split_out):
        if x == 0:
            pass
        if x == 1:
            print('<b>' + fields + '</b>')
        else:
            print(fields + '<br/>')
else:
    print('<b> No NetBIOS Information Detected </b>')
