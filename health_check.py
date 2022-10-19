# Write a script that will send an email if CPU usage is over 80%, available disk space is lower than 20%, available memory is less than 500 MB or the hostname "localhost" cannot be resolved to "127.0.0.1".

#!/usr/bin/env python3

import os
import emails
import psutil
import socket

if psutil.cpu_percent(1) < 80 and psutil.disk_usage('/')[3] < 80 and psutil.virtual_memory()[1]/1024**2 > 500 and socket.gethostbyname("localhost") == "127.0.0.1":
    print("Everything is ok!")

if psutil.cpu_percent(1) > 80 or psutil.disk_usage('/')[3] > 80 or psutil.virtual_memory()[1]/1024**2 < 500 or socket.gethostbyname("localhost") != "127.0.0.1":
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = ""
    if psutil.cpu_percent(1) > 80:
        subject += "Error - CPU usage is over 80%"
    if psutil.disk_usage('/')[3] > 80:
        subject += "Error - Available disk space is less than 20%"
    if psutil.virtual_memory()[1]/1024**2 < 500: # I have to convert bytes to MB
        subject += "Error - Available memory is less than 500MB"
    if socket.gethostbyname("localhost") != "127.0.0.1":
        subject += "Error - localhost cannot be resolved to 127.0.0.1"
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body, attachment=None)
    emails.send_email(message)
