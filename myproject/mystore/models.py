from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.TextField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    date_registration = models.DateField(auto_now=True)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now=True)
    image = models.ImageField(default='')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateField(auto_now_add=True)
