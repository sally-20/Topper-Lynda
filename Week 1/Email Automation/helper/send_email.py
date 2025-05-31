import os
import ssl
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

def send_email(recipient: str, subject: str, body: str) -> None:
    msg = EmailMessage()
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(os.environ["SMTP_SERVER"], int(os.environ["SMTP_PORT"]), context=context) as server:
        server.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
        server.send_message(msg)
