from django.contrib import admin

from .models import Author, Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    list_filter = ['author', 'date', 'tags']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user_name']

# Register your models here.

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
