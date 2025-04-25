import requests
import json

# URL for the joke API
joke_url = 'https://official-joke-api.appspot.com/random_joke'

# Send GET request to retrieve a random joke
response = requests.get(joke_url)

# Print raw response
print("Raw Response:")
print(response.text)

# Print formatted response (JSON)
print("\nFormatted Response:")
joke_data = response.json()  # Convert response to JSON
print(json.dumps(joke_data, indent=4))
