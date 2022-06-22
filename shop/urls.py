import imp
from django.urls import path
from shop.views import checkout, confirmation, detail, index


#create your urls here

urlpatterns = [
    path ('', index, name = 'home'),
    path('<int:myid>', detail, name='detail'),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation")


]