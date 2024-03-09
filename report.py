import smtpdlib
import schedule
import time

def send_email():
    # configs
    sender_email = ''
    receiver_email = ''
    password = ''

    # read email template


    # send email


# check every minute
while True:
    schedule.run_pending()
    time.sleep(10800)
