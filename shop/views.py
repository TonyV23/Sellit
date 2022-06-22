from django.shortcuts import redirect, render
from .models import Product, Order
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

# used to checkout card button 
def checkout(request):
    if request.method == "POST" :
        items = request.POST.get('items')
        price_to_be_paid = request.POST.get('total')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        zipcode = request.POST.get('zipcode')
    
        user_order = Order(items=items, price_to_be_paid=price_to_be_paid, name=name, email= email, address=address, city=city, country=country, zipcode=zipcode)

        # save userData ordering in database
        user_order.save()

        # once the order is saved in the database, the user is redirected to the confirmation page
        return redirect('confirmation')

    return render(request, 'shop/checkout.html')

#used for confirmation page after user ordered
def confirmation(request):
    user_infos = Order.objects.all()[:1]
    for user_info in user_infos:
        user_info_name = user_info.name

    return render(request, 'shop/confirmation.html', {"name" : user_info_name}) 