import os 
import subprocess
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph,Spacer
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.flowables import KeepTogether


try:
    victim = sys.argv[1]
except IndexError:
    print('no victim IP provided')
    quit()

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
    eth_header = Paragraph("<u>SNIFFING OUTPUT</u> <br/>",style=styles['Normal'])
    
    #network headers
    nm2_header = Paragraph("<u>NMAP HTTP ENUMERATION SCAN OUTPUT</u> <br/>",style=styles['Normal'])
    packet_filter_header = Paragraph("<u>PACKET FILTER OUTPUT</u> <br/>",style=styles['Normal'])
    lbc_header = Paragraph("<u>LOAD BALANCER OUTPUT</u> <br/>",style=styles['Normal'])
    nm_header = Paragraph("<u>SERVICE EXPLOIT OUTPUT</u> <br/>",style=styles['Normal'])
    ports_header = Paragraph("<u>OPEN PORTS OUTPUT</u> <br/>",style=styles['Normal'])
    csrf_header = Paragraph("<u>CROSS SITE REQUEST FORGERY OUTPUT</u> <br/>",style=styles['Normal'])
    sql_header = Paragraph("<u>SQL INJECTION OUTPUT</u> <br/>",style=styles['Normal'])
    ftp_header = Paragraph("<u>FTP LOGIN OUTPUT</u> <br/>",style=styles['Normal'])
    
    
    
    
    #run local commands
    lin_text = run_command(lin_command)
    les_text = run_command(les_command)
    eth_text = run_command(eth_command)
    
    #run network commands
    
    nm2_text = run_command(nm2_command)
    packet_filter_text = run_command(packet_filter_command)
    lbc_text = run_command(lbc_command)
    nm_text = run_command(nm_command)
    ports_text = run_command(ports_command)
    csrf_text = run_command(csrf_command)
    sql_text = run_command(sql_command)
    ftp_text = run_command(ftp_command)
    
    
    
    
    #make paragraphs
    lin_para = Paragraph(lin_text, style=styles['Normal'])
    les_para = Paragraph(les_text, style=styles['Normal'])
    eth_para = Paragraph(eth_text, style=styles['Normal'])
    
    #network paragraphs
    nm2_para = Paragraph(nm2_text, style=styles['Normal'])
    packet_filter_para = Paragraph(packet_filter_text, style=styles['Normal'])
    lbc_para = Paragraph(lbc_text, style=styles['Normal'])
    nm_para = Paragraph(nm_text, style=styles['Normal'])
    ports_para = Paragraph(ports_text, style=styles['Normal'])
    csrf_para = Paragraph(csrf_text, style = styles['Normal'])
    sql_para = Paragraph(sql_text, style = styles['Normal'])
    ftp_para = Paragraph(ftp_text, style = styles['Normal'])
    
    spacer = KeepTogether(Spacer(1, 3*inch))
    smallspacer = KeepTogether(Spacer(1,1*inch))
    medspacer = KeepTogether(Spacer(1,2*inch))
    
    
    
    flowables.append(lin_header)
    flowables.append(lin_para)
    flowables.append(smallspacer)
    
    flowables.append(les_header)
    flowables.append(les_para)
    flowables.append(medspacer)
    
    flowables.append(eth_header)
    flowables.append(eth_para)
    flowables.append(smallspacer)
    
    flowables.append(nm2_header)
    flowables.append(nm2_para)
    flowables.append(smallspacer)
    
    flowables.append(packet_filter_header)
    flowables.append(packet_filter_para)
    flowables.append(smallspacer)
    
    flowables.append(lbc_header)
    flowables.append(lbc_para)
    flowables.append(medspacer)
    
    flowables.append(nm_header)
    flowables.append(nm_para)
    flowables.append(spacer)
    
    flowables.append(ports_header)
    flowables.append(ports_para)
    flowables.append(spacer)
    
    flowables.append(csrf_header)
    flowables.append(csrf_para)
    flowables.append(spacer)
    
    flowables.append(sql_header)
    flowables.append(sql_para)
    flowables.append(smallspacer)
    
    flowables.append(ftp_header)
    flowables.append(ftp_para)
    
    
   
    
    
    
    
    
    
 
    doc.build(flowables)
    
    
pdf()
    
    
