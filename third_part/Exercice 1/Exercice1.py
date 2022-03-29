
import requests
r = requests.post('https://httpbin.org/anything', json={"key": "value"})
r.status_code



import requests
import json

r = requests.post(
    "https://httpbin.org/anything",
    data=json.dumps({"key": "value"}),
    headers={"Content-Type": "application/json"},
)

r = requests.post('https://httpbin.org/anything', json={'key':'value'})

r.text

import requests

url = 'https://httpbin.org/anything'

# Get a copy of the default headers that requests would use
headers = requests.utils.default_headers()

# Update the headers with your custom one

headers.update(
    {
        'User-Agent': 'python-requests/2.23.0',
    }
)

response = requests.get(url, headers=headers)

