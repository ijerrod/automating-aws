# coding: utf-8
import requests
url = '' # Replace with slack webhook URL
data = { "text": "Testing Slack notifications." }
requests.post(url, json=data)
