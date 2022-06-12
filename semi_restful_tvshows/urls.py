from django.urls import path, include 

urlpatterns = [
path('', include('tvshow_app.urls')),
]