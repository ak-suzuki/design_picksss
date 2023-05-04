from django.urls import path

from . import views

urlpatterns = [
    path('', views.reference_site_list, name='reference_site_list'),
]
