import requests

def get_flights(dep, arr, y, m, c, a, ch, inf, Class):
    flights = []    
    cabin_classes = {1: "Economy", 2: "Premium Economy", 3: "Business", 4: "First"}
    Class = cabin_classes.get(Class, "Economy")
    
    url = "https://sky-scanner3.p.rapidapi.com/flights/search-everywhere"
    querystring = {
        "fromEntityId": dep, 
        "toEntityId": arr,
        "year": y, 
        "month": m, 
        "currency": c, 
        "adults": a, 
        "children": ch, 
        "infants": inf, 
        "cabinClass": Class
    }

    headers = {
        "x-rapidapi-key": "930dbfb1d6mshaca55b144689bcbp1537ccjsn819e3ddcbb87",
        "x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json().get("data", {})
    
    result = data.get("flightQuotes", {}).get("results", [])
    
    for i, flight in enumerate(result, 1):
        flight_info = {
            "price": flight["content"]["price"],
            "raw_price": flight["content"]["rawPrice"],
            "dep_date": flight["content"]["outboundLeg"]["localDepartureDate"],
            "label_date": flight["content"]["outboundLeg"]["localDepartureDateLabel"],
            "origin_airport": flight["content"]["outboundLeg"]["originAirport"]["skyCode"],
            "destination_airport": flight["content"]["outboundLeg"]["destinationAirport"]["skyCode"],
            "Adults":a,
            "Children":ch,
            "Infants":inf,
            "Class":Class,
            "Currency":c
            
        }
        flights.append(flight_info)
        
        print(f"{i}. Price: {flight_info['price']} | Departure: {flight_info['label_date']} ({flight_info['dep_date']}) | From: {flight_info['origin_airport']} to {flight_info['destination_airport']}")
        print("-----")
    
    return flights

def generate_invoice(selected_flight):
    invoice = f"""
    Invoice
    ========
    Price: {selected_flight['price']}
    Raw Price: {selected_flight['raw_price']}
    Departure Date: {selected_flight['label_date']} ({selected_flight['dep_date']})
    Origin Airport: {selected_flight['origin_airport']}
    Destination Airport: {selected_flight['destination_airport']}
    Adults: {selected_flight['Adults']}
    Children: {selected_flight['Children']}
    Infants: {selected_flight['Infants']}
    Class: {selected_flight['Class']}
    Currency: {selected_flight['Currency']}
    ========
    Thank you for your purchase!
    """
    print(invoice)

def flights_autocomplete(place):
    autocomplete_info = {}
    url = "https://sky-scanner3.p.rapidapi.com/flights/auto-complete"

    querystring = {"query": place}

    headers = {
        "x-rapidapi-key": "930dbfb1d6mshaca55b144689bcbp1537ccjsn819e3ddcbb87",
        "x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json().get("data", [])
    
    if data:
        first_suggestion = data[0]  # Access the first item in the list
        city = first_suggestion['presentation']['title']
        autocomplete_info["city"] = city
        country = first_suggestion['presentation']['subtitle']
        autocomplete_info["country"] = country
        place_id = first_suggestion['presentation']['id']
        autocomplete_info["place_id"] = place_id
        skyid = first_suggestion['presentation']['skyId']
        autocomplete_info["skyId"] = skyid
        flight_entity_id = first_suggestion['navigation']['relevantFlightParams']['entityId']
        autocomplete_info["flightId"] = flight_entity_id
        hotel_entity_id = first_suggestion['navigation']['relevantHotelParams']['entityId']
        autocomplete_info["hotelId"] = hotel_entity_id
    return autocomplete_info, skyid

def main():
    place_a = input('Enter the departure place name: ')
    autocomplete_info_a, skyid_a = flights_autocomplete(place_a)
    # print(autocomplete_info_a)
    place_d = input('Enter the destination place name: ')
    autocomplete_info_d, skyid_d = flights_autocomplete(place_d)
    # print(autocomplete_info_d)
    
    y = input("Enter year in YYYY: ")
    m = input("Enter month in MM: ")
    c = input("Enter currency type (default is INR): ")or "INR"
    a = int(input('Enter the number of adults (above 12 yrs): '))
    ch = int(input('Enter the number of children (2-12 yrs): '))
    inf = int(input('Enter the number of infants (below 2 yrs): '))
    Class = int(input("Enter 1 for economy class\n2 for premium economy\n3 for business\n4 for first class: "))
    
    flights = get_flights(skyid_a, skyid_d, y, m, c, a, ch, inf, Class)
    # print(flights)
    if flights:
        selected_index = int(input("Enter the number of the flight you want to select: ")) - 1
        selected_flight = flights[selected_index]
        generate_invoice(selected_flight)
    else:
        print("No flights found.")

if __name__ == "__main__":
    main()
