import os 
import subprocess
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph,Spacer
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.flowables import KeepTogether
from reportlab.lib import colors
from reportlab.platypus import PageBreak
from reportlab.graphics.shapes import *



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

def lin_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,500,80, fillColor = colors.white))
    info.add(String(3,88,'Info Relating to Linux Priviledge Escalation :',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'LinPEAS is a script that search for possible paths to escalate privileges on Linux/Unix*/MacOS hosts.',fontSize = 12,setFont='Helvetica-Bold' ,fillColor = colors.black))
    info.add(String(3,63,'https://book.hacktricks.xyz/linux-hardening/privilege-escalation',fontSize = 12,setFont='Helvetica-Bold' ,fillColor = colors.black))
    info.add(String(3,50,'https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    
    return(info)
    
def les_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,500,80, fillColor = colors.white))
    info.add(String(3,88,'LES tool is designed to assist in detecting security deficiencies for a given Linux-based machine.',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://github.com/xairy/linux-kernel-exploitation',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://mzet-.github.io/2019/05/10/les-paper.html',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://github.com/lucyoa/kernel-exploits',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)
    
def eth_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,500,80, fillColor = colors.white))
    info.add(String(3,88,'Promiscuous mode can be used in a malicious way to capture private data in transit on a network',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://en.wikipedia.org/wiki/Promiscuous_mode',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://www.blumira.com/glossary/promiscuous-mode/',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://www.techtarget.com/searchsecurity/definition/promiscuous-mode',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)
     
def nm2_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'Using brute-force methods to check if certain data/directories exists on a web server database',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://www.upguard.com/blog/what-is-an-enumeration-attack',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://book.hacktricks.xyz/network-services-pentesting/pentesting-web#brute-force-directories-and-files',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://nmap.org/nsedoc/scripts/http-enum.html',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)
            

def packet_filter_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'Sending many packets to check availability and Anti-DDOS Measures to minimize DDOS impact',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://www.cloudflare.com/en-gb/learning/ddos/how-to-prevent-ddos-attacks/',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://www.byos.io/blog/denial-of-service-attack-prevention',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-network',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)
    
def lbc_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'Load balancers can include security features such as SSL encryption and web application firewalls',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'Load balancers can also introduce vulnerabilities to a network',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://www.reblaze.com/wiki/load-balancing/load-balancing-and-security/',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://www.ibm.com/topics/load-balancing',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)
    
def nm_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'Listing known vulnerabilities for services, including CVE number',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://cve.mitre.org/cve/search_cve_list.html',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://nvd.nist.gov/vuln/search',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://www.cvedetails.com/',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)
    
def ports_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'Assessing Known Vulnerable ports and their status',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://support.huawei.com/enterprise/en/doc/EDOC1100297670',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://blog.netwrix.com/2022/08/04/open-port-vulnerabilities-list/',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://specopssoft.com/blog/open-ports-and-their-vulnerabilities/',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)  

def csrf_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'(CSRF) is an attack that forces an end user to execute unwanted actions on a web application',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://owasp.org/www-community/attacks/csrf',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://portswigger.net/web-security/csrf',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://en.wikipedia.org/wiki/Cross-site_request_forgery',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)
    
def sql_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'A successful SQL injection exploit can read/modify/delete sensitive data from the database',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://owasp.org/www-community/attacks/SQL_Injection',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://portswigger.net/web-security/sql-injection',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://en.wikipedia.org/wiki/SQL_injection',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)    
    
def ftp_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'This form of authentication allows access to an FTP site without a user account on your server or domain',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://book.hacktricks.xyz/network-services-pentesting/pentesting-ftp',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://www.ibm.com/docs/ar/i/7.4?topic=i-configuring-anonymous-ftp',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://www.techtarget.com/whatis/definition/anonymous-FTP-File-Transfer-Protocol',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)
    
def http_logins_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'Tests for access with default credentials used by a variety of web applications and devices.',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://nmap.org/nsedoc/scripts/http-default-accounts.html',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://datarecovery.com/rd/default-passwords/',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://www.softwaretestinghelp.com/default-router-username-and-password-list/',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)  
    
def nbt_info():
    info = Drawing(100,100)
    info.add(Rect(0,30,510,80, fillColor = colors.white))
    info.add(String(3,88,'NetBIOS Name Service plays a crucial role, involving various services such as IP, Shares etc.',fontSize = 12,fillColor = colors.black))
    info.add(String(3,75,'https://book.hacktricks.xyz/network-services-pentesting/137-138-139-pentesting-netbios',fontSize = 12,fillColor = colors.black))
    info.add(String(3,63,'https://www.skywaywest.com/2021/01/what-is-a-netbios-vulnerability/',fontSize = 12,fillColor = colors.black))
    info.add(String(3,50,'https://www.beyondsecurity.com/resources/vulnerabilities/netbios-information-retrieval',fontSize = 12,setFont='Helvetica-Bold',fillColor = colors.black))
    return(info)               
        
    
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
    packet_filter_header = Paragraph("<u>DDOS-ASSESSMENT OUTPUT</u> <br/>",style=styles['Normal'])
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
                flowables.append(lin_info())
                flowables.append(lin_header)
                flowables.append(lin_para)
                flowables.append(PageBreak())
            case '1':  
                les_text = run_command(les_command)
                les_para = Paragraph(les_text, style=styles['Normal'])
                flowables.append(les_info())
                flowables.append(les_header)
                flowables.append(les_para)
                flowables.append(PageBreak())
            case '2':
                eth_text = run_command(eth_command)
                eth_para = Paragraph(eth_text, style=styles['Normal'])
                flowables.append(eth_info())
                flowables.append(eth_header)
                flowables.append(eth_para)
                flowables.append(PageBreak())
            case '3':
                nm2_text = run_command(nm2_command)
                nm2_para = Paragraph(nm2_text, style=styles['Normal'])
                flowables.append(nm2_info())
                flowables.append(nm2_header)
                flowables.append(nm2_para)
                flowables.append(PageBreak())
            case '4':
                packet_filter_text = run_command(packet_filter_command)
                packet_filter_para = Paragraph(packet_filter_text, style=styles['Normal'])
                flowables.append(packet_filter_info())
                flowables.append(packet_filter_header)
                flowables.append(packet_filter_para)
                flowables.append(PageBreak())
                
            case '5':
                lbc_text = run_command(lbc_command)
                lbc_para = Paragraph(lbc_text, style=styles['Normal'])
                flowables.append(lbc_info())
                flowables.append(lbc_header)
                flowables.append(lbc_para)
                flowables.append(PageBreak())
            case '6':
                nm_text = run_command(nm_command)
                nm_para = Paragraph(nm_text, style=styles['Normal'])
                flowables.append(nm_info())
                flowables.append(nm_header)
                flowables.append(nm_para)
                flowables.append(PageBreak())
            case '7':
                ports_text = run_command(ports_command)
                ports_para = Paragraph(ports_text, style=styles['Normal'])
                flowables.append(ports_info())
                flowables.append(ports_header)
                flowables.append(ports_para)
                flowables.append(PageBreak())
            case '8':
                csrf_text = run_command(csrf_command)
                csrf_para = Paragraph(csrf_text, style = styles['Normal'])
                flowables.append(csrf_info())
                flowables.append(csrf_header)
                flowables.append(csrf_para)
                flowables.append(PageBreak())
            case '9':
                sql_text = run_command(sql_command)
                sql_para = Paragraph(sql_text, style = styles['Normal'])
                flowables.append(sql_info())
                flowables.append(sql_header)
                flowables.append(sql_para)
                flowables.append(PageBreak())
            case '10':  
                ftp_text = run_command(ftp_command)
                ftp_para = Paragraph(ftp_text, style = styles['Normal']) 
                flowables.append(ftp_info()) 
                flowables.append(ftp_header)
                flowables.append(ftp_para)
                flowables.append(PageBreak())
            case '11':
                http_logins_text = run_command(http_logins_command)
                http_logins_para = Paragraph(http_logins_text, style = styles['Normal'])
                flowables.append(http_logins_info())
                flowables.append(http_logins_header)
                flowables.append(http_logins_para)
                flowables.append(PageBreak())
            case '12':
                nbt_text = run_command(nbt_command)
                nbt_para = Paragraph(nbt_text, style = styles['Normal'])
                flowables.append(nbt_info())
                flowables.append(nbt_header)
                flowables.append(nbt_para)
                flowables.append(PageBreak())
                
    
    
    
    
    
    
    
    
    
    
 

    doc.build(flowables)
    
    
pdf()
    
    
