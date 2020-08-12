#!/usr/bin/env python3
#import emails
import os
import psutil
import socket
import email.message
import mimetypes
import os.path
import smtplib

email_flag = False

def generate(sender, recipient, subject, body):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    return message

def send(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()


# gives a single float value
if psutil.cpu_percent() > 80:
    subject = "Error - CPU usage is over 80%"
    email_flag = True
elif round(psutil.disk_usage('/').percent, 2) < 20:
    subject = "Error - Available disk space is less than 20%"
    email_flag = True
elif psutil.virtual_memory()._asdict()['free'] < 500000000:
    subject = "Error - Available memory is less than 500MB"
    email_flag = True
elif socket.gethostbyname('localhost') != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    email_flag = True


if email_flag:
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    message = generate(sender, receiver, subject, body)
    send(message)
