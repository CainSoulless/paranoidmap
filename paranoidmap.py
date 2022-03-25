#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Thought of being red team tool operations, paranoidmap automates nmap scans, and then sends the -oN output file by email (Perhaps, a history system).
#  It is more practical, because you can see all the scans files without connecting to the server, where this program is running.
#
#  Author: Rodrigo Hormazabal (Aka. CainSoulless)

from datetime import *
from email import encoders
from datetime import datetime
from optparse import OptionParser
import datetime, subprocess, os, smtplib, getpass, time, ssl
from email.message import EmailMessage

today, hours,firstconf = 0, 0, -1
today = date.today()
now = datetime.datetime.now()
homedir = os.environ["HOME"]


def banner():
    subprocess.run(["clear"], shell = False)
    print(" ____   ___ ___   ____  ____  \n|    \ |   |   | /    ||    \ \n|  _  || _   _ ||  o  ||  o  )\n|  |  ||  \_/  ||     ||   _/ \n|  |  ||   |   ||  _  ||  |   \n|  |  ||   |   ||  |  ||  |   \n|__|__||___|___||__|__||__|   \n                              ")
    print("CainSoulless\nv0.2 \nDate: ",today,"\nHour: ",now.hour,":",now.minute,":",now.second)

#  Only is running of '-c' option was in argv
def configurer(target):
    banner()
    #  if -c is on stdint create a configure file, and them writes with emails.
    if options.configurer is True:
        optionCommand = 0

        f = open("./configure.txt", "w+")
        sender = str(input("\n[-] Sender email: "))
        receiver = str(input("[-] Receiver email: "))
        o = input("[-] Want you to test the sender connection with Gmail?(y/n): ")

        if o == 'y' or 0 == 'yes':
            getpassword = getpass.getpass(prompt="\n[-] sender password: ")
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = ssl.create_default_context()) as s:
                try:
                    s.login(sender, getpassword)
                    print("[+] login success. Gmail account and credentials are fine!.")
                except:
                    print("\n[-] Login failed: Wrong email/password or perhaps Gmail account are not configured, yet.\n    https://myaccount.google.com/lesssecureapps")
                    sys.exit()

        #  Asks for an nmap command line option
        while optionCommand < 1 or optionCommand > 4:
            print("\n   - 1) Aggresive (nmap -p- -T5 -A %s)\n   - 2) Stealth (nmap -p- -sS -%s)\n   - 3) Fast (nmap -p- --open -T5 -v -n %s)\n   - 4) Custom\n" %(target, target, target))        
            optionCommand = int(input("[-] Nmap option command: "))
        
        if optionCommand == 1:
            command = 'nmap -T5 -p- -A'
        elif optionCommand == 2:
            command = 'nmap -sS -p- -A'
        elif optionCommand == 3:
            command = 'nmap -p- --open T5'
        elif optionCommand == 4:
            command = input("Enter command: ")

        #  All the information are stored onto configurer.txt
        f.write("%s\n" %sender)
        f.write("%s\n" %receiver)
        f.write("%s\n" %command)
        f.close()
        print("\n[+] Configured!")
        time.sleep(2)
#          if sys.argv[1] == '-c':
            #  target = str(input("[-] Target: "))
    else:
        try:
            f = open("configure.txt", 'r')
            if os.stat("configure.txt").st_size == 0:
                print("\n[-] No configure settings in file.")
                sys.exit()

            f.close()

        except:
            print("\n[-] Need configure:\n    Usage: python3 %s TARGET -c" %sys.argv[0])
            sys.exit()

def scanner(target):
    #  Opens config file and gets the nmap command(3rd line)
    f = open("configure.txt", "r")
    scanner.historyFile = ' -oN history/scan%s.txt' % (today)
    content = f.readlines()
    userCommandOption = content[2] + target + scanner.historyFile

    #  Start scanning
    subprocess.run(str.split(userCommandOption), shell = False)

    if os.path.exists(scanner.historyFile[5:]) == True:
        print("\n[+] File successful saved!")
        f.close()
        return True

