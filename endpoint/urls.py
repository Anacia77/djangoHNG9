from django.urls import path
from . import views


urlpatterns = [
    path('', views.end, name='end'),
    path('anacia/', views.task1, name='task1')
]