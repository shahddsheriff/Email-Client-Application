import imaplib
import email

IMAP_SERVER = "imap.gmail.com"  
IMAP_PORT = 993

def receive_email(email_user, email_pass):
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_user, email_pass)
        mail.select('inbox')
        
        result, data = mail.search(None, 'ALL')
        mail_ids = data[0].split()
        latest_email_id = mail_ids[-1]
        result, data = mail.fetch(latest_email_id, '(RFC822)')
        
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    print("Latest Email:")
                    print(part.get_payload(decode=True).decode())
        else:
            print("Latest Email:")
            print(msg.get_payload(decode=True).decode())
        
        mail.logout()
    except Exception as e:
        print(f"Error receiving email: {e}")

if __name__ == "__main__":
    email_user = "shahddsheriff@gmail.com"
    email_pass = "znqd vhtb jlon tmke"
    receive_email(email_user, email_pass)
