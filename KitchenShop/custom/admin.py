from django.contrib import admin

from custom.models import Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
