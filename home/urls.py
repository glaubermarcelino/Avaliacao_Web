from django.urls import path
from .views import home, autor

urlpatterns = [
    path('', home),
    path('autor/', autor),
]