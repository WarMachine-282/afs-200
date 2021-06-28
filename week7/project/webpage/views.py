from django.shortcuts import render
from .models import Product

# Create your views here.
def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def signup(request):
    return render(request, 'signup.html')

