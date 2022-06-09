from django.shortcuts import render
from numpy import product
from .models import Product

# Create your views here.
def index(request):
    product_object = Product.objects.all() #selecting all products in database
    return render(request, 'shop/index.html', {'product_object':product_object})