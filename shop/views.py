from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.cart import Cart


def product_list(request):
    cart = Cart(request)
    products = Product.objects.filter(available=True)
    return render(request, 'list.html', {'products': products, 'cart': cart})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, '', {'product': product})
