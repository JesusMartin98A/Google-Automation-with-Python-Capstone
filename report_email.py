# Create another script to process supplier fruit description data from supplier-data/descriptions directory; call the generate_report method from the reports module.

#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def getparagraph(data_folder, file):
    with open(data_folder + file) as dict_string:
        fruit_dictionary = {}
        fruit_dictionary['name'] = dict_string.readline().strip()
        fruit_dictionary['weight'] = dict_string.readline().strip()
    name = "name: " + fruit_dictionary['name']
    weight = "weight: " + fruit_dictionary['weight']
    return f"{name}<br/>{weight}<br/><br/>"

if __name__ == "__main__":
    paragraph = ""
    for file in os.listdir("supplier-data/descriptions/"):
        if file.endswith(".txt"):
            paragraph += getparagraph("supplier-data/descriptions/", file)

    today = datetime.datetime.today()
    report_title = "Processed Update on {} {}, {}".format(today.strftime("%B"), today.day, today.year)

    reports.generate_report("/tmp/report.pdf", report_title, paragraph)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/report.pdf"
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
