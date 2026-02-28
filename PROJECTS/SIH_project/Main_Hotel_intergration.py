import requests
import sys
import os
from datetime import datetime

# Load API keys from environment variables
BOOKING_API_KEY = os.getenv("BOOKING_API_KEY", "your_default_booking_api_key")
BOOKING_API_HOST = "booking-com15.p.rapidapi.com"
GEOCODE_API_KEY = os.getenv("GEOCODE_API_KEY", "your_default_geocode_api_key")

# URL Endpoints
GEOCODE_URL = "https://geocode.maps.co/search"
REVERSE_GEOCODE_URL = "https://geocode.maps.co/reverse"
BOOKING_API_URL = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotelsByCoordinates"

def fetch_lat_long(address):
    """Fetch latitude and longitude for a given address using the geocode API."""
    try:
        response = requests.get(GEOCODE_URL, params={"q": address})
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

def reverse_geocode(lat, lon):
    """Fetch address for a given latitude and longitude using the reverse geocode API."""
    try:
        response = requests.get(REVERSE_GEOCODE_URL, params={"lat": lat, "lon": lon})
        response.raise_for_status()
        data = response.json()
        return data.get("display_name", "N/A")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching reverse geocode data: {e}")
        return "N/A"

def fetch_hotel_details(lat, lon, a_date, d_date, a, ch, r, r_qty, curr):
    """Fetch hotel details using Booking API."""
    query_params = {
        "latitude": lat,
        "longitude": lon,
        "arrival_date": a_date,
        "departure_date": d_date,
        "radius": r,
        "adults": a,
        "children_age": ch,
        "room_qty": r_qty,
        "currency_code": curr
    }

    headers = {
	"x-rapidapi-key": "3560d6dccdmsh5df617b54ffcc1dp1b8d38jsn8e96076ee1c3",
	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
    }

    try:
        response = requests.get(BOOKING_API_URL, headers=headers, params=query_params)
        response.raise_for_status()
        result = response.json()
        return result.get("data", {}).get("result", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching hotel data: {e}")
        sys.exit(1)

def display_charge_distribution(hotel):
    """Display detailed invoice for the given hotel."""
    price_breakdown = hotel.get("composite_price_breakdown", {})
    
    included_charges = price_breakdown.get("included_taxes_and_charges_amount", {}).get("amount_unrounded", "N/A")
    excluded_charges = price_breakdown.get("excluded_amount", {}).get("amount_unrounded", "N/A")
    gross_amount = price_breakdown.get("gross_amount", {}).get("amount_unrounded", "N/A")
    net_amount = price_breakdown.get("net_amount", {}).get("amount_unrounded", "N/A")
    extra_charges = price_breakdown.get("charges_details", {}).get("amount", {}).get("value", "N/A")
    all_inclusive_amount = price_breakdown.get("all_inclusive_amount", {}).get("amount_unrounded", "N/A")
    gross_amount_per_night = price_breakdown.get("gross_amount_per_night", {}).get("amount_unrounded", "N/A")
    gross_amount_hotel_currency = price_breakdown.get("gross_amount_hotel_currency", {}).get("amount_unrounded", "N/A")

    total_gst = None
    charges_details = price_breakdown.get("items", [])
    for item in charges_details:
        if item.get("name", "") == "Goods & services tax":
            total_gst = item.get("item_amount", {}).get("amount_unrounded", "N/A")
    
    benefits = price_breakdown.get("benefits", [])
    
    print("Invoice Details:")
    print(f"  Gross Amount: {gross_amount} INR")
    print(f"  Net Amount: {net_amount} INR")
    print(f"  Included Taxes and Charges: {included_charges} INR")
    print(f"  Excluded Charges: {excluded_charges} INR")
    print(f"  Extra Charges: {extra_charges} INR")
    print(f"  All-Inclusive Amount: {all_inclusive_amount} INR")
    print(f"  Gross Amount per Night: {gross_amount_per_night} INR")
    print(f"  Gross Amount (Hotel Currency): {gross_amount_hotel_currency} INR")
    print(f"  Goods and Services Tax (GST): {total_gst} INR")
    
    if benefits:
        print("  Benefits:")
        for benefit in benefits:
            print(f"    - {benefit.get('name', 'N/A')}")
    
    print("-" * 50)

def display_hotels(hotels):
    """Display hotel details in a user-friendly format."""
    if not hotels:
        print("No hotels found for the given location and date range.")
        return

    for index, hotel in enumerate(hotels, start=1):
        print(f"Hotel {index}:")
        print(f"  Name: {hotel.get('hotel_name', 'N/A')}")
        print(f"  Location: {hotel.get('city', 'N/A')}, {hotel.get('countrycode', 'N/A')}")
        print(f"  Rating: {hotel.get('review_score', 'N/A')} ({hotel.get('review_score_word', 'N/A')})")
        print(f"  Price: {hotel.get('min_total_price', 'N/A')} {hotel.get('currencycode', 'N/A')}")
        print(f"  Free Cancellation: {'Yes' if hotel.get('is_free_cancellable') else 'No'}")
        print(f"  Genius Deal: {'Yes' if hotel.get('is_genius_deal') else 'No'}")
        print(f"  Accommodation Type: {hotel.get('accommodation_type', 'N/A')}")
        print(f"  Check-in: {hotel.get('checkin', {}).get('from', 'N/A')} to {hotel.get('checkin', {}).get('until', 'N/A')}")
        print(f"  Check-out: {hotel.get('checkout', {}).get('from', 'N/A')} to {hotel.get('checkout', {}).get('until', 'N/A')}")
        print(f"  Photo URL: {hotel.get('main_photo_url', 'N/A')}")
        
        latitude, longitude = hotel.get('latitude'), hotel.get('longitude')
        if latitude and longitude:
            address = reverse_geocode(latitude, longitude)
            print(f"  Address: {address}")
        else:
            print("  Address: N/A")
        print("-" * 50)

def display_details(hotel, a_date, d_date, a, ch, r_qty):
    """Display summary details of the selected hotel."""
    print(f"Name: {hotel.get('hotel_name', 'N/A')}")
    print(f"Location: {hotel.get('city', 'N/A')}, {hotel.get('countrycode', 'N/A')}")
    print(f"Arriving: {a_date}")
    print(f"Departing: {d_date}")
    print(f"Adults: {a}")
    print(f"Children: {len(ch)}")
    print(f"Rooms: {r_qty}")
    print(f"Price: {hotel.get('min_total_price', 'N/A')} {hotel.get('currencycode', 'N/A')}")
    print(f"Check-in: {hotel.get('checkin', {}).get('from', 'N/A')} to {hotel.get('checkin', {}).get('until', 'N/A')}")
    print(f"Check-out: {hotel.get('checkout', {}).get('from', 'N/A')} to {hotel.get('checkout', {}).get('until', 'N/A')}")
    print("-" * 50)

def validate_date(date_text):
    """Validate date input."""
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def main():
    """Main function to run the hotel finder application."""
    print("Welcome to the Travel Genie")

    try:
        place = input('Enter the location where you want to find a hotel: ').strip().capitalize()

        lat, lon = fetch_lat_long(place)
        print(f"Coordinates for {place}: Latitude = {lat}, Longitude = {lon}")

        while True:
            a_date = input('Enter arrival date in format YYYY-MM-DD: ')
            if validate_date(a_date):
                break
            else:
                print("Invalid date format. Please try again.")

        while True:
            d_date = input('Enter departure date in format YYYY-MM-DD: ')
            if validate_date(d_date):
                break
            else:
                print("Invalid date format. Please try again.")

        a = input("Enter number of adults (above 18): ")
        ch = input("Enter the age of children (e.g., age1, age2 if 2 children are there): ")
        r = input("Enter search radius in kilometers: ")
        r_qty = input("Enter number of rooms required: ")
        curr = input("Enter currency code (e.g., INR, USD): ")

        hotels = fetch_hotel_details(lat, lon, a_date, d_date, a, ch, r, r_qty, curr)
        display_hotels(hotels)

        if hotels:
            hotel_choice = int(input("Enter the hotel number you want to choose: ")) - 1
            selected_hotel = hotels[hotel_choice]
            display_details(selected_hotel, a_date, d_date, a, ch, r_qty)
            display_charge_distribution(selected_hotel)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

