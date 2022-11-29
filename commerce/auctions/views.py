from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewList
import datetime
from .models import *

def index(request):
    return render(request, "auctions/index.html", {
        "listings": listings.objects.all()
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



def newlisting(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request)
        # create a form instance and populate it with data from the request:
        form = NewList(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # need to pull the user_id of seller
            item = listings(
                Title= form.cleaned_data['Title'],
                Description=form.cleaned_data['Description'],
                Starting_bid=form.cleaned_data['Starting_bid'],
                Image=form.cleaned_data['Image'],
                Category=form.cleaned_data['Category'],
                Duration = datetime.timedelta(days=10),
                Seller = request.user
            )

            item.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("index"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewList()

    return render(request, 'auctions/newlisting.html', {'form': form})