![Screenshot from 2021-07-11 22-52-31](https://user-images.githubusercontent.com/38092779/125224132-fd73d580-e29a-11eb-8fa9-12b31fab7ef2.png)

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
Instructions: For now is necesarily to change the "sender", "receiver" and "target" variables in the source code, in the next update will be implemented a config.sh of something like that for only one configuration and not input all the time the target and emails. Just change the variables:
```
vi paranoidmap.py
python3 paranoidmap.py
```
![Screenshot from 2021-07-11 21-55-20](https://user-images.githubusercontent.com/38092779/125223761-4e36fe80-e29a-11eb-9bbf-e08c6c422874.png)

In the script just put the time in 24 hours format (HH:MM:SS AM/PM) and enter the password of email sender (not put it in a variable, just for security).

# Gmail configuration: 
The only important thing you need to do in your sender gmail is enable the "less secure app" function:
![Screenshot from 2021-07-11 21-54-07](https://user-images.githubusercontent.com/38092779/125223822-673faf80-e29a-11eb-8bc2-0299bdae8baa.png)

https://myaccount.google.com/lesssecureapps

And remove it from the spam section in the second email (receiver).
![Untitled design](https://user-images.githubusercontent.com/38092779/125223809-63139200-e29a-11eb-92b4-98e06a35477a.png)

# PD:
If you want to optimize the code or made contrubution send me a message. Thank you!.
(Lab 1 by the The Hacker Playbook 3).





