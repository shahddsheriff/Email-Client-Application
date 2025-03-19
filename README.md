==========================================
EMAIL CLIENT APPLICATION
==========================================

1. INTRODUCTION
----------------
The Email Client Application is a Python-based GUI tool that allows users to 
send and receive emails using their Gmail accounts. It features an intuitive 
interface for composing emails, checking the inbox, and receiving push 
notifications for new emails.

2. FEATURES
------------
- Send Emails – Users can compose and send emails.  
- Receive Emails – Users can check their inbox for new messages.  
- Push Notifications – The application notifies users of new emails using Plyer.  
- Login System – Secure authentication before accessing the email client.  
- Auto-Check Emails – The app checks for new emails every 30 seconds.  
- Graphical User Interface (GUI) – Built with Tkinter for an easy-to-use experience.  

3. DEPENDENCIES
----------------
This application requires the following Python libraries:

- smtplib – Sends emails using SMTP (built-in, no installation needed)
- email.mime – Formats email body & attachments (built-in, no installation needed)
- imaplib – Receives emails via IMAP (built-in, no installation needed)
- tkinter – GUI framework (built-in, no installation needed)
- plyer – Push notifications for new emails → Install with: `pip install plyer`
- ttk – Themed widgets for a better UI (built-in, no installation needed)

4. INSTALLATION
----------------
Before running the application, ensure that:
- You have Python 3.x installed.  
- You have `pip` (Python package manager) installed.  

To install dependencies, run:
pip install plyer

5. APPLICATION FILES
---------------------
The project consists of three main files:

- `send_email.py`
  - Handles email-sending using SMTP.
  - Function: `send_email(sender_email, password, recipient_email, subject, body)`

- `receive_email.py`
  - Handles receiving emails using IMAP.
  - Function: `receive_email(email_user, email_pass, check_new_only=False)`

- `gui.py`
  - Initializes the Graphical User Interface (GUI).
  - Functions:
    - `login()`: Handles login authentication.
    - `gui_send_email()`: Collects input and calls send_email().
    - `gui_receive_email()`: Calls receive_email() and displays messages.
    - `auto_check_email()`: Checks for new emails every 30 seconds.

6. RUNNING THE APPLICATION
---------------------------
To start the email client, open a terminal or command prompt and run:
python gui.py


7. HOW TO USE THE APPLICATION
------------------------------
1. Login – Enter your Gmail email and app password.
2. Send an Email:
   - Enter recipient details and message content.
   - Click the "Send Email" button.
3. Check Inbox:
   - Click the "Check Inbox" button.
   - A pop-up will display the latest email.
4. Automatic Email Checking:
   - The application auto-checks every 30 seconds.
   - If a new email arrives, a notification pops up.

8. TESTING & RESULTS
---------------------
- Send Email Test – Verified that emails are sent successfully.  
- Receive Email Test – Ensured inbox messages are fetched correctly.  
- Login System Test – Checked authentication handling.  
- Push Notifications Test – Verified that new emails trigger notifications.  

Test Case Results:
| Test Case                    | Expected Outcome                 | Actual Outcome | Status |
|------------------------------|---------------------------------|---------------|--------|
| Send Email (valid credentials) | Email sent successfully         | Passed        | ✅ |
| Send Email (wrong password)    | Error pop-up shown              | Passed        | ✅ |
| Check Inbox (valid credentials) | Latest email displayed          | Passed        | ✅ |
| Check Inbox (wrong password)   | Error pop-up shown              | Passed        | ✅ |
| Push Notifications (new email) | Notification appears            | Passed        | ✅ |

9. FUTURE IMPROVEMENTS
------------------------
- Add support for Yahoo, Outlook, and other email providers.  
- Implement message filtering and search functionality.  
- Introduce Dark Mode for improved UI experience.  

10. CONCLUSION
--------------
The Email Client Application provides a simple and user-friendly interface 
for managing emails. It ensures secure authentication, real-time notifications, 
and easy email handling, making it a great lightweight email management tool 
for personal use.

