from django.shortcuts import render, redirect, HttpResponse
from cartt.models import ContactUs, CartItem
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from decimal import Decimal
from django.db.models import Sum
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .models import Customer  # Adjust the import based on the location of your Customer model
from .forms import CustomerForm
from django.shortcuts import render, get_object_or_404

from django.template.loader import get_template
from xhtml2pdf import pisa
from cartt.models import *

# Create your views here.


def login(request):
    return render(request, 'login.html')

def orders(request):
    try:
        customer = get_object_or_404(Customer, user=request.user)
        orders = customer.orders.all()  # Fetch related orders
    except Customer.DoesNotExist:
        # Handle case where the customer does not exist
        orders = []

    context = {
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'orders.html', context)


@login_required(login_url='/login/')
def checkout_success(request):
    return render(request, 'checkout_success.html')


@login_required(login_url='/login/')
def cart(request):
    return render(request, 'cart.html')

@login_required(login_url='/login/')
def wishlist(request):
    return render(request, 'wishlist.html')


@login_required(login_url='/login/')
def blog(request):
    return render(request, 'blog.html')


@login_required(login_url='/login/')
def base(request):
    return render(request, 'base.html')


@login_required(login_url='/login/')
def mail(request):
    return render(request, 'mail.php')


@login_required(login_url='/login/')
def shop_now(request):
    return render(request, 'shop_now.html')
    

@login_required(login_url='/login/')
def checkout(request):
     if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        add1 = request.POST.get('add1')
        add2 = request.POST.get('add2')
        postal_code = request.POST.get('postal_code')
        total_price = request.POST.get('total_price')

        total_price_str = request.POST.get('total_price', '0.00')
        try:
            total_price = Decimal(total_price_str.replace('$', '').replace(',', ''))
        except InvalidOperation:
            # Handle invalid decimal conversion
            total_price = Decimal('0.00')



        # Retrieve or create a customer
        customer, created = Customer.objects.get_or_create(user=request.user)


        # Create the Order instance
        order = Order(
            customer=customer,
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            country=country,
            add1=add1,
            add2=add2,
            postal_code=postal_code,
            total_price=total_price, 
        )
        order.save()


 # Retrieve cart items and create OrderItem instances
        cart_items = CartItem.objects.filter()
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            # Optionally, remove the cart item after order creation
            item.delete()

         

        return redirect('checkout_success')  

        cart_items = []  # Replace with actual cart items retrieval logic
        total = Decimal('0.00')  # Replace with actual total calculation logic

        return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total, 'customer': customer})


@login_required(login_url='/login/')
def contact(request):
    if request.method == 'POST':
        contact = ContactUs(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message  = request.POST.get('message'),
        )
        contact.save()
    return render(request, 'contact.html')
    


@login_required(login_url='/login/')
def profile_view(request):
    customer = get_object_or_404(Customer, user=request.user)
    return render(request, 'profile.html', {'customer': customer})



@login_required(login_url='/login/')
def edit_profile(request):
    customer = get_object_or_404(Customer, user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Redirect to the profile view after saving
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'edit_profile.html', {'form': form})


def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect('profile_view')  # Redirect to profile view after creating
    else:
        form = CustomerForm()
    
    return render(request, 'create_customer.html', {'form': form})



class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)




@login_required(login_url='/login/')
def generate_invoice(request):

    # Context data for the invoice
    context = {
        'order_id': 'INV00123',
        'customer_name': 'John Doe',
        'items': [
            {'description': 'Product A', 'quantity': 2, 'price': 150},
            {'description': 'Product B', 'quantity': 1, 'price': 300},
        ],
        'total_price': 600
    }
    
    # Load the HTML template
    template = get_template('invoice_template.html')
    html = template.render(context)
    
    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
    # Generate the PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors generating the invoice', status=400)
    
    return response


@login_required(login_url='/login/')
def place(request):
    customer = get_object_or_404(Customer, user=request.user)
    return render(request, 'place.html', {'customer': customer})

