from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('reference_site_list', include('apps.backend.reference_site.urls')),
]
