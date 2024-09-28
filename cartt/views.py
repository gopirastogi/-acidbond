from django.shortcuts import render,  get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views import View
from .forms import OrderForm
from django.conf.urls import handler404
from store.models import Customer


# AddToCartFormCreate your views her

def cart(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.objects.filter(category_id=categoryID)
    else:
        products = Product.objects.all()
    return render(request, 'index.html', {'categories': categories, 'products': products})


def mans(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.objects.filter(category_id=categoryID)
    else:
        products = Product.objects.all()
    return render(request, 'mans.html', {'categories': categories, 'products': products})

@login_required(login_url='/login/')
def test(request):
    return render(request, "test.html")

@login_required(login_url='/users/send-otp/')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    customer = get_object_or_404(Customer, user=request.user)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('mans')
@login_required(login_url='/login/')
def cart_view(request):
    cart_items = CartItem.objects.all()
    items = CartItem.objects.all()
    customer = get_object_or_404(Customer, user=request.user)

    total_quantity = sum(item.quantity for item in items)

    total = sum(item.total_price() for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total, 'total_quantity': total_quantity,'customer': customer} )

@login_required(login_url='/login/')
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart_view')  # Replace with your cart view name


@login_required(login_url='/login/')
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    customer = order.customer
    context = {
        'order': order,
        'customer': customer
    }
    return render(request, 'checkout.html', context)




def custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_page_not_found_view