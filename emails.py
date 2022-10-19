# Send the email using the emails.generate_email() and emails.send_email() methods.

#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, receiver, subject, body, attachment=None):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)

    if attachment:
        attachment_filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split("/", 1)

        with open(attachment, "rb") as ap:
            message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)

    return message

def send_email(message):
    mail_server = smtplib.SMTP("localhost")
    mail_server.send_message(message)
    mail_server.quit()
