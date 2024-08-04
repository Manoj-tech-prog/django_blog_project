from django.contrib import admin
from .models import Post, Category, Comment, Profile
from api_app.models import NewsArticle
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(NewsArticle)