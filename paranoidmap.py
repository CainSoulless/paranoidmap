#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import datetime, subprocess, os, smtplib, getpass, time
 
#Manipulable variables.

sender = ""
receiver = ""
target = ""

#Not manipuable variables.
today, hours,firstconf = 0, 0, -1
today = date.today()
now = datetime.datetime.now()
homedir = os.environ["HOME"]

def banner():
    print(" ____   ___ ___   ____  ____  \n|    \ |   |   | /    ||    \ \n|  _  || _   _ ||  o  ||  o  )\n|  |  ||  \_/  ||     ||   _/ \n|  |  ||   |   ||  _  ||  |   \n|  |  ||   |   ||  |  ||  |   \n|__|__||___|___||__|__||__|   \n                              ")
    print("version 0.1 \nDate: ",today,"\nHour: ",now.hour,":",now.minute,":",now.second)

    try:
        check_output,retornoerror = '', ''
        outputmkdir = subprocess.check_output("mkdir {}/.paranoidmap 2> /dev/null".format(homedir), shell = True)
    except subprocess.CalledProcessError as retornoerror:
        if retornoerror.returncode == 1:
            pass
banner()
if firstconf == -1: #This if only for changes in the future lul.
    print("REMEMBER to change variables of 'sender', 'target' and 'receiver' in the code.")
    time.sleep(1)
    #password = getpass.getpass(prompt="Sender password: ")
    time.sleep(1)
    
    #Validate if the user has input a correct time.
    def validate_time(set_alarm):
        if len(set_alarm) != 11:
            print("Please try a valid time format... ")
        else:
            if int(set_alarm[0:2]) > 12 and int(set_alarm[0:2]) < 0 :
                print("Please try a valid HOUR...")
            elif int(set_alarm[3:5]) > 59 and int(set_alarm[3:5]) < 0 :
                print("Please try a valid MINUTE...")
            elif int(set_alarm[6:8]) > 59 and int(set_alarm[6:8]) < 0 :
                print("Please try a valid SECOND...")
            else:
                return "ok"
    #Take the time.
    while True:
        set_alarm = input("Enter time in 'HH:MM:SS AM/PM' format: ")

        validate = validate_time(set_alarm.lower())
        if validate != "ok":
            print(validate)
        else:
            print(f"Setting time for {set_alarm}...") 
        break
    
    #Assigns according to set_alarm position.
    alarm_hour = set_alarm[0:2]
    alarm_min = set_alarm[3:5]
    alarm_sec = set_alarm[6:8]
    alarm_period = set_alarm[9:].upper()
    
    #Waits for the time.
    def wait_time():
        while True:
            now = datetime.datetime.now()
            current_hour = now.strftime("%H")
            current_min = now.strftime("%M")
            current_sec = now.strftime("%S")
            current_period = now.strftime("%p")
        
            if alarm_period == current_period:
            
                if alarm_hour == current_hour:
                    if alarm_min == current_min:
                        if alarm_sec == current_sec:
                            def scanner():
                                #Start the scanning and open the output file for sends it later.
                                os.system('/usr/bin/nmap {} -T4 -p- -oN {}/.paranoidmap/scan{}.txt'.format(target, homedir, today))
                                scantxt = open("{}/.paranoidmap/scan{}.txt".format(homedir, today),"rb")
                                
                                def send_email():
                                    try:
                                    #Header email.
                                        msg = MIMEMultipart()
                                        msg["From"] = sender
                                        msg["To"] = receiver
                                        msg["Subject"] = str("{} | {} | {}".format(target, today, now))
                                        #Prepare the body.
                                        body = MIMEBase("application", "octate-steam")
                                        body.set_payload((scantxt.read()))                                        
                                        encoders.encode_base64(body)
                                    
                                        body.add_header("Content-Decomposition", "attachment", filename = "scan{}.txt".format(today))
                                        msg.attach(body)
                                        #Prepare the smtp service.            
                                        gmail = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                                        print("-------------------\nLog: smtp.gmail.com")
                                        #gmail.starttls()
                                        gmail.login(sender, password)
                                        print("-------------------\nLog: Login success.")
                                        text = msg.as_string()
                                        gmail.sendmail(sender, receiver, text)
                                        gmail.quit()
                                        print("-------------------\nLog: Email sended.\n-------------------")
                                        print("Date: ",today, "\nHour: ",now.hour,":", now.minute,":", now.second)

                                    except:
                                        print("Emailing scan not completed...")
                                send_email()        
                                wait_time()
                            scanner()
    wait_time()
    firstconf = 1
