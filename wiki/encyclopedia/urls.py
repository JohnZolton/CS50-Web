from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:page>', views.display, name="page"),
    path('search/', views.search, name='search'),
    path('newpage/', views.newpage, name='newpage'),
    path('add', views.addpage, name='addpage'),
    path('edit', views.edit, name='edit'),
    path('posted', views.posted, name='posted'),
    path('randchoice', views.randchoice, name='randchoice')
]
