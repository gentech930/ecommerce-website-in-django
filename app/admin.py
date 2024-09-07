from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'category')  # Customize the fields you want to display
    search_fields = ('name', 'category')  # Add search functionality

admin.site.register(Product, ProductAdmin)




