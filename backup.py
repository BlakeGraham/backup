# /user/bin/env python3 back.py blakewgraham12@gmail.com
from backupcfg import jobs# wont work if importing only backupcfg 
import sys
import os
import os.path
import shutil
from datetime import datetime
import pathlib
import ssl 
import smtplib
#imports

dstDir = "/home/ec2-user/environment/backups/"
timestamp = datetime.now().strftime("%Y,%m,%d,%H:%M:%S") #current date and time being added to file

backuplog =open('backup.log','a')#opens a back upm log to be written im

def email(body):#defineing email
    
    content = "Subject: backup success/error\n\n" + body +"\n"
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
        server.login("blakewgraham12@gmail.com","olhibimpscshwhhm")#what email and pasword it is sending from
        server.sendmail("blakewgraham12@gmail.com","blakewgraham12@gmail.com",content)#what email is receving

if len(sys.argv)<2:
    
    print('usage: not enough arguments')
 #check if there are enough agruments
else:

    job=sys.argv[1]
    #check to see if job eneterd exists
    if not job in jobs:
        print('error: job not valid')
        backuplog.write('FAIL wrong number of arguments '+ str(sys.argv)+ timestamp +'\n')
        email('wrong number of arguments '+ str(sys.argv)+ timestamp)        
                                    
    else:
        srcloc=jobs[job]        #serchers for job in backupcfg.py
        srcpath=pathlib.PurePath(srcloc)
        print(srcloc)
        
        #removes(./) from filename
        dstloc = dstDir + srcpath.name + '-' + timestamp #adds timestamp to the file/directories
        print(dstloc)
            
            
        if pathlib.Path(srcloc).is_dir():
            try:
                shutil.copytree(srcloc,dstloc)#trying to create a back up
                backuplog.write(" SUCCESS the program has succeded in making a copy of directories " + timestamp + '\n') #prints in backup log if success
                email(" the program has succeded in making a copy of directories " + timestamp + '\n')#sends email if succss
            except:#when copy fails
                print("error" + job + ' has failed')
                backuplog.write(' FAIL the program has failed copying directoies '+ timestamp +'\n') #prints in backup log if fails\
                email(' the program has failed copying directoies '+ timestamp +'\n')#sends email if fail
              
        else:
            try:
                shutil.copy2(srcloc,dstloc)#
                backuplog.write(" SUCCESS the program has succeded in making a copy of file1 " + timestamp + '\n')      
                email(" the program has succeded in copying file1 " + timestamp + '\n')
            except:
                print("error" + job + ' has failed')                 
                backuplog.write(' FAIL the program has failed in making a copy of file1 '+ timestamp + '\n')
                email(' the program has failed in making a copy of file1 '+ timestamp +'\n')
          
backuplog.close() #closes the backup log
        
  