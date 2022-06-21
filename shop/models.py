from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # this class help us to show new products or categories at first line after they have been added
    class Meta:
        ordering = ['-date_added']


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField(max_length=200)
    category = ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.CharField(max_length=50000)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # this class help us to show new products or categories at first line after they have been added
    class Meta:
        ordering = ['-date_added']

class Order(models.Model):
    items = models.CharField(max_length=300)
    price_to_be_paid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    city =  models.CharField(max_length=200)
    country = models.CharField(max_length=300)
    zipcode =  models.CharField(max_length=300)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_ordered']

