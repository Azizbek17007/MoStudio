from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('blog/', galeria_page, name='gallarery'),
    path('blog/<int:pk>/', pricing_page, name='blog-detail'),
]