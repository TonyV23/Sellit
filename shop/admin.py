from django.contrib import admin
from .models import Category, Product, Order


# Register your models here.

# for displaying our database tables in table
class AdminCategories(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminProducts(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')

class AdminOrders(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'city', 'country', 'zipcode', 'date_ordered')


admin.site.register(Category, AdminCategories)
admin.site.register(Product, AdminProducts)
admin.site.register(Order, AdminOrders)