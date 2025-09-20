import requests
from datetime import datetime, timedelta
import os
import configparser

def get_geo_coordinate(api_key, city):
    url=f"""http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={5}&appid={api_key}"""
    response = requests.get(url)
    data = response.json()
    """
    [
        {'name': 'Suwon-si', 
         'local_names': 
            {'ascii': 'Suwon', 'es': 'Suwon', 'lt': 'Suvonas', 'et': 'Suwon', 'zh': '水原市', 'pt': 'Suwon', 'ru': 'Сувон', 'ca': 'Suwon', 'ja': '水原市', 'fi': 'Suwon', 'en': 'Suwon-si', 'ko': '수원시', 'de': 'Suwon', 'fr': 'Suwon', 'feature_name': 'Suwon', 'uk': 'Сувон', 'el': 'Σούουον'},
         'lat': 37.2633325, 
         'lon': 127.0287472, 
         'country': 'KR'
        }
    ]
    """
    return data[0]['lat'], data[0]['lon']

def get_weather_5day_per_3hour(api_key, lon, lat):
    url=f"""http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"""
    response = requests.get(url)
    data = response.json()
    """
    {
      "cod": "200",
      "message": 0,
      "cnt": 40,
      "list": [
        {
          "dt": 1661871600,
          "main": {
            "temp": 296.76,
            "feels_like": 296.98,
            "temp_min": 296.76,
            "temp_max": 297.87,
            "pressure": 1015,
            "sea_level": 1015,
            "grnd_level": 933,
            "humidity": 69,
            "temp_kf": -1.11
          },
          "weather": [
            {
              "id": 500,
              "main": "Rain",
              "description": "light rain",
              "icon": "10d"
            }
          ],
          "clouds": {
            "all": 100
          },
          "wind": {
            "speed": 0.62,
            "deg": 349,
            "gust": 1.18
          },
          "visibility": 10000,
          "pop": 0.32,
          "rain": {
            "3h": 0.26
          },
          "sys": {
            "pod": "d"
          },
          "dt_txt": "2022-08-30 15:00:00"
        },
        ...
    """
    weather_info = data['list']
    current_date = datetime.now()
    weather_by_day = {}
    for i in range(6):
        date = current_date.date() + timedelta(days=i)
        weather_by_day[date.strftime("%A")] = []
        for forecast in weather_info:
            forecast_date = datetime.fromtimestamp(forecast['dt']).date()
            if forecast_date == date:
                weather_by_day[date.strftime("%A")].append(forecast['weather'][0]['description'])
    for day, weather in weather_by_day.items():
        print(f"{day}: {', '.join(weather)}")

def get_current_weather(pi_key, lon, lat):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    """
    {
    'coord': 
        {'lon': 127.0276, 'lat': 37.2613}, 
    'weather': 
        [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 
    'standard': 'stations', 
    'main': {'temp': 284.84, 'feels_like': 283.58, 'temp_min': 279.6, 'temp_max': 284.84, 'pressure': 1008, 'humidity': 58}, 
    'visibility': 10000, 
    'wind': {'speed': 0.51, 'deg': 160}, 
    'clouds': {'all': 40}, 
    'dt': 1681646477, 
    'sys': {'type': 1, 'id': 5509, 'country': 'KR', 'sunrise': 1681592213, 'sunset': 1681639584}, 
    'timezone': 32400, 
    'id': 6575883, 
    'name': 'Seryui-dong', 
    'cod': 200
    }
    """

if "__main__" == __name__:
    base_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    config = configparser.ConfigParser()
    print(os.path.join(base_dir, 'conf', 'token_information.ini'))
    config.read(os.path.join(base_dir, 'conf', 'token_information.ini'), encoding='UTF8')
    api_key = config['openweather']['key']

    #lon, lat = get_geo_coordinate(api_key, 'Suwon-si')
    #Suwon-si Home
    config.read(os.path.join(base_dir, 'conf', 'local_coordinates.ini'), encoding='UTF8')
    lat = config['home']['lat']
    lon = config['home']['lon']
    #get_weather_5day_per_3hour(api_key, lon, lat)
    get_current_weather(api_key, lon, lat)