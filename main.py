import requests #sends http requests to website, returns response object with a response data (content, status, encoding, etc)
from pprint import pprint #formats response contents into readable format (pretty print)


API_KEY = '31501ca1d1d67a648f1d0cd6ddf28aea'

city = input('Enter a city: ')

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + city #url to send response to 

weather_data = requests.get(base_url).json() 

pprint(weather_data)



