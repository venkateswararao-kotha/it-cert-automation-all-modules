#!/usr/bin/env python3

import emails
import os
import reports

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "Hi\n\nAll fruits are uploaded to our website successfully. A detailed list is attached to this email."

message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
emails.send(message)
