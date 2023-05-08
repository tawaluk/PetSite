from django.contrib import admin
from django.urls import path
from infoposts import views

app_name = 'infoposts'

urlpatterns = [
    path('', views.root, name='base'),
]
