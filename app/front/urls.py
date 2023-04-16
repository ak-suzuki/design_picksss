from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.front_top, name='front_top'),
]
