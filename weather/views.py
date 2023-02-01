from django.shortcuts import render, get_object_or_404
import requests
from .models import CityWeather
from .forms import CityWeatherForm
# Create your views here.

def index(request):
    cities = CityWeather.objects.all()

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0c850260273a0bf801fc6592d894f879'

    if request.method == 'POST':
        form = CityWeatherForm(request.POST)
        form.save()


    form = CityWeatherForm()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        weather ={
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'humidity': r['main']['humidity'],
            'pressure': r['main']['pressure'],
            'windspeed': r['wind']['speed'],

        }

        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form }
    return render(request, 'weather/sky.html', context)


