from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    path('', views.login, name='login'),  # root URL
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),


]

