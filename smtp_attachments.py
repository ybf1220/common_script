#!/usr/bin/env python
# -*- coding:utf-8 -*-
#smtp_attachments.py
#auth@:binfang.ye
#date@:2015-02-12

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

path = ""
recipients = ["",""]

def delete_file(path):
  for f in os.listdir(path):
    file=os.path.join(path,f)
    if os.path.isfile(file): 
      os.remove(file) 
      #print " %s has been deleted" %os.path.basename(file)

def send_mail(path):
  _smtp_server = ""
  _user = ""
  _pwd  = ""
  _recipients = recipients

  msg = MIMEMultipart()
  msg["Subject"] = "Subject"
  msg["From"]    = _user
  msg["To"]      = ",".join(_recipients)
  part = MIMEText("content")
  msg.attach(part)
  for f in os.listdir(path):
    file=os.path.join(path,f)
    if os.path.isfile(file):
      part = MIMEApplication(open(file,'rb').read())
      part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
      msg.attach(part)
      #print " %s has added to mail attactment" %os.path.basename(file)

  s = smtplib.SMTP(_smtp_server, timeout=25)
  #s.set_debuglevel(1)
  s.login(_user, _pwd)
  s.sendmail(_user, _recipients, msg.as_string())
  s.close()
  print " mail send successfully!"

if __name__ == "__main__":
  ## this loop judge if the path is empty or not.
  for f in os.listdir(path):
    file=os.path.join(path,f)
    if os.path.isfile(file):
      send_mail(path)
      delete_file(path)
      os._exit(0)
  print "the path %s is empty!" % path
