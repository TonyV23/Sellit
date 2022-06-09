from django.shortcuts import render
from numpy import product
from .models import Product

# Create your views here.
def index(request):
    product_object = Product.objects.all() #selecting all products in database
    item_name = request.GET.get("item-name") #retrieve the content from the search bar (on name attribute)
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains = item_name)  
        

    return render(request, 'shop/index.html', {'product_object':product_object})