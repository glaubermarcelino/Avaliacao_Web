from django.urls import path
from .views import home, autor, tutoriais

urlpatterns = [
    path('', home),
    path('autor/', autor),
    path('tutoriais', tutoriais)
]