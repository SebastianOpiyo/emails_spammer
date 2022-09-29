#!/usr/bin/env python 


# The link below handles most questions of Gitter.
# https://gitter.im/gophish/gophish?at=572d0298a351d8310951a2e4
import json
import jsonify
import requests

key = '3e35419d03ca86bd6dfa5e89f0e27a08d2832a7e452686c9068216a112e224a2'
url = "http://localhost:3333/api/templates"


def main_template():
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
    resp.raise_for_status()
    if resp.status_code != 204:
        templates = resp.json()
        for template in templates:
            print(template["id"], " - ", template["name"], " - ", template['modified_date'])
    print(f"No data was found")


if __name__ == "__main__":
    main_template()
