import smtplib
from email.mime.text import MIMEText
from tour import *

def Gmail():
    Tour = tour()
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login('qorehduf3@gmail.com','jvljgoaecwgljjxe')

    msg = MIMEText(str(Tour.makeAreaCode()))
    msg['Subject'] = '테스트'
    msg['To'] = 'honey1586@naver.com'
    s.sendmail('qorehduf3@gmail.com','honey1586@naver.com',msg.as_string())

    s.quit()