import subprocess
import os,sys
import smtplib
import string
import random


#email and password goes here 
email_u=""
password_u="" 

file="COD4"
def sendmail(email,password,message):
    while True:
        try:
            server=smtplib.SMTP("smtp.gmail.com",587)
            break
        except Exception:
            continue
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()
def check_and_apply_perm():
    if(os.path.exists(file)):
        subprocess.call("icacls "+file+" /deny Everyone:(OI)(CI)(DE,DC)",shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)

def hide():
    if(os.path.exists(file)):
        subprocess.call("attrib +h +s "+file,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
        code=generate_code()
        sendmail(email_u,password_u,code)
        make_file(code)
def generate_code():
    letters=string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))
def make_file(cod):
    file=open('code.txt','w')
    file.write(cod)
    file.close
    subprocess.call("attrib +h +s code.txt",stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)

def have_file():
    file=open('code.txt','r')
    code=file.read()
    while True:
        x=input("enter code:")
        if x==code:
            subprocess.call("attrib -h -s COD4",stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
            break
        else:
            print("Wrong code Enter again")



check_and_apply_perm()
print("What to do \n 1) to delete press 1\n 2) to have file back press 2")
user=int(input("Enter: "))
if(user==1):
    hide()
elif(user ==2):
    have_file()
else: 
    print("Wrong input")