#  Validate if the user has input a correct time.
def validate_time(set_alarm, alarm_hour, alarm_min, alarm_sec):
    if len(set_alarm) > 8:
        print("Please try a valid time format... ")
        return False
    else:
        if alarm_hour < 0 and alarm_hour > 24:
            print("Please try a valid HOUR...")
        elif alarm_min < 0 or alarm_min > 59:
            print("Please try a valid MINUTE...")
        elif alarm_sec < 0 or alarm_sec > 59:
            print("Please try a valid SECOND...")
        else:
            return True


# Function mantained around all the time until the clock is on the right time.
def wait_time(now):
    try:
        # Eternal loop waiting for the time previously implemented by the user
        while True:
            now = datetime.datetime.now()
            current_hour = int(now.strftime("%H"))
            current_min = int(now.strftime("%M"))
            current_sec = int(now.strftime("%S"))

            if current_hour == alarm_hour and current_min == alarm_min and current_sec == alarm_sec:
                return True
    except KeyboardInterrupt:
        print("\nBye!")

def send_email():
    f = open("configure.txt", 'r')
    content = f.readlines()
    
    #  Header
    msg = EmailMessage()
    msg["From"] = content[0]
    msg["To"] = content[1]
    msg["Subject"] = str("%s | %s | %s" %(target, today, now))
    msg.add_attachment(open(scanner.historyFile[5:], 'r'). read())

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = ssl.create_default_context()) as s:
            print("-------------------\n[-] smtp.gmail.com")
            try:
                s.login(content[0], getpassword)
                print("-------------------\n[-] login success.")
            except:
                print("-------------------\n[-] login failed: Wrong email or password.")
            s.send_message(msg)
            print("-------------------\n[+] Email sended.\n-------------------")
            print("Date: ",today, "\nHour: ",now.hour,":", now.minute,":", now.second)
            print("\nNext auto-scan in 24 hours.")
    except:
        print("\n[-] Emailing not completed...")
        sys.exit()
    wait_time(now)

if __name__ == "__main__":
    # Utility section.
    parser = OptionParser()
    parser.add_option('-c', '--configure',
                      help='Add the corresponding sender, receiver emails',
                      action='store_true',
                      dest='configurer')
    (options, args) = parser.parse_args()
    if len(sys.argv) < 2 or sys.argv[1] == '-c':
        banner()
        print("\n[-] TARGET missing!\n    Usage: python3 %s TARGET\n           python3 %s TARGET -c" %(sys.argv[0], sys.argv[0]))
        sys.exit()
    else:
        target = sys.argv[1]
        configurer(target)
    # Check if the history file exists
    try:
        check_output, retornoerror = '', ''
        outputmkdir = subprocess.check_output(["mkdir", "history" ], shell = False)
    except subprocess.CalledProcessError as retornoerror:
        if retornoerror.returncode == 1:
            print("[-] History file non exist!.")
            pass

    # Starts with the enviroments.
    banner()

    #  Get the password
    time.sleep(1)
    getpassword = getpass.getpass(prompt="\n[-] sender password: ")

    #Take the time.
    time.sleep(0.5)
    set_alarm = input("\n[-] Enter time in 'HH MM SS' format, or just 'now': ")

    # Recognize if the user input a real time, or just wants to start now.
    if len(set_alarm) == 8:
        #Assigns according to set_alarm position.
        alarm_hour = int(set_alarm[0:2])
        alarm_min = int(set_alarm[3:5])
        alarm_sec = int(set_alarm[6:8])
    elif set_alarm == "now" and len(set_alarm) == 3:
        alarm_hour = int(now.strftime("%H"))
        alarm_min = int(now.strftime("%M"))
        alarm_sec = int(now.strftime("%S")) + 10
        if alarm_sec >= 60:
            alarm_sec -= 60
            alarm_min += 1
    
    validate = validate_time(set_alarm.lower(), alarm_hour, alarm_min, alarm_sec)
    if validate != True:
        print(validate)
    else:
        print("[+] Done setting time for %s:%s:%s !" % (alarm_hour, alarm_min, alarm_sec))

    if wait_time(now) == True:
        scanner(target)
        send_email()
        sys.exit(1)
