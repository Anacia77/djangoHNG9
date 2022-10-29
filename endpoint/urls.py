from django.urls import path
from . import views


urlpatterns = [
    path('', views.end, name='end'),
    path('task1/', views.task1, name='task1')
]