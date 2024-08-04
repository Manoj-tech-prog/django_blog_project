from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='media/profile')
    youtube_url = models.CharField(blank=True, null=True, max_length=100)
    facebook_url = models.CharField(blank=True, null=True, max_length=100)
    website_url = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,blank=True)
    author = models.CharField(max_length=50, blank=True)
    title_tag = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True, default='images/default-image.jpeg')
    date_time_post = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    comment_body = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name