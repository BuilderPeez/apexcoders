from .models import AppInfo, Category
from userprofile.models import Cart

def apex(request):
     info = AppInfo.objects.get(pk=1)
     category = Category.objects.all()

     context = {
          'info': info,
          'category': category
     }

     return context

def cartcount(request):
     cart = Cart.objects.filter(user__username = request.user.username, paid=False)
     itemcount = 0

     for item in cart:
          itemcount += item.quantity

     context = {
          'cart': cart,
          'itemcount': itemcount
     }     

     return context