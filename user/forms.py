from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Detail




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']


class DetailForm(ModelForm):
    class Meta:
        model =Detail
        fields = ['name', 'phone', 'profile_pic']