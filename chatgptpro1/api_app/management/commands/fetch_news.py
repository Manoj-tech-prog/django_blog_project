from typing import Any
import requests
from django.core.management.base import BaseCommand
from api_app.models import NewsArticle

class Command(BaseCommand):
    help = "Fetch Live News and store in the database"

    def handle(self, *args, **kwargs):
        api_key = '374ea7196abc4f4ab7ddd6d55dbe6e29'
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

        response = requests.get(url)
        articles = response.json().get('articles')

        for article in articles:
            NewsArticle.objects.create(
                title = article['title'],
                description = article['description'],
                url = article['url'],
                
                published_at = article['publishedAt']
            )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully fetched and stored news articles'))