# import requests

# params = {
#     'access_key': '12919ccf4267b2aa7bf52b93c649831c'
# }

# api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

# api_response = api_result.json()

# print(api_response)

# import requests

# params = {
#     'access_key': '12919ccf4267b2aa7bf52b93c649831c'  
# }

# api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

# api_response = api_result.json()

# for flight in api_response['data']:
#     flight_date = flight.get('flight_date')
#     airline = flight['airline'].get('name')
#     flight_number = flight['flight'].get('number')
#     departure_airport = flight['departure'].get('airport')
#     arrival_airport = flight['arrival'].get('airport')
#     flight_status = flight.get('flight_status')
    
#     print(f"Flight Date: {flight_date}")
#     print(f"Airline: {airline}")
#     print(f"Flight Number: {flight_number}")
#     print(f"Departure Airport: {departure_airport}")
#     print(f"Arrival Airport: {arrival_airport}")
#     print(f"Flight Status: {flight_status}")
#     print("="*40)

# import requests
# from Hotel_intergration import fetch_lat_long, reverse_geocode
# from math import radians, sin, cos, sqrt, atan2

# def findIOTA(place,key):
#     params = {
#     'access_key': '12919ccf4267b2aa7bf52b93c649831c'  
#     }

#     req = requests.get('https://api.aviationstack.com/v1/airports', params)
#     data=req.json().get("data",[])
#     # print(data)
#     for airport in data:
#         if airport.get("country_name") == place:
#             print(f"Airport Name: {airport.get('airport_name')}, IATA Code: {airport.get('iata_code')}")
#     print(f"No airport found in {place}")
    

# def haversine(lat1, lon1, lat2, lon2):
#     # Haversine formula to calculate distance between two coordinates
#     R = 6371.0 # Earth radius in kilometers
#     lat1, lon1, lat2, lon2 = radians(lat1), radians(lon1), radians(lat2), radians(lon2)
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     distance = R * c
#     return distance

# def closestAirports(lat, lon, airports, max_distance):
#     nearest_airport = None
#     min_distance = float('inf')
    
#     for airport in airports:
#         airport_lat = float(airport['latitude'])
#         airport_lon = float(airport['longitude'])
#         distance = haversine(lat, lon, airport_lat, airport_lon)
        
#         if distance < min_distance:
#             min_distance = distance
#             nearest_airport=airport
    
#     return nearest_airport
        


# def main():
#     key="12919ccf4267b2aa7bf52b93c649831c"
#     departure=input("From where do you want to depart ")
#     lat, lon = fetch_lat_long(departure)
#     print(lat, lon)
#     # arrive=input("Where to arrive ")
#     params = {
#     'access_key': key  
#     }

#     response = requests.get('https://api.aviationstack.com/v1/airports', params=params)
    
#     if response.status_code != 200:
#         print("Error fetching airport data")
#         return
    
#     airports = response.json().get("data", [])
#     if not airports:
#         print("No airports found.")
#         return
#     max_distance = 3500  # Example: 1000 kilometers
#     closest_airports = closestAirports(lat, lon, airports, max_distance)
    
#     if closest_airports:
#         print(f"Airports within {max_distance} km of {departure}:")
#         for airport in closest_airports:
#             lat,lon=airport['latitude'], airport['longitude']
#             print(f"{airport['airport_name']} located at {reverse_geocode(lat,lon)} - Distance: {airport['distance']:.2f} km")
#     else:
#         print(f"No airports found within {max_distance} km of {departure}.")
    
    
# if __name__=="__main__":
#     main()



import requests
from math import radians, sin, cos, sqrt, atan2
from Main_Hotel_intergration import fetch_lat_long
from Main_Hotel_intergration import reverse_geocode


def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  
    lat1, lon1, lat2, lon2 = radians(lat1), radians(lon1), radians(lat2), radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def closestAirports(lat, lon, airports, max_distance=None):
    closest_airports = []
    
    for airport in airports:
        airport_lat = float(airport['latitude'])
        airport_lon = float(airport['longitude'])
        distance = haversine(lat, lon, airport_lat, airport_lon)
        
        if max_distance is None or distance <= max_distance:
            airport_info = airport.copy()
            airport_info['distance'] = distance
            closest_airports.append(airport_info)
    

    closest_airports.sort(key=lambda x: x['distance'])
    
    return closest_airports

def start1():
    api_key = "12919ccf4267b2aa7bf52b93c649831c"
    departure = input("From where do you want to depart? ").capitalize()
    lat, lon = fetch_lat_long(departure)
    # print(f"Coordinates of {departure}: Latitude = {lat}, Longitude = {lon}")
    
    params = {
        'access_key': api_key,
        'limit': 100,  
    }

    response = requests.get('https://api.aviationstack.com/v1/airports', params=params)
    
    if response.status_code != 200:
        print("Error fetching airport data")
        return
    
    airports = response.json().get("data", [])
    if not airports:
        print("No airports found.")
        return

    max_distance = int(input('Select radius or defaultly have it 2000km '))  
    closest_airports = closestAirports(lat, lon, airports, max_distance)
    
    if closest_airports:
        print(f"Airports within {max_distance} km of {departure}:")
        for i, airport in enumerate(closest_airports):
            lat, lon = airport['latitude'], airport['longitude']
            print(f"{i + 1}. {airport['airport_name']} located at {reverse_geocode(lat, lon)} - Distance: {airport['distance']:.2f} km")
        try:
            choice = int(input(f"Select the suitable airport for the service among (1-{len(closest_airports)}): "))
            if 1 <= choice <= len(closest_airports):
                selected_airport = closest_airports[choice - 1]
                print(f"You selected {selected_airport['airport_name']}.")
                print(f"Latitude: {selected_airport['latitude']}, Longitude: {selected_airport['longitude']}")
                print(f"Distance: {selected_airport['distance']:.2f} km")
                return selected_airport['airport_name'], selected_airport['iata_code']
                
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"No airports found within {max_distance} km of {departure}.")
    
if __name__ == "__main__":
    name,code=start1()

