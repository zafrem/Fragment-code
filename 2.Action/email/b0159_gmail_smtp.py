import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "your_email@gmail.com"
password = "your_password"

from_address = "your_email@gmail.com"  # Send email
to_address = "recipient_email@example.com"  # Recv email

# MIME email Create
message = MIMEMultipart()
message['From'] = from_address
message['To'] = to_address
message['Subject'] = "SMTP Email Test"

# Main text
body = "Python email example."
message.attach(MIMEText(body, 'plain'))

#attach file
attach_file = open('Report.doc','rb')
attach_mime = MIMEBase('application','octet-stream')
attach_mime.set_payload((attach_file).read())
encoders.encode_base64(attach_mime)
message.add_header('Content-Disposition', "attachment; filename= " + "Report.doc")
message.attach(attach_mime)
# SMTP Server connection and Send mail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # TLS(Transport Layer Security)
    server.login(username, password)  # login
    server.send_message(message)  # Send Mail
    print("Success")
except Exception as e:
    print(f"Fail: {e}")
finally:
    server.quit()  # SMTP Terminate
