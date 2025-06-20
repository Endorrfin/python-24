import requests
from twilio.rest import Client

# ⚪️ Weather API: https://openweathermap.org/
# 🔹Weather now: https://www.ventusky.com/

# 🔴TRIAL ACCESS to SERVICE
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = 'bc0b331f174eaf2c2a3c0e332035c7ef'


# 🟣SMS SERVICE: https://www.twilio.com/en-us
# 🔴TRIAL ACCESS to SERVICE
account_sid = 'AC357826531379b5588410dfc6a348ab6b'
auth_token = 'e772d9fdeec56c25e0db284ed79a5367'

# UA 🇺🇦
LATITUDE = 50.553333
LONGITUDE = 30.213516

# PL 🇵🇱
# LATITUDE = 52.229675
# LONGITUDE = 21.012230

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

# 🦶🦶STEPS
    #1️⃣ Get you latitude & longitude from https://www.latlong.net/
    #2️⃣ Make a request to the forecast API using the requests module
    #3️⃣ Print out the HTTP status code that you get back
    #4️⃣ Print the response to the console
    #5️⃣ Copy-paste the response to an online JSON viewer (e.g., jsonviewer.stack.hu).
    #6️⃣ Locate the weather id and description for each forecast.

weather_params = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'appid': api_key,
    'cnt': 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
print('RESPONSE', response.status_code)
# print('💽 DATA', response.json())

weather_data = response.json()
# print(weather_data['list'][0]['weather'][0]['id'])

will_rain = False
for hour_data in weather_data['list']:
    # print('🌧️', hour_data['weather'][0]['id'])
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # print('Bring an umbrella! ☔️')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "It's going to rain 💦 today. Remember to bring an ☔️",
        from_='+19785197483',
        to='+380502356490'
    )

    print('📩', message.status)
