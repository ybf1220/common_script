#!/usr/bin/python
#coding:utf-8

import smtplib 
from email.mime.text import MIMEText 
import sys 

mail_host = ''
mail_user = ''
mail_pass = ''
mail_postfix = ''

def send_mail(to_list,subject,file): 
    me = mail_user
    file_object = open(file)  
    try:  
        mail_content = file_object.read()  
    finally:  
        file_object.close( ) 
    msg = MIMEText(mail_content) 
    msg['Subject'] = subject 
    msg['From'] = me 
    msg['to'] = ",".join(to_list) 

    try: 
        s = smtplib.SMTP()
        #s.set_debuglevel(1)
        s.connect(mail_host) 
        s.login(mail_user,mail_pass) 
        s.sendmail(me,to_list,msg.as_string()) 
        s.close() 
        return True
    except Exception,e: 
        print str(e) 
        return False

if __name__ == "__main__": 
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
