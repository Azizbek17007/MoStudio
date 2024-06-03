from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Home, Contact,  Pricing,  About, Category

admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Pricing)
admin.site.register(About)
