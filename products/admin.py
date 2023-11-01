from django.contrib import admin
from .models import Product, Category, Artist


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
        'program',
        'has_sizes',
        'price',
        'rating',
        'image_url',
        'image',
    )


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
