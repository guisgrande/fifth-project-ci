from django.contrib import admin
from .models import Product, Category, Offer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_sku', 'system_name', 'display_name')
    search_fields = ('system_name', 'display_name')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('offer_sku', 'offer_name', 'offer_display', 'offer_discount')
    search_fields = ('offer_name', 'offer_display')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'release_date',
        'category',
        'price',
        'rating'
        )
    list_filter = ('release_date', 'category')
    search_fields = ('sku', 'name')
