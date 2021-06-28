from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('products', views.products, name='products'),
    path('signup', views.signup, name='signup')
]
