from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from .models import Post, Category,Comment, Profile
from .forms import CommentForm
import requests
import json
import os
from datetime import datetime
from api_app.models import NewsArticle

# Create your views here.
def homepage(request):
    trending_posts = NewsArticle.objects.all().order_by('-published_at')[:5]  # Customize the filter as needed
    latest_posts = NewsArticle.objects.all().order_by('-published_at')[:5]
    worldwide_posts = NewsArticle.objects.all().order_by('-published_at')[:5]

    context = {
        'trending_posts': trending_posts,
        'latest_posts': latest_posts,
        'worldwide_posts': worldwide_posts,
        'user': request.user
    }
    return render(request, 'home.html', context)

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

def add_comment_for_posts(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = article
            comment.save()
            return HttpResponseRedirect(reverse('detail_post', args=[pk]))
    form = CommentForm()
    return render(request, 'add_comment.html', {'form':form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    article = NewsArticle.objects.filter(category=category)
    return render(request, 'category_posts.html', {'category': category, 'article': article})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def Register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('homepage')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form':form})


def detail_post(request, pk):
    article = NewsArticle.objects.get(pk=pk)
    return render(request, 'post_details.html', {'article':article})

def truncate_fractional_seconds(timestamp):
    """Truncate fractional seconds to six digits."""
    if '.' in timestamp:
        date_part, microsecond_part = timestamp.split('.')
        truncated_part = microsecond_part[:6]  # Take only the first 6 digits
        return f"{date_part}.{truncated_part}Z"
    return timestamp



INDEX_FILE = 'index.txt'
NEWS_FILE = 'news_data.json'

def news_view(request):
    try:
        if not os.path.exists(NEWS_FILE):
            return render(request, 'livenews.html', {'articles': []})

        with open(NEWS_FILE, 'r') as file:
            news_data = json.load(file)

        if 'articles' not in news_data:
            return render(request, 'livenews.html', {'articles': []})

        if not os.path.exists(INDEX_FILE):
            return render(request, 'livenews.html', {'articles': []})

        with open(INDEX_FILE, 'r') as file:
            current_index = int(file.read().strip())

        articles = news_data['articles'][current_index:current_index + 5]
        return render(request, 'livenews.html', {'articles': articles})
    except Exception as e:
        print(f"An error occurred while reading the JSON file: {e}")
        return render(request, 'livenews.html', {'articles': []})

    
    # API_KEY = '374ea7196abc4f4ab7ddd6d55dbe6e29'
    # url_path = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'

    # response = requests.get(url_path)

    # data = response.json()

    # articles = data['articles']

    # # for article in articles:  to display date time day field in output
    # #     # Truncate fractional seconds and convert to datetime object
    # #     article['publishedAt'] = datetime.strptime(
    # #         truncate_fractional_seconds(article['publishedAt']),
    # #         '%Y-%m-%dT%H:%M:%S.%fZ'
    # #     )

    # # # Sort articles by publishedAt in descending order (most recent first)
    # # articles.sort(key=lambda x: x['publishedAt'], reverse=True)                                                                    
    #                                                                     #or this is for normal if you don't want to show date time in output or
    #                                                                     # template # Adjust timestamp format
    #                                                                     # for article in articles:
    #                                                                     #     article['publishedAt'] = truncate_fractional_seconds(article['publishedAt'])

    #                                                                     # # Sort articles by publishedAt in descending order (most recent first)
    #                                                                     # articles.sort(key=lambda x: datetime.strptime(x['publishedAt'], '%Y-%m-%dT%H:%M:%S.%fZ'), reverse=True)


    # return render(request, 'livenews.html',{'articles':articles})

# def news_live(request):
#     API_Key = '374ea7196abc4f4ab7ddd6d55dbe6e29'
#     URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_Key}"

#     response = requests.get(URL)

#     data = response.json()

#     articles = data['articles']

#     return render(request, 'livenews.html',{'articles':articles})

def profile_page(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'profile_page.html', {'user':user})