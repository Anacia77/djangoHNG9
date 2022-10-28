from django.urls import path
from . import views


urlpatterns = [
    path('', views.task1, name='task1'),
]