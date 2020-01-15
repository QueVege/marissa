from django.urls import path
from . import views


app_name = 'clothing'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('run/', views.url_to_redis, name='run'),
    path('catalog/', views.clothing_list, name='catalog')
]