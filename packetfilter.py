import subprocess
import json


victim = '192.168.195.132'

#run siege for 10seconds, output in json format
output = subprocess.run (['siege',victim,'-t','10s','-j'],capture_output=True).stdout


#parse json output
parseg = json.loads(output)

transactamount = float(parseg['transactions'])
success = float(parseg['successful_transactions'])


if parseg['transactions'] == parseg['successful_transactions']:
    print('no packet filtering measures in place - configure packet filtering and/or nacl')
    print('the transaction rate was:', parseg['transaction_rate'])
    print('the availability was:',parseg['availability'])
    quit()
elif success >= (transactamount*0.80):
    print('success rate seems to be equal or more than 80% - packet filter may be misconfigured')
else:
    print('success rate is lower than 80% - packet filtering seems to be working for >= 80% of packets')
