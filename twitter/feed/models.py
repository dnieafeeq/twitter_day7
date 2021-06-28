from django.db import models
from django.utils import timezone
from accounts.models import Profile
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    text = models.TextField(max_length = 280, default='')
    datetime = models.DateTimeField(default = timezone.now)
    author = models.name = models.ForeignKey(User, default='', on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.text[:5]

    @property
    def number_of_comments(self):
        return Comment.objects.filter(tweet_connected=self).count()


class Comment(models.Model):
    text = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_connected = models.ForeignKey(Tweet, on_delete=models.CASCADE)