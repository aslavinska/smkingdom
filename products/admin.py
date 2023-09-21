from django.contrib import admin
from .models import  Product, Category, Artist, PrintOptions

class ArtistAdmin(admin.ModelAdmin):
        list_display = (
        'name',
        'background',
        'mainartstyle',
        'email',
    )


class CategoryAdmin(admin.ModelAdmin):
        list_display = (
        'friendly_name',
        'name',
    )

class ProductAdmin(admin.ModelAdmin):
        list_display = (
        'category',
        'sku',
        'artistname',
        'name',
        'description',
        'motivation',
        'program',
        'has_sizes',
        'price',
        'image_url',
        'image',
    )



class PrintOptionsAdmin(admin.ModelAdmin):
        list_display = (
        'name',
        'printname',
        'has_frame',
        'has_mattfinish',
        'has_signature',
        
    )

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PrintOptions, PrintOptionsAdmin)