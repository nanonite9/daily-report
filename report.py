import smtplib
import schedule
import time
from config import EMAIL_CONFIG
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # configs
    sender_email = ''
    receiver_email = ''
    password = ''

    # message container
    msg = MIMEMultipart('alt')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Welcome to my Daily Report'

    # read email template
    with open('template.html', 'r') as file:
        email_content = file.read()

    msg.attach(MIMEText(email_content, 'html'))

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# run daily
schedule.every().day.at("22:00").do(send_email)

# check every minute
while True:
    schedule.run_pending()
    time.sleep(10800)
