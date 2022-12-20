from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)

class follows(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, default=None, related_name='follower')
    following = models.ManyToManyField(User, default=None, related_name='isfollowing')

class tweet(models.Model):
    id = models.AutoField(primary_key=True)
    tweet = models.TextField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    likers = models.ManyToManyField(User, default=None, related_name='likers')
    likes = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-time']

    