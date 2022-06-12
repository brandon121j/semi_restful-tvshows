from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	
    path('shows', views.shows),
    path('shows/new', views.newshows),
    path('shows/add', views.addshows),
    path('shows/<int:id>', views.singleshow),
    path('shows/<int:id>/edit', views.editshows),
    path('shows/<int:id>/editshow', views.edit),
    path('shows/<int:id>/destroy', views.destroy),
]