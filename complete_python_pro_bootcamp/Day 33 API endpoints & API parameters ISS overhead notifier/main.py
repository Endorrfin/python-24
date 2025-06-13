import requests

# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: User Screwed Up
# 5XX: Server Screwed Up

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print('RESPONSE STATE', response)
print('RESPONSE STATUS CODE', response.status_code)
print('RESPONSE RAISE for STATUS', response.raise_for_status())

data = response.json()
print('💽 DATA', data)

data_specific = response.json()['iss_position']['longitude']
print('💽 DATA FORMATTED', data_specific)

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude, latitude)
print('ISS POSITION', iss_position)

if response.status_code != 200:
    print('❌ Error')
    raise Exception('That resource does not exist.')
elif response.status_code == 401:
    raise Exception('You are not authorised to access this data.')



