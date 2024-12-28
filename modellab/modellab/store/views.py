from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product

# Home page
def index(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    products = Product.objects.all()
    if search_query:
        products = products.filter(name__icontains=search_query)
    if category_id:
        products = products.filter(category__id=category_id)
    return render(request, 'store/index.html', {'products': products})

# Category page
def category(request):
    return render(request, 'store/category.html')

# Product page
def product(request):
    return render(request, 'store/product.html')

# About page
def about(request):
    return render(request, 'store/about.html')

# Contact page
def contact(request):
    return render(request, 'store/contact.html')

# Cart page
def cart(request):
    return render(request, 'store/cart.html')

# Checkout page
def checkout(request):
    if request.method == 'POST':
        # Process the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # Simulate saving the order (you can save to the database here)
        print(f"Order placed by {name} with email {email}. Shipping to {address}.")

        # Redirect to order confirmation
        return redirect('order_confirmation')

    return render(request, 'store/checkout.html')

# Profile page
def profile(request):
    return render(request, 'store/profile.html')

# Order Confirmation page
def order_confirmation(request):
    # Example data to simulate order confirmation (replace with actual DB data)
    order = {
        'id': 12345,
        'address': '123 Main Street, Cityville',
        'total': 99.99,
        'items': [
            {'name': 'Product 1', 'price': 25.00, 'quantity': 2},
            {'name': 'Product 2', 'price': 49.99, 'quantity': 1},
        ]
    }
    
    user = {
        'name': 'John Doe',
    }
    
    context = {
        'order': order,
        'user': user,
    }

    return render(request, 'store/confirmation.html', context)

def home(request):
    return render(request, 'home.html')

   
def checkout(request):
    return render(request, 'checkout.html')

def category(request):
    return render(request, 'store/checkout.html', context)

