from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'geekshop - каталог',
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/products.html', context)
