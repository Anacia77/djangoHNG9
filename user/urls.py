from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path('welcome/', views.welcomePage, name='welcomePage'),
    path('register/', views.registerPage, name='register'),
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/', views.account, name='account'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('check_email_exist',views.check_email_exist,name="check_email_exist"),
    path('check_username_exist',views.check_username_exist,name="check_username_exist"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('user_profile_save', views.user_profile_save, name="user_profile_save"),

]