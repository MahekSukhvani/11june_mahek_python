from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about,name='about'),
    path('booktest/',views.booktest,name='booktest'),
    path('reports/',views.reports,name='reports'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('userlogout/',views.userlogout),
    path('otp/',views.otp,name='otp')
]