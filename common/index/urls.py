from django.urls import path

from .views import UploadImage

urlpatterns = [
    path("image/upload", UploadImage.as_view())
    ]
