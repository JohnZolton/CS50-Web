## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com/) and [Django](https://www.djangoproject.com/). 
```
# Clone this repository
git clone --depth 1 --filter=blob:none --sparse https://github.com/JohnZolton/CS50-Web

# Go into the repository
cd CS50-Web

# check out twitter
git sparse-checkout set project4

# Go into the directory
cd project4

# Install dependencies
pip install -r requirements.txt

# Run the app
python manage.py runserver
```

## Description
This is a twitter clone, created using Django. Users can write tweets, like tweets, follow and unfollow other users. Users can also view their follow feed or view all tweets, organized by most recent. They can view a user's personal page and see their followers, following, and all their tweets.
