# Take the jpeg images from the supplier-data/images directory that you've processed and upload them to the [linux-instance-IP-Address]/upload URL.

#!/usr/bin/env python3

import requests
import os

def upload(file, url):
    with open(file, "rb") as opened:
        r = requests.post(url, files={'file': opened})

for file in os.listdir("supplier-data/images/"):
    if file.endswith(".jpeg"):
        upload("supplier-data/images/" + file, "http://localhost/upload/")
