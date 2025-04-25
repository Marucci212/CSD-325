# Justin Marucci
# Assignment 9

import requests
response = requests.get('http://www.google.com')
print(response.status_code)
