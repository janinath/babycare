
from django.shortcuts import render, get_object_or_404,redirect
from . models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from seller.models import Product
from django.views.generic import ListView
from .forms import RazorpayPaymentForm
import razorpay
from django.contrib import messages
from .models import Customer
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required



# Create your views here.
def Home(request):
   
    return render(request,'customers/home.html')
def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        # try:
        #     customer = Customer.objects.get(c_email=username, c_pswd=password)
            
        # except Customer.DoesNotExist:
        #     # User not found or password incorrect
        #     error_message = 'Invalid email or password. Please try again.'
        #     return render(request, 'customers/login.html',{'error_message': error_message})
        # # Authentication successful, log the user in
        customer_exist = Customer.objects.filter(c_email=username,c_pswd=password).exists()
        if customer_exist :
            customer = Customer.objects.get(c_email=username,c_pswd=password)
            request.session['customerid']=customer.id
        
            return redirect('customers:dashboard')
        else:
            return redirect('customers:login')

    return render(request, 'customers/login.html')
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         # Initialize the user variable
#         user = None

#         try:
#             # Attempt to authenticate the user
#             user = authenticate(request, username=username, password=password)

#             # Check if the authentication was successful
#             if user is not None:
#                 login(request, user)
#                 return redirect('customers:dashboard')
#             else:
#                 # Authentication failed
#                 error_message = 'Invalid email or password. Please try again.'
#                 return render(request, 'customers/login.html', {'error_message': error_message})

#         except Customer.DoesNotExist:
#             # User not found or password incorrect
#             error_message = 'Invalid email or password. Please try again.'
#             return render(request, 'customers/login.html', {'error_message': error_message})

#     return render(request, 'customers/login.html')
    

def Signup(request):
    
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mob']
        password = request.POST['pswd']

        # Check if the email is already registered
        if Customer.objects.filter(c_email=email).exists():
            messages.error(request, 'Email is already registered. Please use a different email.')
            return redirect('customers:signup')

        # Create a new customer object and save it to the database
        customer = Customer(c_name=name, c_email=email, c_mob=mobile, c_pswd=password, status='Active')
        customer.save()

        messages.success(request, 'Account created successfully. You can now log in.')
        return redirect('customers:login')

    return render(request, 'customers/signup.html')


def Dashboard(request):
    
        products = Product.objects.all()
        pd = Product.objects.all()
        page=request.GET.get('page',1)
        paginator=Paginator(pd,3) #show 3 products
        try:
            pd = paginator.page(page)
        except PageNotAnInteger:
            pd = paginator.page(1)
        except EmptyPage:
            pd = paginator.page(paginator.num_pages)

   # Calculate the page range based on the current page
        current_page = int(page)
        max_pages = paginator.num_pages
        page_range = list(range(max(1, current_page - 2), min(max_pages, current_page + 2) + 1))
        return render(request, 'customers/dashboard.html', {'pd': pd, 'page_range': page_range, 'current_page': current_page, 'max_pages': max_pages})

   
        # Redirect to the login page if the user is not authenticated
        return render(request,'customers/dashboard.html',{'pd': products})
def Searchproduct(request):
    return render(request,'customers/searchproduct.html')



class SellerProductListView(ListView):
    model = Product
    template_name = 'customer/seller_product_list.html'
    context_object_name = 'seller_products'
# def Cart_(request):
#     # Retrieve customer ID from the session
#     customer_id = request.session.get('customerid')
#     if customer_id is not None:
#         # If the customer is logged in, retrieve the customer object
#         customer = Customer.objects.get(pk=customer_id)

#         # Retrieve cart items for the logged-in customer
#         cart_items = Cart.objects.filter(customer=customer)

#         return render(request, 'customers/cart.html', {'cart_items': cart_items})
#     else:
#         # If the customer is not logged in, you might want to redirect to the login page
#         # or handle this case appropriately
#         return redirect('customers:login')
def Cart_(request):
    # cart_items = Cart.objects.all()
    
    # return render(request, 'customers/cart.html', {'cart_items': cart_items,})
    # Check if the 'customerid' session variable exists
    if 'customerid' in request.session:
        customer_id = request.session['customerid']
        
        # Retrieve customer information based on the customer_id
        try:
            customer = Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            # Handle the case where the customer does not exist
            # You may want to redirect the user to the login page or show an error message
            return redirect('customers:login')

        # Your logic for cart items using the customer information
        cart_items = Cart.objects.filter(customer=customer)
        
        return render(request, 'customers/cart.html', {'cart_items': cart_items, 'customer': customer})
    else:
        # Handle the case where the 'customerid' session variable does not exist
        # You may want to redirect the user to the login page or show an error message
        return redirect('customers:login')

def Viewpdt(request, product_id):
    pdt = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        title = pdt.title
        image = pdt.image
        price = pdt.price
        quantity = request.POST.get('quantity')
        total = int(quantity) * price  # Calculate total based on quantity

        # Save to Cart model
        cart_item = Cart(p_name=title, p_image=image, p_price=price, p_quantity=quantity, p_total=total)
        cart_item.save()
    
        # Display a success message
        return render(request, 'customers/viewpdt.html', {'pd': pdt, 'msg': 'Item added to cart successfully'})

    return render(request, 'customers/viewpdt.html', {'pd': pdt,})
def Buy(request,id):
    product=Product.objects.get(id=id)
    return render(request,'customers/buy.html' , {'p':product})
def Pay():
    pass

def DeleteCartItem(request,pk):
    deleteitem=Cart.objects.get(id=pk).delete()
    return redirect ('customers:cart')

def razorpay_payment(request,):
    if request.method == 'POST':
        form = RazorpayPaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']

            client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

            # Create a Razorpay order
            order_data = {
                'amount': int(amount*100),  # Razorpay expects the amount in paise
                'currency': 'INR',
                'receipt': 'order_receipt_' + str(amount),
                'payment_capture': 1  # Auto-capture payment
            }
            order = client.order.create(data=order_data)

            return render(request, 'customers/form.html', {'order': order},)
        

    else:
        form = RazorpayPaymentForm()
    

    return render(request, 'customers/form.html', {'form': form, })
def Logout(request):
    return render(request,'customers/home.html')
     
    
    
    
        
    
