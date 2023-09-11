import os

import django
from django.test import Client

# simple script to test path requests and responses

os.environ.setdefault("_MODULE", "attackflow.settings")
django.setup()

c = Client()

# with open('../test.txt') as f:
#     # Request objects are different HttpRequest obejcts
#     # content is sent as a byte string for testing purposes
#     response = c.post('/upload_report/', {'file': f})
#     text = response.content.decode()
#     print(text)

response = c.post('/login_test/', {'username': 'test', 'password': 'test'})
print(response.content)
response = c.get('/login_test/')
print(response.content)

