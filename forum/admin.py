# forum/admin.py
from django.contrib import admin
from account.models import User
from .models import Category, Post, Comment, Tag, PostTag

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(PostTag)