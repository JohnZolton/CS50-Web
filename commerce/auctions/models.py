from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50, blank=True, null=True, unique=True)
    otpkey = models.CharField(max_length=32, blank=True, null=True, default=None)
    twofactorenabled= models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.username}'

# auction listings
class listings(models.Model):
    id = models.AutoField(primary_key=True)
    Title= models.CharField(max_length=50)
    Description=models.CharField(max_length=300)
    Starting_bid=models.DecimalField(decimal_places=2, max_digits=12)
    Image = models.ImageField(upload_to='images/', null=False, blank=False)
    Category = models.CharField(max_length=20)
    Duration= models.DurationField()
    Starttime = models.DateTimeField(auto_now_add=True)
    Seller= models.ForeignKey(User, on_delete=models.CASCADE, related_name="Seller")
    Active = models.BooleanField(default=True)
    Winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="Winner")
    def __str__(self):
        return f'Item: {self.Title}; Duration: {self.Duration}; Seller: {self.Seller}'

# auction bids
class bids(models.Model):
    id = models.AutoField(primary_key=True)
    bidder= models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    desired = models.ForeignKey(listings, on_delete=models.CASCADE)

    def __str__(self):
        return f'User: {self.bidder}; amount: {self.amount}; item: {self.desired.id}'

# comments on auction bids
class comments(models.Model):
    id = models.AutoField(primary_key=True)
    onitem = models.ForeignKey(listings, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    text = models.CharField(max_length=140)
    commenttime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Username: {self.user}; comment: {self.text}; item: {self.onitem.id}'

class watchlist(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(listings, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Username: {self.user}; item: {self.items}'
