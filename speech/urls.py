from django.urls import path
from .views import upload_speech

urlpatterns = [path("upload", upload_speech)]
