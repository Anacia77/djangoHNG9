from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


app_name = 'users'
urlpatterns = [
    path('', views.welcomePage, name='welcomePage'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/', views.userPage, name='account'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]