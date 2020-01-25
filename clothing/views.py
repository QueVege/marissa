from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from scrapy_redis import get_redis

from .models import Product


def index(request):

    """Render page with button to start parsing"""

    return render(request, 'clothing/index.html', {})


def load(request):

    """Set start url to redis queue"""

    Product.objects.all().delete()

    r = get_redis()
    r.lpush(
        'marissa:start_urls',
        'https://www.marissacollections.com/shop/clothing.html?limit=9'
    )

    return redirect('clothing:products_list')


class ProductsList(ListView):

    """Implementing a view to display products list"""

    model = Product
    template_name = 'clothing/products_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products_count'] = Product.objects.count()

        return context


class ProductDetail(DetailView):

    """Implementing a view to display product detail page"""

    model = Product
    template_name = 'clothing/product_detail.html'
