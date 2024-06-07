from django.shortcuts import render
from .models import Home,  Pricing,  Contact, About, Category


def home_page(request):
    homes = Home.objects.all()

    context = {'homes': homes}
    return render(request, 'index.html', {'context': home_page})

def contact_page(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contact.html', {'contacts': contact_page})

def about_page(request):
    about = About.objects.all()
    context = {'about': about}
    return render(request, 'about.html', {'about': about_page})

def pricing_page(request):
    pricing = Pricing.objects.all()
    context = {'pricing': pricing}
    return render(request, 'pricing.html', {'pricing': pricing_page})

def gallery_page(request):
    context = {
    'gallery': Home.objects.all()}
    return render(request, 'gallery.html', {'gallery': gallery_page})