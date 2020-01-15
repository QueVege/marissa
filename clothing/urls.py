from django.urls import path
from . import views


app_name = 'clothing'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('run/', views.url_to_redis, name='run'),
    path('products/', views.ProductsList.as_view(), name='products_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
]