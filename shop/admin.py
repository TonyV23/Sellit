from django.contrib import admin
from .models import Category, Product, Order


# Register your models here.

admin.site.site_header = "La piraterie SHOP"
admin.site.site_title = "Viper23 Shop"
admin.site.index_title = "TonyV23"

# for displaying our database tables in table
class AdminCategories(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminProducts(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',) # search products by it's titles
    list_editable = ('price',)

class AdminOrders(admin.ModelAdmin):
    list_display = ('items','price_to_be_paid', 'name', 'email', 'address', 'city', 'country', 'zipcode', 'date_ordered')


admin.site.register(Category, AdminCategories)
admin.site.register(Product, AdminProducts)
admin.site.register(Order, AdminOrders)