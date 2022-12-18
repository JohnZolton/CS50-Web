from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)

class follows(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='following')
    following = models.ManyToManyField(User, related_name='followers')


class tweet(models.Model):
    id = models.AutoField(primary_key=True)
    tweet = models.TextField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-time']

    