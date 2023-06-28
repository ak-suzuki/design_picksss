from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('reference_site/', include('djangoapp.administrator.reference_site.urls')),
]
