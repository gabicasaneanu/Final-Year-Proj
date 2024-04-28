import os 
import subprocess
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph,Spacer
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.flowables import KeepTogether


victim = sys.argv[1]
    

current_dir = os.getcwd()
lin_command = ('python3',current_dir+'/linL.py')
les_command = ('python3',current_dir+'/localenum.py')
eth_command = ('python3',current_dir+'/promiscStatus.py')

#processes requiring victim IP
nm2_command = ('python3',current_dir+'/nmapVulnpt2.py',victim)
packet_filter_command = ('python3',current_dir+'/packetfilter.py',victim)
lbc_command = ('python3',current_dir+'/lbc.py',victim)
nm_command = ('python3',current_dir+'/nmapVuln.py',victim)
ports_command = ('python3',current_dir+'/nonoports.py',victim)
csrf_command = ('python3',current_dir+'/csrf.py',victim)
sql_command = ('python3',current_dir+'/sql.py',victim)
ftp_command = ('python3',current_dir+'/ftp.py',victim)
http_logins_command = ('python3',current_dir+'/httplogins.py',victim)
nbt_command = ('python3',current_dir+'/netbios.py',victim)

def run_command(inp):
    x = subprocess.run(inp, capture_output = True).stdout
    return(x)



    
    
def pdf():
    doc = SimpleDocTemplate('VulnerabillityReport.pdf',
    pagesize = letter)
    styles = getSampleStyleSheet()
    
    
    flowables = []
    styles = getSampleStyleSheet()
    
    #local headers
    lin_header = Paragraph("<u>LINPEAS OUTPUT</u> <br/>",style=styles['Normal'])
    les_header = Paragraph("<u>LINUX EXPLOIT SUGGESTER OUTPUT</u> <br/>",style=styles['Normal'])
    eth_header = Paragraph("<u>PORT STATUS OUTPUT</u> <br/>",style=styles['Normal'])
    
    #network headers
    nm2_header = Paragraph("<u>NMAP HTTP ENUMERATION SCAN OUTPUT</u> <br/>",style=styles['Normal'])
    packet_filter_header = Paragraph("<u>PACKET FILTER OUTPUT</u> <br/>",style=styles['Normal'])
    lbc_header = Paragraph("<u>LOAD BALANCER OUTPUT</u> <br/>",style=styles['Normal'])
    nm_header = Paragraph("<u>SERVICE EXPLOIT OUTPUT</u> <br/>",style=styles['Normal'])
    ports_header = Paragraph("<u>OPEN PORTS OUTPUT</u> <br/>",style=styles['Normal'])
    csrf_header = Paragraph("<u>CROSS SITE REQUEST FORGERY OUTPUT</u> <br/>",style=styles['Normal'])
    sql_header = Paragraph("<u>SQL INJECTION OUTPUT</u> <br/>",style=styles['Normal'])
    ftp_header = Paragraph("<u>FTP LOGIN OUTPUT</u> <br/>",style=styles['Normal'])
    http_logins_header = Paragraph("<u>HTTP DEFAULT LOGIN OUTPUT</u> <br/>",style=styles['Normal'])
    nbt_header = Paragraph("<u>NETBIOS NAME TABLE INFORMATION</u> <br/>", style =styles['Normal'])
    
    spacer = KeepTogether(Spacer(1, 3*inch))
    smallspacer = KeepTogether(Spacer(1,1*inch))
    medspacer = KeepTogether(Spacer(1,2*inch))
    
    split_args = sys.argv[2].split()
    
    for arguments in split_args:
        match arguments:
            case '0':
                lin_text = run_command(lin_command)
                lin_para = Paragraph(lin_text, style=styles['Normal'])
                flowables.append(lin_header)
                flowables.append(lin_para)
                flowables.append(smallspacer)
            case '1':  
                les_text = run_command(les_command)
                les_para = Paragraph(les_text, style=styles['Normal'])
                flowables.append(les_header)
                flowables.append(les_para)
                flowables.append(medspacer)
            case '2':
                eth_text = run_command(eth_command)
                eth_para = Paragraph(eth_text, style=styles['Normal'])
                flowables.append(eth_header)
                flowables.append(eth_para)
                flowables.append(smallspacer)
            case '3':
                nm2_text = run_command(nm2_command)
                nm2_para = Paragraph(nm2_text, style=styles['Normal'])
                flowables.append(nm2_header)
                flowables.append(nm2_para)
                flowables.append(smallspacer)
            case '4':
                packet_filter_text = run_command(packet_filter_command)
                packet_filter_para = Paragraph(packet_filter_text, style=styles['Normal'])
                flowables.append(packet_filter_header)
                flowables.append(packet_filter_para)
                flowables.append(smallspacer)
            case '5':
                lbc_text = run_command(lbc_command)
                lbc_para = Paragraph(lbc_text, style=styles['Normal'])
                flowables.append(lbc_header)
                flowables.append(lbc_para)
                flowables.append(medspacer)
            case '6':
                nm_text = run_command(nm_command)
                nm_para = Paragraph(nm_text, style=styles['Normal'])
                flowables.append(nm_header)
                flowables.append(nm_para)
                flowables.append(spacer)
            case '7':
                ports_text = run_command(ports_command)
                ports_para = Paragraph(ports_text, style=styles['Normal'])
                flowables.append(ports_header)
                flowables.append(ports_para)
                flowables.append(spacer)
            case '8':
                csrf_text = run_command(csrf_command)
                csrf_para = Paragraph(csrf_text, style = styles['Normal'])
                flowables.append(csrf_header)
                flowables.append(csrf_para)
                flowables.append(spacer)
            case '9':
                sql_text = run_command(sql_command)
                sql_para = Paragraph(sql_text, style = styles['Normal'])
                flowables.append(sql_header)
                flowables.append(sql_para)
                flowables.append(smallspacer)
            case '10':  
                ftp_text = run_command(ftp_command)
                ftp_para = Paragraph(ftp_text, style = styles['Normal'])  
                flowables.append(ftp_header)
                flowables.append(ftp_para)
                flowables.append(smallspacer)
            case '11':
                http_logins_text = run_command(http_logins_command)
                http_logins_para = Paragraph(http_logins_text, style = styles['Normal'])
                flowables.append(http_logins_header)
                flowables.append(http_logins_para)
                flowables.append(smallspacer)
            case '12':
                nbt_text = run_command(nbt_command)
                nbt_para = Paragraph(nbt_text, style = styles['Normal'])
                flowables.append(nbt_header)
                flowables.append(nbt_para)
                flowables.append(smallspacer)
                
    
    
    
    
    
    
    
    
    
    
 

    doc.build(flowables)
    
    
pdf()
    
    
