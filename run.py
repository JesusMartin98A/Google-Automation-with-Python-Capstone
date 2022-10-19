# Write a Python script named run.py to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library.

#!/usr/bin/env python3

import os
import requests

def descriptionstojson(data_folder):
    for file in os.listdir(data_folder):
        if file.endswith(".txt"):
            with open(data_folder + file) as dict_string:
                fruit_dictionary = {}
                fruit_dictionary['name'] = dict_string.readline().strip()
                fruit_dictionary['weight'] = int(dict_string.readline().strip().strip(" lbs")) # Drop "lbs" and convert number to an integer
                fruit_dictionary['description'] = dict_string.readline().strip()
                fruit_dictionary['image_name'] = os.path.splitext(file)[0] + ".jpeg"
                r = requests.post('http://localhost/fruits/', json=fruit_dictionary)
                print(r.request.body)
                print(r.status_code)

descriptionstojson("supplier-data/descriptions/")

# The final JSON object should be similar to: {"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}
