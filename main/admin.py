from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Home, Contact, Galeria, Pricing, Author, About

admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(Galeria)
admin.site.register(Pricing)
admin.site.register(Author)
admin.site.register(About)
