import requests

# Your TransitLand API key
api_key = 'H7yXGinjuKw6SykxsKyLPsKN6HEYkqIX'

# Endpoint URL for Transit Stops
url = 'https://transit.land/api/v1/stops'

# Parameters for the API request
params = {
    'lat': '40.7128',  # Latitude for New York City
    'lon': '-74.0060', # Longitude for New York City
    'r': '500',        # Radius in meters
    'apikey': api_key
}

# Make the API request
response = requests.get(url, params=params)

# Print the status code and content for debugging
print(f"Status Code: {response.status_code}")
print(f"Response Content: {response.text}")

# Check if the request was successful before parsing JSON
if response.status_code == 200:
    try:
        stops = response.json()
        print("Stops data:", stops)
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response content was not in JSON format.")
else:
    print(f"Error: {response.status_code}, {response.text}")
