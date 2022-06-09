import imp
from django.urls import path
from shop.views import index


#create your urls here

urlpatterns = [
    path ('', index, name = 'home') 
]