from django.shortcuts import render
from .models import Product, Ideas

# Create your views here.


def about(request):
    return render(request, 'about.html')


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def dashboard(request):
    idea = Ideas.objects.all()
    return render(request, 'dashboard.html', {'idea': idea})


def login(request):
    return render(request, 'login.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def signup(request):
    return render(request, 'register.html')


def add_idea(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            # imgURL = request.POST['imgURL']
            name = request.POST['name']
            # price = request.POST['price']
            desc = request.POST['desc']
            # check whether it's valid:
            Ideas.objects.create( name=name, desc=desc )
            idea = Ideas.objects.all()
            return render(request, 'dashboard.html', {'idea': idea})
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
        else:
            idea = Ideas.objects.all()
            return render(request, 'dashboard.html', {'idea': idea})




