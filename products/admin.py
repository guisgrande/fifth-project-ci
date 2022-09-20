from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_sku', 'system_name', 'display_name')
    search_fields = ('system_name', 'display_name')


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
