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
    id = models.AutoField(primary_key=True)
    Title= models.CharField(max_length=50)
    Description=models.CharField(max_length=300)
    Starting_bid=models.IntegerField()
    Image = models.CharField(max_length=100)
    Category = models.CharField(max_length=20)
    Duration= models.DurationField()
    Seller= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'Item: {self.Title}; Duration: {self.duration}; Seller: {self.seller}'

# auction bids
class bids(models.Model):
    id = models.AutoField(primary_key=True)
    bidder= models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    desired = models.ForeignKey(listings, on_delete=models.CASCADE)

    def __str__(self):
        return f'User: {self.bidder}; amount: {self.amount}; item: {self.desired}'

# comments on auction bids
class comments(models.Model):
    id = models.AutoField(primary_key=True)
    onitem = models.ForeignKey(bids, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    text = models.CharField(max_length=140)


    def __str__(self):
        return f'Username: {self.user}; comment: {self.text}; item: {self.onitem}'