from django.contrib import admin
from .models import Category, Post, Comment, PostCategory, Author, Subscription


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Subscription)