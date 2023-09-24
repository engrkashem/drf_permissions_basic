from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']


@admin.register(models.ProductReviewModel)
class ProductReviewModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating',
                    'review', 'created_at', 'updated_at']
