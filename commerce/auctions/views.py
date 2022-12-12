from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
import datetime
from .models import *
from django.db.models import Max
from django.urls import resolve

def index(request):
    return render(request, "auctions/index.html", {
        "listings": listings.objects.all(),
        "today": datetime.datetime.now()
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

def yourlist(request):
    user_id = request.user
    mylist = watchlist.objects.filter(user=user_id).values()
    obj_ids = []
    for item in mylist:
        obj_ids.append(item['items_id'])
    obj_list = listings.objects.filter(id__in = obj_ids)

    print(obj_list)
    return render(request, "auctions/yourlist.html", {
        "listings": obj_list
    })

def newlisting(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = NewList(request.POST, request.FILES)
        files = request.FILES
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

def listing(request, item):

    if request.method=='GET':
        item_id = request.GET.get('item')
        user_id = request.user
    else:
        item_id = int(request.POST['item_id'])
        user_id = request.user
    ans = listings.objects.get(id=item_id)
    timeleft = ans.Duration + ans.Starttime.astimezone() - datetime.datetime.now().astimezone()
    time = str(timeleft)[:-7]
    form = CommentForm()
    
    if comments.objects.filter(onitem=item_id):
        item_comments = comments.objects.filter(onitem=item_id)
    else: item_comments = None

    
    item = listings.objects.get(id=item_id)
    is_watched = watchlist.objects.filter(user=user_id, items=item)
    is_seller = item.Seller == user_id
    is_winner = item.Winner == user_id

    if request.method=='POST':
        if request.POST.get('formtype') == 'comment':
            form = CommentForm(data=request.POST)
            item_id = int(request.POST['item_id'])
            item = listings.objects.get(id=item_id)
            user_id = request.user
        
            if form.is_valid() and form.cleaned_data['txt']:
                text = comments(
                    onitem=item,
                    user=user_id,
                    text=form.cleaned_data['txt'],
                    commenttime = datetime.datetime.now()
                )
                text.save()
                form = CommentForm()
                current_url = request.path
                return HttpResponseRedirect(current_url + f'?item={item_id}')
            
        elif request.POST.get('formtype') == 'watch':
            item_id = request.POST['item_id']
            item = listings.objects.get(id=item_id)
            user_id = request.user
            new_watch = watchlist(user=user_id, items=item)
            # check if saved 
            if not is_watched:
                new_watch.save()
                is_watched = True

        elif request.POST.get('formtype') == 'remove':
            item_id = request.POST['item_id']
            item = listings.objects.get(id=item_id)
            watchlist.objects.filter(user=user_id, items=item).delete()
            is_watched = False
        
        elif request.POST.get('formtype') == 'bid':
            allbids = bids.objects.filter(desired=item_id)
            
            if allbids.aggregate(Max('amount'))['amount__max']:
                maxbid = allbids.aggregate(Max('amount'))['amount__max']

            else:
                maxbid = float(item.Starting_bid)

            user_bid = float(request.POST['qty'])

            if user_bid > maxbid:
                cur_bid = bids(
                    bidder= user_id,
                    amount = user_bid,
                    desired = item
                )
                cur_bid.save()
                item.Starting_bid = user_bid
                item.save()
            else:
                item.Starting_bid = maxbid
                item.save()

            ans = listings.objects.get(id=item_id)

        elif request.POST.get('formtype') == 'closebidding':
            high_bid = bids.objects.filter(desired=item, amount=item.Starting_bid)
            winner = high_bid.values('bidder').values('bidder_id')[0]['bidder_id']
            winner_id = User.objects.get(id=winner)
            item.Winner=winner_id
            item.Active=False
            item.save()
            ans.Active=False

            

    return render(request, "auctions/listing.html", {'item':ans,
        "timeleft": time,
        'form': form,
        'comments': item_comments,
        'is_watched':is_watched,
        'is_bidder': is_seller,
        "is_winner": is_winner})

def category(request):
    category_choices = [
    ('1', 'Fashion'),
    ('2', 'Toys'),
    ('3', 'Electronics'),
    ('4', 'Home'),
    ('5', 'Hardware')
]
    categories = []
    for _, x in category_choices:
        categories.append(x)

    return render(request, 'auctions/categories.html', {'categories': categories})

def getcategory(request, category):
    category_choices = [
    ('1', 'Fashion'),
    ('2', 'Toys'),
    ('3', 'Electronics'),
    ('4', 'Home'),
    ('5', 'Hardware')
]
    for x, y in category_choices:
        if y == category:
            options = listings.objects.filter(Category=x)

    return render(request, 'auctions/speccategory.html', {'category': category,
    'listings': options})