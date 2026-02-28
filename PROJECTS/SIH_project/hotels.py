import requests
import sys
from math import radians, sin, cos, sqrt, atan2

GEOCODE_API_KEY = "66c7757c28938583789454xng952904"
GEOCODE_URL = "https://geocode.maps.co/search"
REVERSE_GEOCODE_URL = "https://geocode.maps.co/reverse"


def reverse_geocode(lat, lon):
    """Fetch address for a given latitude and longitude using reverse geocode API."""
    try:
        response = requests.get(REVERSE_GEOCODE_URL, params={"lat": lat, "lon": lon, "api_key": GEOCODE_API_KEY})
        response.raise_for_status()
        data = response.json()
        return data.get("display_name", "N/A")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching reverse geocode data: {e}")
        return "N/A"

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    lat1, lon1, lat2, lon2 = radians(lat1), radians(lon1), radians(lat2), radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def closestHotel(lat, lon, hotels, max_distance):
    closest_hotels = []
    
    for hotel in hotels:
        loc = hotel["location"]
        hotel_lat, hotel_lon = loc.split(",")
        hotel_lat, hotel_lon = float(hotel_lat), float(hotel_lon)
        print(hotel_lat,hotel_lon)
        distance = haversine(lat, lon, hotel_lat, hotel_lon)
        
        if max_distance is None or distance <= max_distance:
            hotel_info = hotel.copy()
            hotel_info['distance'] = distance
            closest_hotels.append(hotel_info)
    
    closest_hotels.sort(key=lambda x: x['distance'])
    
    return closest_hotels


def fetch_lat_long(address):
    try:
        response = requests.get(GEOCODE_URL, params={"q": address, "api_key": GEOCODE_API_KEY})
        response.raise_for_status()
        data = response.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
        else:
            print("No results found for the given address.")
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching geocode data: {e}")
        sys.exit(1)


def main():
    loc = input("Enter location where you want to find the hotel: ")
    lat, lon = fetch_lat_long(loc)
    print(f"Latitude: {lat}, Longitude: {lon}")
    
    url = "https://sky-scanner3.p.rapidapi.com/hotels/auto-complete"
    querystring = {"query": f"{loc}"}
    headers = {
        "x-rapidapi-key": "930dbfb1d6mshaca55b144689bcbp1537ccjsn819e3ddcbb87",
        "x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    hotels = response.json().get("data", [])
    
    if not hotels:
        print("No hotels found in the area.")
        sys.exit(1)
    
    max_distance = float(input("Enter the maximum distance (in km) to search for hotels: "))
    nearby_hotels = closestHotel(lat, lon, hotels, max_distance)
    
    if not nearby_hotels:
        print("No nearby hotels found within the specified distance.")
        sys.exit(1)
    
    # Assuming you want to print the closest hotel's entityId
    closest_hotel = nearby_hotels[0]
    entityId = closest_hotel.get("entityId", "N/A")
    print(f"Closest Hotel Entity ID: {entityId}")
    entityName = closest_hotel.get("entityName", "N/A")
    print(f"Closest Hotel Entity ID: {entityName}")
    

if __name__ == "__main__":
    main()
