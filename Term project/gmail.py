import smtplib
from email.mime.text import MIMEText

def Gmail():
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login('qorehduf3@gmail.com','jvljgoaecwgljjxe')

    msg = MIMEText("내용: 본문내용 테스트입니다.")
    msg['Subject'] = '제목: 메일 보내기 테스트입니다.'
    msg['To'] = 'honey1586@naver.com'
    s.sendmail('qorehduf3@gmail.com','honey1586@naver.com',msg.as_string())

    s.quit()