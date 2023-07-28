from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path('details/<str:id>', views.details, name='details'),
    path('category/<str:id>/<slug:slug>', views.category, name='category'),   
    path('contact', views.contact, name='contact'),   
    path('signout', views.signout, name='signout'),   
    path('signin', views.signin, name='signin'),   
    path('register', views.register, name='register'),   
    path('profile', views.profile, name='profile'),   
    path('profile_update', views.profile_update, name='profile_update'),   
    path('password_update', views.password_update, name='password_update'),   
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),   
    path('cart', views.cart, name='cart'),   
    path('delete', views.delete, name='delete'),   
    path('update', views.update, name='update'),   
    path('checkout', views.checkout, name='checkout'),   
    path('payment', views.payment, name='payment'),   
    path('callback', views.callback, name='callback'),   
    path('search', views.search, name='search'),   
]
