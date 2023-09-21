from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.signals import user_logged_in
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from allauth.account.signals import email_confirmed
import stripe



class Artist(models.Model):
    name = models.CharField(max_length=100)
    background = models.TextField()
    email = models.CharField(max_length=50)
    mainartstyle =  models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    artistname = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist')
    name =  models.CharField(max_length=100)
    description = models.TextField()
    motivation = models.TextField()
    program = models.CharField(max_length=100)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name


class PrintOptions(models.Model):
    name = models.CharField(max_length=100) 
    printname = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    has_frame = models.BooleanField(default=False, null=True, blank=True)
    has_mattfinish = models.BooleanField(default=False, null=True, blank=True)
    has_signature = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
            return self.name