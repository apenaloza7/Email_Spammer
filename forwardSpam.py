import smtplib
import time
import random
import sys

from email.header import Header
from email.mime.text import MIMEText
#Open a file for reading

myEmail = '' # change to your email
p_reader = open('password.txt', 'rb') # edit for your password
cipher = p_reader.read()
recipients = [''] # enter recipients here

def exitMessage():
        print('Done!')

def spam():
            
    stopCount = 50     # Used to set a number to stop at
    stopCounter = 0     # DO NOT EDIT
    emailsSent = 0      # DO NOT EDIT

    while (True):
        fp = open('message.txt', 'rb')

        # Multipart class is for multiple recipients
        msg = MIMEText(fp.read(), 'plain', 'utf-8')
        fp.close()

        thread_number = random.randint(0, 10000)
        msg['Subject'] = Header('Minutely Spam Report (randomizer: ' + str(thread_number) + ')', 'utf-8')
        msg['From'] = myEmail
        msg['To'] = ', '.join(recipients)

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(myEmail, cipher)
        s.sendmail(myEmail, recipients, msg.as_string())

        if stopCounter == stopCount:
                exitMessage()
                sys.exit()
        else:
                stopCounter += 1  # Add 1 to the stop count
                emailsSent += 1
                print('Email sent to: ' + ', '.join(recipients) + ' \n Total emails sent:  ' + str(emailsSent))
                s.quit()
                # time.sleep(1) # Change rate of fire here   Got rid of this to be as annoying as possible
        
spam()