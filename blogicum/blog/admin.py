from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "is_published", "created_at", "slug"]
    search_fields = ["title", "description"]
    list_filter = ["is_published", "created_at"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "is_published", "created_at"]
    search_fields = ["name"]
    list_filter = ["is_published", "created_at"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "category",
        "location",
        "is_published",
        "pub_date",
        "created_at",
    ]
    search_fields = ["title", "text", "author__username", "category__title"]
    list_filter = ["is_published", "pub_date", "created_at", "category"]
    autocomplete_fields = ["author", "location", "category"]
    date_hierarchy = "pub_date"
