# Justin Marucci 
# Assignment 9.2

import requests

# Test Connection 
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
print("Astronaut API Test:" , response.status_code

# Raw Response 
print("\nFormatted Output:")
print(response.text)

# Formatted Output
print("\nFormatted Output:")
data = response.json ()
print(f"There are {data['number']} astronauts in space right now:\n")
for person in data["people"]
    print(f"{person['name']} is on the {person['craft']}")
