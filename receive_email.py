import imaplib
import email
from plyer import notification

IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993

last_email_id = None  

def receive_email(email_user, email_pass, check_new_only=False):
    global last_email_id  

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(email_user, email_pass)
        mail.select("inbox")

        result, data = mail.search(None, "ALL")
        mail_ids = data[0].split()
        latest_email_id = mail_ids[-1]  # Get newest email ID

        # When auto-checking, notify only if a new email arrived
        if check_new_only and last_email_id == latest_email_id:
            return None, None, "No new emails."

        # Update last seen email ID
        last_email_id = latest_email_id  

        # Always fetch the latest email (for manual check)
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        email_from = msg["from"]
        email_subject = msg["subject"]

        email_body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    email_body = part.get_payload(decode=True).decode()
        else:
            email_body = msg.get_payload(decode=True).decode()

        return email_from, email_subject, email_body
    except Exception as e:
        return None, None, f"Error receiving email: {e}"