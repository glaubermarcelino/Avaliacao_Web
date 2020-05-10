from django.urls import path
from .views import home, autor
from .views import tutorial

urlpatterns = [
    path('', home),
    path('autor/', autor),
    path('tutorial', tutorial)
]