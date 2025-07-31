from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from shop.models import Category,Product

# Create your views here.

def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.all().order_by('?')[:8]  # random 8 products
    return render(request, 'home.html', {
        'categories': categories,
        'featured_products': featured_products
    })

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form= AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

