import smtplib
from_addr = 'anymail@gmail.com'
to_addr = 'wigsur@gmail.com'
message = """From: {Fitz} <anymail@gmail.com>
To: {Cam} <wigsur@gmail.com> 
Subject: Lab 3 Test, let me know if you get it
Body
"""
# Credentials (if needed)
username = 'anymail@gmail.com'
password = 'password'
 
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message)
server.quit()