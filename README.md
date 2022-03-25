<img src='https://github.com/CainSoulless/paranoidmap/blob/main/images/Screenshot%20from%202022-03-25%2002-16-36.png'>

# ParanoidMap
Paranoidmap, script writen in python that automate ports scan with nmap depending on the time you indicate, creating an txt file with the output and sending it in a email as notification system on pentesting or Red Teaming operations. In some times you want to automate the recon phase while having an history about the port schedule of the target.

# Installation:

The modules used has been installed by default in a system, but in case of need exist a "requirement.txt" in the repository. (Optional) Run the following command below:
```
pip install -r requirement.txt
```
Clone the repository with git:
```
git clone https://github.com/CainSoulless/paranoidmap
cd /paranoidmap
```
# Gmail configuration: 
The only important thing you need to do in your sender gmail is enable the "less secure app" function:
![Screenshot from 2021-07-11 21-54-07](https://user-images.githubusercontent.com/38092779/125223822-673faf80-e29a-11eb-8bc2-0299bdae8baa.png)

https://myaccount.google.com/lesssecureapps

And remove it from the spam section in the second email (receiver).
![Untitled design](https://user-images.githubusercontent.com/38092779/125223809-63139200-e29a-11eb-92b4-98e06a35477a.png)

# Usage:
If the gmail account was not configured properly, the program could not access to the sender account and sends the file.
The program can be configured with the '-c' option:
```
python3 paranoidmap.py TARGET -c
```
Into it you can input the email accounts, select or type a custom nmap command option.
The normal use is:
```
python3 paranoidmap.py TARGET
```
In the program just put the time in 24 hours format (HH MM SS), or just typing 'now', and enter the password of the sender email.

# PD:
If you want to optimize the code or made contrubution send me a message. Thank you!.
(Lab 1 by the The Hacker Playbook 3).
