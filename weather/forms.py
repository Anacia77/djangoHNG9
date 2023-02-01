from django.forms import ModelForm, TextInput
from .models import CityWeather


class CityWeatherForm(ModelForm):
    class Meta:
        model = CityWeather
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})
        }