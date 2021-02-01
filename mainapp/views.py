from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    if id:
        context = {
            'title': 'geekshop - каталог',
            'product': Product.objects.get(id=id)
        }
    else:
        context = {
            'title': 'geekshop - каталог',
            'products': Product.objects.all(),
            'categories': ProductCategory.objects.all()
        }
    return render(request, 'mainapp/products.html', context)
