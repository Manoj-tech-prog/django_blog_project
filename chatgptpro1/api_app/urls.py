from django.urls import path
from .views import NewsArticleListCreate

urlpatterns = [
    path('all_news/', NewsArticleListCreate.as_view(), name='news_list_create')
]