import requests
from django.shortcuts import render
from .models import City
from aweather_project.settings import API_KEY

def get_weather_data(city_name):
    api_key = API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'q':city_name, 'units':'metric', 'lang':'ru', 'APPID': api_key}

    response = requests.get(url, params)
    return response.json()

def index(request):
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        weather_data = get_weather_data(city_name)
    else:
        weather_data = None
    return render(request, 'weather_app/index.html', {'weather_data': weather_data})
