from django.urls import path
from .views import home, autor
from .views import tutoriais

urlpatterns = [
    path('home', home),
    path('autor/', autor),
    path('', tutoriais)
]