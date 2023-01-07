from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('settings', views.settings, name='settings'),
    path("newlisting", views.newlisting, name="newlisting"),
    path('twofactor', views.twofactor, name='twofactor'),
    path('email', views.email, name='email'),
    path('changemail', views.changemail, name='changemail'),
    path('changeusername', views.changeusername, name='changeusername'),
    path('changepass', views.changepass, name='changepass'),
    path('twofactorlogin', views.twofactorlogin, name='twofactorlogin'),
    path('yourlist', views.yourlist, name='yourlist'),
    path('categories', views.category, name='category'),
    path('categories/<str:category>', views.getcategory, name='getcategory'),
    path('<str:item>', views.listing, name='listing'),

]

