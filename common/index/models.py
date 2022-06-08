from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Image(models.Model):

    image = CloudinaryField("image")
    timestamp = models.DateTimeField(default=timezone.now)

    @property
    def image_url(self):
        return (
            f"https://res.cloudinary.com/dpoix2ilz/{self.image}"
        )
