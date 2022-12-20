from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, get_script_prefix
from .models import *
import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


from .models import User


def index(request):
    tweets = tweet.objects.all()
    return render(request, "network/index.html", {
        'tweets': tweets
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def newtweet(request):
    
    if request.method=='POST':
        text = request.POST['body']
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        newtweet = tweet(
            author = user,
            tweet = text,
            time = datetime.datetime.now(),
            likes = 0
        )
        newtweet.save()
        #return HttpResponseRedirect(reverse("index"))
    return HttpResponseRedirect(request.POST['page'])

def viewprofile(request, username):
    cur_user = request.user
    profile = User.objects.get(username=username)
    tweets = tweet.objects.filter(author = profile)
    follower_count = 0
    following_count = 0
    follows_you = False
    is_following = False

    profile_info, t = follows.objects.get_or_create(account=profile)

    follower_count = profile_info.followers.all().count()
    following_count = profile_info.following.all().count()

    if cur_user in profile_info.followers.all():
        is_following=True

    user_follow_info, t = follows.objects.get_or_create(account=cur_user)
    if cur_user in user_follow_info.following.all():
        follows_you=True

    if request.method=='POST':
        if request.POST.get('formtype') == 'follow':
            print('follow form sent')
            user_follow_info.following.add(profile)
            profile_info.followers.add(cur_user)
            print(profile_info.followers.all())
            is_following = True
            
        if request.POST.get('formtype') == 'unfollow':
            print('unfollow form sent')
            user_follow_info.following.remove(profile)
            profile_info.followers.remove(cur_user)
            is_following = False
        follower_count = profile_info.followers.all().count()


    return render(request, "network/profile.html", {
        'user_profile': profile,
        'tweets': tweets,
        'follower_count':follower_count,
        'following_count': following_count,
        'is_following': is_following,
        'follows_you': follows_you
    })

def following(request):
    if not request.user.id:
        return HttpResponseRedirect(reverse('login'))
    
    user = User.objects.get(id=request.user.id)

    users_following, t = follows.objects.get_or_create(account=user)

    accs_followed = users_following.following.all()
    accounts = User.objects.filter(id__in=accs_followed)
    tweets = tweet.objects.filter(author__in=accounts)

    return render(request, "network/following.html", {
        'tweets':tweets,
    })


def like(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        tweet_id = jsonData.get('tweet_id')

        cur_tweet = tweet.objects.get(id=tweet_id)
        user = User.objects.get(id=request.user.id)
        cur_tweet.likers.add(user)
        cur_tweet.likes = cur_tweet.likers.all().count()
        cur_tweet.save()

        response_data = {'likes': cur_tweet.likes}

        return HttpResponse(json.dumps(response_data), content_type="application/json")



def unlike(request):

    if request.method == 'POST':
        jsonData = json.loads(request.body)
        tweet_id = jsonData.get('tweet_id')

        cur_tweet = tweet.objects.get(id=tweet_id)
        user = User.objects.get(id=request.user.id)
        cur_tweet.likers.remove(user)
        
        cur_tweet.likes = cur_tweet.likers.all().count()

        print(cur_tweet.likes)
        cur_tweet.save()
        response_data = {'likes': cur_tweet.likes}

        return HttpResponse(json.dumps(response_data), content_type="application/json")

#@csrf_exempt # probs return later
def edit(request):
    if request.method == "POST":
        jsonData = json.loads(request.body)
        tweet_id = jsonData.get('tweet_id')
        tweet_body = jsonData.get('body')
        
        cur_tweet = tweet.objects.get(id=tweet_id)
        cur_tweet.tweet = tweet_body
        cur_tweet.time = timezone.now()
        cur_tweet.save()

        response_data = {'tweet_body': tweet_body}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
