import json
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class SendMail:

    def __init__(self):
        file = open("settings.txt", "r", encoding="utf-8")
        settings = json.load(file)
        file.close()

        now = datetime.now()
        fileName = now.strftime('%d-%m-%Y')

        email_user = settings['mail']['emailID']
        email_password = settings['mail']['password']
        email_send = settings['mail']['recipient']

        grade = settings['class']
        section = settings['section']

        subject = f'Attendance for class {grade} - {section}'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = f'Hi there, this is a mail from automated attenedance system. Attendance file for class {grade} - {section} on {fileName} is attached below'
        msg.attach(MIMEText(body,'plain'))

        filename = f'attendance/{fileName}.csv'
        attachment = open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()