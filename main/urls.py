from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('gallery/', gallery_page, name='gallery.html'),
    path('pricing/', pricing_page, name='pricing'),
]