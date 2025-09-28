import logging
import requests


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# api.open-notify.org/iss-now.json

# Response Codes (general)
# 1xx: Hold on
# 2xx: Here you go
# 3xx: Go Away
# 4xx: You Screwed Up
# 5xx: I Screwed Up
# httpstatuses.com

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) # Returns only status code in brackets [200]
print(response.status_code) #Retuns statuc code value 200

data_all = response.json()
data_latlong_only = response.json()["iss_position"]["longitude"]
data_long_only = response.json()["iss_position"]["longitude"]
print(f"Data All: {data_all}")
print(f"LatLong: {data_latlong_only}")
print(f"Longitude only: {data_long_only}")

longitude = data_all["iss_position"]["longitude"]
latitude = data_all["iss_position"]["latitude"]

iss_position = (longitude, latitude) # touple
print(iss_position)

response.raise_for_status()  # Catch errors from non-successful requests












