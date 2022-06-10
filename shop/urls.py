import imp
from django.urls import path
from shop.views import detail, index


#create your urls here

urlpatterns = [
    path ('', index, name = 'home'),
    path('<int:myid>', detail, name='detail')

]