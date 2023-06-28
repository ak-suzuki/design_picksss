from django.urls import path

from . import views

app_name = 'reference_site'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('add/', views.item_add, name='item_add'),
]
