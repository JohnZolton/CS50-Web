from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50, blank=True, null=True, unique=True)
    creditcard = models.CharField(max_length=19, blank=True, null=True, unique=True)

    def __str__(self):
        return f'Username: {self.username}'

# auction listings
class listings(models.Model):

    item= models.CharField(max_length=50)
    date= models.DateField(auto_now_add = True)
    duration= models.DurationField()
    seller= models.ManyToOneRel(User, on_delete=models.CASCADE, related_name="Seller")
    def __str__(self):
        return f'Item: {self.item}; Date: {self.date}; Seller: {self.seller}'

# auction bids
class bids(models.Model):

    bidder= models.ForeignKey(User, on_delete=models.CASCADE, related_name='Bidder')
    amount = models.IntegerField()
    bid_time = models.TimeField(auto_now_add = True)
    desired = models.ForeignKey(listings, on_delete=models.CASCADE, related_name='wants')
    def __str__(self):
        return f'User: {self.bidder}; amount: {self.amount}; item: {self.desired}'

# comments on auction bids
class comments(models.Model):
    onitem = models.ForeignKey(bids, on_delete=models.CASCADE, related_name='commenter')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    text = models.CharField(max_length=140)
    comment_time = models.TimeField()

    def __str__(self):
        return f'Username: {self.user}; comment: {self.text}'