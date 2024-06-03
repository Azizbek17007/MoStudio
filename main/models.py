from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Home(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home')
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name



class About(TimeStampedModel):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about')
    def __str__(self):
        return self.name

class Pricing(TimeStampedModel):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    processing = models.CharField(max_length=100)
    type_of_camera = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pricing')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title




class Contact(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name





