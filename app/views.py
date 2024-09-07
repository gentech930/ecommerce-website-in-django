from django.shortcuts import render
from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

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


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    return render(request, 'cart.html', {'cart': cart, 'items': items})
from django.shortcuts import render, redirect

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    return redirect('cart_view')

def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    return render(request, 'app/cart.html', {'cart': cart, 'products': products})











