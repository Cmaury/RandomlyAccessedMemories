import os
from random import choice
import smtplib
from email.mime.text import MIMEText

dir = #where you store your saved ideas
files = os.listdir(dir)
file = choice(files)

fp = open(dir + '/' + file, 'rb')
msg = MIMEText(fp.read())
fp.close()

msg['Subject'] = 'Randomly Accessed %s' % file
msg['From'] = 'youremail@mail.com'
msg['To'] = 'youremail@mail.com'

server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login('yourgmail@gmail.com','your password')

server.sendmail('youremail@email.com',['youemail@mail.com'], msg.as_string())
server.quit()