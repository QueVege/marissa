from django.urls import path
from . import views


app_name = 'clothing'
urlpatterns = [
    path('', views.index, name='index'),
    path('load/', views.load, name='load'),
    path('products/', views.ProductsList.as_view(), name='products_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
]