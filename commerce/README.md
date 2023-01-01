![](2023-01-01-13-07-12.gif)

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com/), [Python](https://www.python.org/), [Django](https://www.djangoproject.com/) and [Pillow](https://pillow.readthedocs.io/en/stable/). 
```
# Clone this repository
git clone --depth 1 --filter=blob:none --sparse https://github.com/JohnZolton/CS50-Web

# Go into the repository
cd CS50-Web

# check out commerce
git sparse-checkout set commerce

# Go into the directory
cd commerce

# Install dependencies
pip install -r requirements.txt

# Run the app
python manage.py runserver
```
## Description
This is an e-commerce auction web app akin to eBay or facebook marketplace. Users can create new listings to auction off items, with optional categories and pictures. Users can place bids on listings, comment on listings, see the current price and see the time remaining. The owner of a listing can close bidding at any time. Then the winner can see if they won a given item.
