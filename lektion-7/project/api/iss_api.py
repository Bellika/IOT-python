import requests
import json
import os
import reverse_geocoder as rg

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/iss_data.json')
API_URL = 'https://api.wheretheiss.at/v1/satellites/25544/'

def fetch_iss_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

def save_iss_data(iss_data):
    with open(DATA_FILE, "w") as f:
        json.dump(iss_data, f, indent=4)

def iss_location():
    with open(DATA_FILE, "r") as f:
        iss_data = json.load(f)

    latitude = iss_data["latitude"]
    longitude = iss_data["longitude"]

    coords = (latitude, longitude)

    result = rg.search(coords)
    place = result[0]

    print(f"ISS is close to: {place['name']}, {place['admin1']}, {place['cc']}")
