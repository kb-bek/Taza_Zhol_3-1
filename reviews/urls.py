from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reviews/', reviews, name='reviews'),
    path('send-reviews/', ReviewSend.as_view(), name='send-reviews'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
