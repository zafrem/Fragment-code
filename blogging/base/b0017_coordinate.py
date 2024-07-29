import requests

key = '97d52cb5774c2e2fe79623e0c28c9421'

lat = 21.3363571
lon = -158.0282134

def get_current_weather(key, lon, lat):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    response = requests.get(url)
    data = response.json()
    return data

if "__main__" == __name__:
    print(get_current_weather(key, lon, lat))
# Output
# {'coord':
#   {'lon': -158.0282, 'lat': 21.3364},
#  'weather':
#   [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle',
#       'icon': '09d'}],
#   'base': 'stations',
#   'main': {'temp': 301.51, 'feels_like': 304.38, 'temp_min': 297.01,
#       'temp_max': 303.1, 'pressure': 1017, 'humidity': 69},
#   'visibility': 10000,
#   'wind': {'speed': 5.66, 'deg': 50, 'gust': 12.35},
#   'clouds': {'all': 20},
#   'dt': 1719019088,
#   'sys': {'type': 1, 'id': 7868, 'country': 'US', 'sunrise': 1718985065,
#       'sunset': 1719033418},
#   'timezone': -36000,
#   'id': 5855070,
#   'name': '‘Ewa Gentry',
#   'cod': 200
#  }

