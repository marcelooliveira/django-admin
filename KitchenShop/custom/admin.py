from django.contrib import admin

from custom.models import Category
@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass
