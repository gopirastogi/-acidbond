# utils.py

from django.conf import settings
from django.utils.safestring import mark_safe

def get_cart_items(request):
    """Retrieve cart items from session."""
    cart = request.session.get('cart', {})
    items = []
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            items.append({'product': product, 'quantity': quantity, 'price': product.price})
        except Product.DoesNotExist:
            continue
    return items

def add_to_cart(request, product_id, quantity):
    """Add a product to the cart."""
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    request.session['cart'] = cart

def clear_cart(request):
    """Clear the cart from the session."""
    request.session['cart'] = {}
