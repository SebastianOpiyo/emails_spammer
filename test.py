#!/usr/bin/env python 


# The link below handles most questions of Gitter.
# https://gitter.im/gophish/gophish?at=572d0298a351d8310951a2e4
import json
import requests

key = "703d6d6d4f3c5fbc00861221333f5c3960f5971b3bebfc7928ce014e78dab579"
url = "http://localhost:3333/api/templates"

print("\nList of names of the current templates:\n")
resp = requests.get(url + "?api_key=" + key)
templates = resp.json()
for template in templates:
        print(template["id"], "- ", template["name"], " - ", template['modified_date'])

# New template data
t_data = {
  "id": 27,
  "name": "Example Template",
  "subject": "Example email template subject",
  "text": "This is a test message!",
  "html": "<html><head></head><body>This is a test message!</body></html>",
  "attachments": [
    {
      "id": 1,
      "name": "Example Attachment",
      "content": "Hello, world!",
      "type": "text/plain"
    }
  ],
#  "modified_date": "2015-01-01T01:02:03.000000Z"
}

print("\nPOSTing new item...") 
resp = requests.post(url + "?api_key=" + key, t_data)
print("\nStatus: ")
print(resp.status_code)

print("\nList of names of the current templates:\n")
resp = requests.get(url + "?api_key=" + key)
templates = resp.json()
for template in templates:
        print(template["id"], " - ", template["name"], " - ", template['modified_date'])