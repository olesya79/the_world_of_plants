from blog.models import Blog
from blog.models import Bloger
from django.contrib import admin


# Register your models here.


@admin.register(Bloger)
class BlogerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'location', 'email', 'phone']
    ordering = ['second_name']
    search_fields = ['second_name__istartwith']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    search_fields = ['title__istartwith']
