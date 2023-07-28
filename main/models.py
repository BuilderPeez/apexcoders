from django.db import models

# Create your models here.

class AppInfo(models.Model):
    logo = models.ImageField(upload_to='logo')
    carousel1 = models.ImageField(upload_to='carousel')
    carousel2 = models.ImageField(upload_to='carousel')
    carousel3 = models.ImageField(upload_to='carousel')
    banner = models.ImageField(upload_to='banner')
    appname = models.CharField(max_length=100)
    copyright = models.IntegerField()

    def __str__(self):
        return self.appname

class Category(models.Model):
    name = models.CharField(max_length=100)
    catslug = models.SlugField(unique=True)
    catimg = models.ImageField(upload_to='catimg')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    pix = models.ImageField(upload_to='pix')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promo_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    topselling = models.BooleanField()
    featured = models.BooleanField()
    uploaded = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='image', blank=True, null=True)
    sent = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.full_name
    
