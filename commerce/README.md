<p align ='center'>
<a href="http://www.youtube.com/watch?feature=player_embedded&v=ux4rXEOuZLI
" target="_blank"><img  src="http://img.youtube.com/vi/ux4rXEOuZLI/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="560" height="315" border="10"  /></a>
</p>
<p align ='center'>
  <a href="http://www.youtube.com/watch?feature=player_embedded&v=ux4rXEOuZLI
" target="_blank">(Youtube Link)</a>
</p>

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com/), [Django](https://www.djangoproject.com/) and [Pillow](https://pillow.readthedocs.io/en/stable/). 
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
