####        Weather - Fetcher        ####

import requests

API_KEY = '61048f1550428b164965337dade186bb'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


city = input('Enter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather = data['weather'][0]['main']
    print('weather: ',weather)

    temperature = round(data['main']['temp'] - 273.15, 2)
    print('temperature: ',temperature, 'celsius')

else:
    print('Error Occured')
