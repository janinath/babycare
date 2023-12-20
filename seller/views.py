from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Homes(request):
    return render(request,'seller/homes.html')
def Logins(request):
    return render(request,'seller/logins.html')
def Signups(request):
    return render(request,'seller/signups.html')
def Addproduct(request):
    if request.method == 'POST':
        title=request.POST['title']
        description=request.POST['description']
        image=request.FILES['image']
        price=request.POST['price']
        quantity=request.POST['quantity']
        category=request.POST['category']
        status=request.POST['status']
        product=Product(title=title,description=description,image=image,price=price,quantity=quantity,category=category,status=status)
        product.save()
        return JsonResponse({'msg':'successfully added'})
            

    else:
        return render(request,'seller/addproduct.html')
def Viewproduct(request):
    pdts=Product.objects.all().order_by('title')
    # Number of items per page
    items_per_page = 2 # You can adjust this value based on your preference

    # Create a Paginator instance
    paginator = Paginator(pdts, items_per_page)

    # Get the requested page number from the request's GET parameters
    page = request.GET.get('page')
    finaldata = paginator.get_page(page)

    try:
        # Get the Page object for the requested page
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        products = paginator.page(paginator.num_pages)
    return render(request,'seller/viewproduct.html',{'product':pdts})
def Delete(request,pk):
    pdts=Product.objects.get(id=pk).delete()
    return redirect('seller:viewproduct')
    

    
    
    
    
