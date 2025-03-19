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

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) #creates a connection to Gmail's SMTP server on port 587
        server.starttls()  #starts the TLS encryption
        server.login(sender_email, password)  
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        return "Email sent successfully!"

    except smtplib.SMTPAuthenticationError:
        return "Error: Incorrect email or password."
    except smtplib.SMTPRecipientsRefused:
        return "Error: Invalid recipient email address."
    except smtplib.SMTPException as e:
        return f"SMTP Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"
