'''
Author: Dino Charalambous
Date: 2/11/2022
Description: To take a list of peer IPSec Tunnel IP addresses and find their readable name
    associations, which is output to the results file. 
Usage: Run show command execshow against firewall device, you will also need a copy of that devices config.
'''

from multiprocessing.sharedctypes import Value
import os
from netmiko import ConnectHandler
from pathlib2 import Path

def execshow():
    # show command for l2l vpn tunnel info
        cisco1 = {
            "device_type": "cisco_asa",
            "host": "<ip_address>",
            "username": uusername,
            "password": upassword,
            "secret": secret,
        }

        # Show command that we execute.
        command = "show vpn-sessiondb l2l | grep Connection|Index|Encryption|Hashing"

        with ConnectHandler(**cisco1) as net_connect:
            net_connect.enable()
            print("Showing routes")
            output = net_connect.send_command(command)
            #print(output)
            with open('ipsecreport.txt', 'a') as file:
                file.write(output)



def clean_report():
    with open('ipsecreport.txt', 'r') as sfile:
        for line in sfile:
            line = line.strip()
            if 'Connection' in line:
                s = line.split(':')
                ipsec = (s[1])
                with open('ipsecpeers.txt', 'a') as ippeers:
                    ippeers.write(ipsec+'\n')

def read_asa():
    mylist = []
    with open('ipsecpeers.txt') as f:
        for line in f:
            line = line.strip()
            mylist.append(line)
        #print(mylist)

    with open('<device config>', 'r') as asa:
        a = asa.readlines()
        for i in mylist:
            for j in a:
                if i in j and 'crypto map' in j:
                    #print(j)
                    with open('peerinfo.txt','a') as peer:
                        peer.writelines(j)

def read_peerinfo():
    peerlist = []
    with open('peerinfo.txt', 'r') as f:
        for line in f:
            line = line.strip()
            peerlist.append(line)

        result = [item.split(' ') for item in peerlist]
        
        for r in result:
            ip = r[6]
            r = r[2:4]
            x = ' '.join(r)
            #print(x)
            with open('peerindex.txt', 'a') as peerindex:
                peerindex.write(x + ' ' + ip + '\n')

def read_peerasa():
    mystr = ' match address'
    with open('peerindex.txt') as file2:
        for i in file2.readlines():
            i = i.strip('\n')
            s = i.split(' ')
            ip = s[2]
            c = s[0:2]
            cj = ' '.join(c)

            with open('<device config>') as file1:
                with open('results.txt', 'a') as r:
                    for j in file1.readlines():
                        if cj+mystr in j:    
                            r.write(ip + ' ' + j + '\n')

def ip_name():
    peerip = []
    peer_dict = {}
    with open('results.txt', 'r') as file:
        for line in file.readlines():
            if not line.isspace():
                line = line.split(' ')
                ip = line[0]
                name = line[7]
                name = name.strip('\n')
                peer_dict.update({ip:name})
                peerip.append(ip)
            #print(ip)

    for key, value in peer_dict.items():
        #print(key, value)
        file = Path(r'ipsecreport.txt')
        data = file.read_text()
        data = data.replace('Connection   : {}'.format(key), 'Connection   : {}'.format(value))
        file.write_text(data)
        
def send_mail():
        smtpObj = smtplib.SMTP('<mail server>', 25, 'localhost')
        sender_email = "sender@domain.com"
        receiver_email = "receiver@domain.com"

        msg = MIMEMultipart()
        msg['Subject'] = 'IPSec Tunnel Report (Named)'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        filename = "ipsecreport.txt"
        msg.attach(MIMEText(open(filename).read()))

        smtpObj.sendmail(sender_email, receiver_email, msg.as_string())


#this section cleans out the files for new files to be written, make sure files dont exist on first run
def clean_files():
        os.remove('ipsecreport.txt')
        os.remove('results.txt')
        os.remove('peerindex.txt')
        os.remove('peerinfo.txt')
        os.remove('ipsecpeers.txt')
       

            
execshow()            
clean_report()
read_asa()
read_peerinfo()
read_peerasa()
ip_name()
send_mail()
clean_files()
