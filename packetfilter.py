import subprocess
import json
import sys

victim = sys.argv[1]

#run siege for 10seconds, output in json format
output = subprocess.run (['siege',victim,'-t','10s','-j'],capture_output=True).stdout


#parse json output
parseg = json.loads(output)

transactamount = float(parseg['transactions'])
success = float(parseg['successful_transactions'])


if parseg['transactions'] == parseg['successful_transactions']:
    print('<b>no packet filtering measures in place</b> <br/> configure packet filtering and/or nacl <br/>')
    print('<b>the transaction rate was:</b>', parseg['transaction_rate'],'<br/>')
    print('<b>the availability was:</b>',parseg['availability'],'<br/>')
    quit()
elif success >= (transactamount*0.80):
    print('success rate seems to be equal or more than 80% - packet filter may be misconfigured or not in place')
else:
    print('success rate is lower than 80% - packet filtering seems to be working for >= 80% of packets')
