import os
import wget
import subprocess
import json
from pprint import pprint

lin_url = 'https://github.com/carlospolop/PEASS-ng/releases/download/20240204-ab87b191/linpeas.sh'
parser_url = 'https://raw.githubusercontent.com/carlospolop/PEASS-ng/master/parsers/peas2json.py'

lin_exists_path = './temp/linpeas.sh'
out_path = './temp/lin_out.out'
lin_parser_path = './temp/peas2json.py'
final_out_path = './temp/finalp.json'


first_bash_command = ('bash'+ ' ' + lin_exists_path + ' '+'-s'+ ' ' + '-a' + ' '+ '>' + out_path)
second_bash_command = ('python3' + ' ' + lin_parser_path + ' ' + out_path + ' ' +  final_out_path)  

def FileTempCheck(inp):
    return(os.path.isfile(inp))
        
        
def TryDownload(url):
    print('downloading')
    tries = 3
    for i in range(tries):
        try:
            outpp = './temp'
            wget.download(url, out = outpp )
        except:
            if i < tries - 1:
                continue
            else:
                raise Exception('Could not resolve DNS of repo')
        break


def setupFiles():
    if FileTempCheck(lin_exists_path):
        pass
    else:
        TryDownload(lin_url)
    if FileTempCheck(lin_parser_path):
        pass
    else:
        TryDownload(parser_url)

setupFiles()

def BashCommands():
    if FileTempCheck(out_path):
        pass
    else:   
        os.system(first_bash_command)
    
    if FileTempCheck(final_out_path):
        pass
    else:
        os.system(second_bash_command)
        
json_file = open(final_out_path)
json_data = json.load(json_file)

sections = {'Basic information':'None', 'System Information':'None', 'Container':'None', 'Cloud':'None', 'Processes, Crons, Timers, Services and Sockets':'None', 'Network Information':'None', 'Users Information':'None', 'Software Information':'None', 'Files with Interesting Permissions':'None', 'Other Interesting Files':'None', 'API Keys Regex':'None'}

colors_sections_indexed = []

def ParserREDYELLOW(json_in):
    for keys in json_in:
        print('<b>',keys,'</b>','<br/>')
        js_p = json_in[keys]['sections']
        for je in js_p:
            act = json_in[keys]['sections'][je]['lines']
            for acs in act:
                gex = list(acs['colors'].keys())
                if gex == ['RED'] or gex == ['REDYELLOW']:
                    if acs['clean_text'] is None:
                        break
                    else:
                        sections[keys] = acs['clean_text']
                        print(acs['clean_text'],' == ',gex,'<br/>')
                    #print(json_in[keys]['sections'][je]['lines'])
                    
            break
    
                    
                    
                    
            
            
            
            
print(ParserREDYELLOW(json_data))


  

