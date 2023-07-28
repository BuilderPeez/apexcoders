from django.contrib import admin
from .models import *
from userprofile.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'catslug':('name',)}
    list_display = ['id', 'name']

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['id', 'title', 'price', 'category', 'promo_price', 'topselling', 'featured', 'uploaded', 'edited']

admin.site.register(AppInfo)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Order)
