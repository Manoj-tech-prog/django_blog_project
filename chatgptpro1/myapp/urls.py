from django.urls import path
from .views import (homepage, login_view, Register_page, detail_post, about_page, contact_page, add_comment_for_posts,category_list,category_posts,
news_view, profile_page)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login_view, name='loginform'),
    path('logout/', LogoutView.as_view(next_page='homepage'),name='Logout'),
    path('register/', Register_page, name='registerform'),
    path('post/<int:pk>/',detail_post, name='detail_post'),
    path('about/page/', about_page, name='about_page'),
    path('contact_page/', contact_page, name='contact-page'),
    path('add/comment/<int:pk>', add_comment_for_posts, name='add_comment'),
    path('category_list', category_list, name='category_list'),
    path('category/<int:category_id>/', category_posts, name='category_posts'),
    path('live_news/', news_view, name='news_live'),
    path('profile/page/<int:pk>/', profile_page, name="profilepage")
]