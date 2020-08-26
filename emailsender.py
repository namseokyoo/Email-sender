from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib


#계정설정
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

SMTP_USER = "namseok.yoo@gmail.com"
SMTP_PASSWORD = "qdwgmzuwivmfbeee"

# def is_vslid(addr)

def send_mail(addr,subj_layout, cont_layout, attachment=None):
  msg =MIMEMultipart("alternative")
  
  msg["From"] = SMTP_USER
  msg["To"] = addr
  msg["Subject"] = subj_layout
  
  contents = cont_layout
  text = MIMEText(_text = contents, _charset = "utf-8")
  msg.attach(text)
  
  
  smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
  
  smtp.login(SMTP_USER, SMTP_PASSWORD)
  
  smtp.sendmail(SMTP_USER, addr, msg.as_string())
  
  smtp.close()
  

  
  
  
  
  
  
  
  
  
  
  
  
  
