from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    #image_url = models.ImageField(upload_to='media/')
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title