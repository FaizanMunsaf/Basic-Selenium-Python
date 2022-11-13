# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:48:04 2022

@author: Faizan
"""
from email.message import EmailMessage
import ssl
import smtplib

sender_email = "email.tester.faizan@gmail.com"
email_password = "hcbsqtdwdpniazgg"
reciver_email = "faizanmunsafcode@gmail.com"

subject = "Check out my video"

body = '''
    Here is python code you may check it out
'''

em = EmailMessage()

em['From'] = sender_email
em['To'] = reciver_email
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(sender_email, email_password)
    smtp.sendmail(sender_email, reciver_email, em.as_string())