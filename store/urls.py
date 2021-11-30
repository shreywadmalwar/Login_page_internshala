from django.contrib import admin
from django.urls import path
from .views import login, signup, user


urlpatterns = [
    path('', login),
    path('signup', signup),
    path('user', user)
]
