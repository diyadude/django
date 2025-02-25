from django.contrib import admin

from .models import Author, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    list_filter = ['author', 'date', 'tags']

# Register your models here.

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
