
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newtweet", views.newtweet, name="newtweet"),
    path('user/unfollow', views.unfollow, name='follow'),
    path('user/follow', views.follow, name='follow'),
    path("user/like", views.like, name="like"),
    path("user/unlike", views.unlike, name="unlike"),
    path("user/edit", views.edit, name="edit"),
    path("user/<str:username>", views.viewprofile, name="viewprofile"),
    path("following", views.following, name="following"),
    path("like", views.like, name="like"),
    path("unlike", views.unlike, name="unlike"),
    path("edit", views.edit, name="edit"),


    
]
