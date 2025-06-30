import requests
from datetime import datetime

USERNAME = 'endorrfin'
TOKEN = '9B1qF0kDc13RHvip'
GRAPH_ID = 'graph1'


pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    # 'token': '5wcvscgo6XA0AoU5M9c8jC1B3KC20McN3peN9LDF0nk00nHF0femTM1fjCwFm0JY55NLl19JH4dns87WiACDkiNsTE7IwkxIbSvpI6tAnB6i6D9b4V9rLB5DB6HxgoNP'
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Morning jog',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# 🏃🏃‍♂️‍➡️CREATE MY MORNING JOG
# https://pixe.la/v1/users/endorrfin/graphs/graph1.html

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# 🟢 POST METHOD
# pixel_creation_endpoint = '/v1/users/<username>/graphs/<graphID>'
pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()
# print('📆 default', today)
# print('📆 formated', today.strftime('%Y%m%d'))

todayFormated = datetime(year=2025, month=6, day=28)
# print('📆 today formated', todayFormated)

pixel_data = {
    # 'date': '20250628',
    'date': today.strftime('%Y%m%d'),
    # 'quantity': '8.34',
    'quantity': input('🏃‍➡️ How many kilometers did you run today? '),
}

response_post = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response_post.text)

# 🟣 PUT METHOD
# update_endpoint = /v1/users/<username>/graphs/<graphID>
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    'quantity': '8.14'
}

response_put = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response_put.text)


# 🔴 DELETE METHOD
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response_del = requests.delete(url=delete_endpoint, headers=headers)
# print(response_del.text)







