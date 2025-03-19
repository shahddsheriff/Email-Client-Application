import tkinter as tk
from tkinter import messagebox, ttk
from send_email import send_email
from receive_email import receive_email
from plyer import notification
import smtplib

# Global Variables
user_email = ""
user_password = ""
main_window = None

def login():
    global user_email, user_password
    user_email = email_entry.get()
    user_password = password_entry.get()
    
    # Check if credentials are provided
    if not user_email or not user_password:
        messagebox.showerror("Login Error", "Please enter both email and password.")
        return
    
    # Verify login by trying to connect to SMTP
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user_email, user_password)
        server.quit()
        
        login_window.destroy()
        open_main_app()
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Login Error", "Invalid email or password.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

def gui_send_email():
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END)
    
    #Check if fields are empty
    if not recipient_email or not subject or not body.strip():
        messagebox.showerror("Error", "All fields are required!")
        return
    
    result = send_email(user_email, user_password, recipient_email, subject, body)
    messagebox.showinfo("Email Status", result)

def gui_receive_email():
    email_from, email_subject, email_body = receive_email(user_email, user_password)
    if email_from:
        messagebox.showinfo(f"Email from {email_from}", f"Subject: {email_subject}\n\n{email_body}")
    else:
        messagebox.showerror("Error", email_body)

# Function to Check Inbox & Notify Automatically
def auto_check_email():
    global main_window

    if user_email and user_password:
        email_from, email_subject, email_body = receive_email(user_email, user_password, check_new_only=True)

        #Only notify if a new email arrives
        if email_from:
            notification.notify(
                title="New Email Received",
                message=f"From: {email_from}\nSubject: {email_subject}",
                timeout=10
            )

    #Schedule the next auto-check in 30 seconds
    main_window.after(30000, auto_check_email)

def open_main_app():
    global recipient_entry, subject_entry, body_entry
    global main_window
    
    main_window = tk.Tk()
    main_window.title("Email Client")
    main_window.geometry("450x400")
    
    frame = ttk.Frame(main_window, padding=10)
    frame.grid(row=0, column=0)
    
    ttk.Label(frame, text="Recipient Email:").grid(row=0, column=0, sticky="w")
    recipient_entry = ttk.Entry(frame, width=40)
    recipient_entry.grid(row=0, column=1, pady=5)
    
    ttk.Label(frame, text="Subject:").grid(row=1, column=0, sticky="w")
    subject_entry = ttk.Entry(frame, width=40)
    subject_entry.grid(row=1, column=1, pady=5)
    
    ttk.Label(frame, text="Message:").grid(row=2, column=0, sticky="nw")
    body_entry = tk.Text(frame, width=40, height=5)
    body_entry.grid(row=2, column=1, pady=5)
    
    send_button = ttk.Button(frame, text="Send Email", command=gui_send_email)
    send_button.grid(row=3, column=0, pady=10, padx=5, sticky="ew")
    
    receive_button = ttk.Button(frame, text="Check Inbox", command=gui_receive_email)
    receive_button.grid(row=3, column=1, pady=10, padx=5, sticky="ew")

    # Auto-check email every 30 seconds
    main_window.after(30000, auto_check_email)   

    main_window.mainloop()

# Login Window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("350x200")

ttku = ttk.Frame(login_window, padding=10)
ttku.grid(row=0, column=0)

ttk.Label(ttku, text="Email:").grid(row=0, column=0, sticky="w")
email_entry = ttk.Entry(ttku, width=30)
email_entry.grid(row=0, column=1, pady=5)

ttk.Label(ttku, text="Password:").grid(row=1, column=0, sticky="w")
password_entry = ttk.Entry(ttku, width=30, show="*")
password_entry.grid(row=1, column=1, pady=5)

login_button = ttk.Button(ttku, text="Login", command=login)
login_button.grid(row=2, column=1, pady=10, sticky="ew")

login_window.mainloop()
