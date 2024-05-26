from django.shortcuts import render
import requests 
# Create your views here. c4aa6b00b9a7764307be4ce7a1ced3d6
from django.utils.translation import gettext as _
from django.utils.translation import get_language

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang={}&appid=c4aa6b00b9a7764307be4ce7a1ced3d6'
    
    city = None
    weather_data = None

    lottie_mapping = {
        '01d': 'animations/clearsky.json',
        '01n': 'animations/clearsky.json',
        '02d': 'animations/fewclouds.json',
        '02n': 'animations/fewclouds.json',
        '03d': 'animations/fewclouds.json',
        '03n': 'animations/fewclouds.json',
        '04d': 'animations/fewclouds.json',
        '04n': 'animations/fewclouds.json',
        '09d': 'animations/showerrain.json',
        '09n': 'animations/showerrain.json',
        '10d': 'animations/rain.json',
        '10n': 'animations/rain.json',
        '11d': 'animations/thunderstorm.json',
        '11n': 'animations/thunderstorm.json',
        '13d': 'animations/snow.json',
        '13n': 'animations/snow.json',
        '50d': 'animations/mist.json',
        '50n': 'animations/mist.json',
    }

    current_language = get_language()

    if request.method == 'POST': 
        city = request.POST.get('city')
        if city:
            city_weather = requests.get(url.format(city, current_language)).json() 

            if city_weather.get('cod') == 200:  
                icon_code = city_weather['weather'][0]['icon']
                weather_data = {
                    'city': city,
                    'temperature': city_weather['main']['temp'],
                    'description': city_weather['weather'][0]['description'],
                    # 'icon': city_weather['weather'][0]['icon']
                    'animation': lottie_mapping.get(icon_code, 'animations/na.json') 
                }
            else:
                weather_data = {'error': 'City not found or API limit exceeded'}
    context = {'weather_data' : weather_data}
    return render(request, 'index.html', context)
