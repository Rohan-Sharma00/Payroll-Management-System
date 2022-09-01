import smtplib
from email.message import EmailMessage
from django.core.mail import send_mail


 # creates SMTP session
s = smtplib.SMTP('smtp.office365.com', 587)
# start TLS for security
s.starttls()
a = "PFA Salary Slip OF Bhavesh Khandelwal"
msg = EmailMessage()
msg['Subject'] = 'Salary Slip'
msg['From'] = 'bhavesh.khandelwal@indiraicem.ac.in'
msg['To'] = 'khandelwal.bhavesh0@gmail.com'
msg.set_content(a)
s.login("bhavesh.khandelwal@indiraicem.ac.in", "Xox25042")

s.send_message(msg)
s.quit()
print("email send successfully")