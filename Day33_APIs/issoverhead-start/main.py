import requests
from datetime import datetime
import logging
import smtplib
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


MY_LAT = -49.507351 # Your latitude
MY_LONG = 175.127758 # Your longitude
MY_EMAIL = "berginVM@gmail.com"
MY_PASSWORD = 'xxmd aaht tpgs ysor'


def iss_overhead(lat, long):
    logger.info("Entering iss_overhead")

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    logger.info(f"iss_overhead response: {data}")

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude - 5 < lat < iss_latitude + 5 and iss_longitude -5 < long < iss_longitude + 5:
            logger.info("ISS is in range")
            return True
    return False

    #Your position is within +5 or -5 degrees of the ISS position.

def is_night(lat, long):
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    logger.info(f"is_night data reponse: {data}")

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    logger.info(f"Sunrise hour: {sunrise}, Sunset hour: {sunset}, Time Now hour: {time_now}")

    if sunrise > time_now or time_now > sunset:
        logger.info("is night True")
        return True
    return False

while True:
    time.sleep(10)
    if iss_overhead(MY_LAT, MY_LONG) and is_night(MY_LAT, MY_LONG):
        print("Send Email!")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PASSWORD)
            connection.sendmail(from_addr = MY_EMAIL, 
                                to_addrs = MY_EMAIL, 
                                msg = f"Subject:{subject}\n\n{message}"   # msg format: msg="Subject:Thanks\n\nThanks for you email!"
                                )
        break
    else:
        print("Can't see it")




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



