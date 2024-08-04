from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NewsArticle
from .serializers import NewsArticleSerializer
from rest_framework import status
# Create your views here.

class NewsArticleListCreate(APIView):
    def get(self, request):
        articles = NewsArticle.objects.all().order_by('-published_at')
        serializer = NewsArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NewsArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        # Delete all articles
        NewsArticle.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)