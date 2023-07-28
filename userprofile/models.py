from django.db import models
from django.contrib.auth.models import User
from main.models import Product

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    pix = models.ImageField(upload_to='profilepix')
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField(default = 1)
    amount = models.CharField(max_length=50)
    paid = models.BooleanField()

    def __str__(self):
        return self.product.title
    
   
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    pay_code = models.CharField(max_length=50)
    paid = models.BooleanField()
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
