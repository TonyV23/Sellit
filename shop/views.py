from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

# for homepage
def index(request):
    product_object = Product.objects.all() #selecting all products in database
    item_name = request.GET.get("item-name") #retrieve the content from the search bar (on name attribute)
    if item_name != '' and item_name is not None :
        product_object = Product.objects.filter(title__icontains = item_name)  
    
    # pagination 
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page) 

    return render(request, 'shop/index.html', {'product_object':product_object})

# for product details
def detail(request, myid): # myid to get each product
    product_object = Product.objects.get(id=myid)
    


    return render(request, 'shop/detail.html', {'product':product_object})