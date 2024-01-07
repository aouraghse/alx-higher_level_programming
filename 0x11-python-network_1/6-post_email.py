#!/usr/bin/env python3
"""
A Python script that:
- takes in a URL,
- sends a POST request to the URL with an email parameter,
- and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
	url = sys.argv[1]
	email = sys.argv[2]

	data = {'email': email}
	response = requests.post(url, data=data)

	print("Your email is: {}".format(email))
	print(response.text)
