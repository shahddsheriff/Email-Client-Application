import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(sender_email, password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587) #creates a connection to Gmail's SMTP server on port 587
        server.starttls()  #starts TLS connection for 
        server.login(sender_email, password)  
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    sender_email = "shahddsheriff@gmail.com"
    password = "znqd vhtb jlon tmke"
    recipient_email = "shahddsheriff@gmail.com"
    subject = "Test Email"
    body = "This is a test email sent from Python."
    send_email(sender_email, password, recipient_email, subject, body)