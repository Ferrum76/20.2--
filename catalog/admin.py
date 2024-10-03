from django.contrib import admin
from django.contrib.admin import ModelAdmin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Version)
class VersionAdmin(ModelAdmin):
    list_display = ("id", "product", "version_number", "version_name", "version_sign")
    list_filter = ("product",)
    search_fields = ("product", "version_number",)
