# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Route for homepage
     path('', views.home, name='home'), # Route for homepage
    path('category/', views.category, name='category'),  # Category page
    path('product/', views.product, name='product'),  # Product page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('cart/', views.cart, name='cart'),  # Cart page
    path('checkout/', views.checkout, name='checkout'),  # Checkout page
    path('profile/', views.profile, name='profile'),  # Profile page
    path('checkout.html', views.checkout, name='checkout'),
     path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
      path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
      path('category/', views.category, name='category'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
]
