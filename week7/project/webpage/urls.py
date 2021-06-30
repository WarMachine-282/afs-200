from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about', views.about, name='about'),
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('products', views.products, name='products'),
    path('signup', views.signup, name='signup'),
    path('add_idea', views.add_idea, name='add_idea')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)