from django.contrib import admin
from django.urls import path
from account import views
urlpatterns = [
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('logout/',views.logout),
]
