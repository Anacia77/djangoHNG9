from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.welcomePage, name='welcomePage'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/', views.userPage, name='account'),
]