import requests
from datetime import datetime


SAMPLE_LAT = 31.8646
SAMPLE_LONG = -88.7012

parameters = {
    "lat": SAMPLE_LAT,
    "lng": SAMPLE_LONG,
    "formatted": 0
}



response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)

response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunrise']
print(sunset + sunrise)

sunrise_hour = (sunrise.split("T"))[1].split(":")[0]
sunset_hour = (sunset.split("T"))[1].split(":")[0]
print(f"Sunrise hour: {sunrise_hour}")

hour_now = datetime.now().hour