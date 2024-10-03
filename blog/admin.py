from django.contrib import admin

from blog.models import Blog

@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "image", "views_count", "is_published")
    list_filter = ("title", "created_at", "is_published")
    search_fields = ("title",)