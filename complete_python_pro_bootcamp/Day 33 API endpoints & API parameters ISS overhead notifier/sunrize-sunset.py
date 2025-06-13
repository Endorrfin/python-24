import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = 'lkirnadz@gmail.com'
MY_PASSWORD = 'abcd1234567()'

MY_LAT = 50.4504
MY_LONG = 30.5245

# MY_LAT = 51.507351
# MY_LONG = -0.127758

def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    print('💽 DATA', data)

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    print('☀️ SUNRISE', sunrise, '\n', '🌤️ SUNSET', sunset)

    time_now = datetime.now()
    print('⏰ TIME NOW', time_now)

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(600) #600 second
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject:Look ⬆️\n\nThe ISS is above you it the sky.'
        )

