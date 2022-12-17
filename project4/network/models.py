from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # followers
    pass


class tweet(models.Model):
    # tweet text
    # user who twoted
    # time twoted
    # likes
    pass
    