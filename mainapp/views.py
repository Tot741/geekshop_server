from django.shortcuts import render
from json import load


# Create your views here.
def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open("mainapp/fixtures/products.json", "r") as json_data:
        catalog = load(json_data)
        catalog_list = catalog.values()
    context = {
        'title': 'geekshop - каталог',
        'products': catalog_list,
    }
    return render(request, 'mainapp/products.html', context)
