from django.shortcuts import render
from .models import Home, Author, Pricing, Galeria, Contact, About


def home_page(request):
    homes = Home.objects.all()

    context = {'homes': homes}
    return render(request, 'home.html', context)



def galeria_page(request):
    galerias = Galeria.objects.all()
    return render(request, 'galleria.html', {'gallerias': galerias})


def author_page(request):
    authors = Author.objects.all()
    return render(request, 'single.html', {'single': authors})

def contact_page(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})

def about_page(request):
    about = About.objects.all()
    return render(request, 'about.html', {'about': about})

def pricing_page(request):
    pricing = Pricing.objects.all()
    return render(request, 'pricing.html', {'pricing': pricing})



