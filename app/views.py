from django.shortcuts import render
from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'app/product_detail.html', {
        'product': product
    })
def home(request):
    products = Product.objects.all()
    return render(request, 'app/index.html', {'products': products})
def shop(request):
     products = Product.objects.all()
     return render(request, 'app/shop.html' , {'products': products} )
def shop_detail(request):
    return render(request, 'app/detail.html')
def contact(request):
    return render(request, 'app/contact.html')
def cart(request):
    return render(request, 'app/cart.html')
def checkout(request):
    return render(request, 'app/checkout.html')











