from django.shortcuts import render, HttpResponse, redirect
import json
import urllib, requests

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        #source = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=0c850260273a0bf801fc6592d894f879').read()
        #r = json.loads(source)

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0c850260273a0bf801fc6592d894f879'
        r = requests.get(url.format(city)).json()


        #str(r)
        data = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'humidity': r['main']['humidity'],
            'pressure': r['main']['pressure'],
            'windspeed': r['wind']['speed'],

        }
        #print(data)
        #return redirect('index')
    else:
        data = {}
    
    context = {'data': data}
    return render(request, 'sky.html', context)