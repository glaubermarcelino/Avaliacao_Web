from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, autor, tutoriais

urlpatterns = [
    path('', index),
    path('autor/', autor),
    path('tutoriais', tutoriais)
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)