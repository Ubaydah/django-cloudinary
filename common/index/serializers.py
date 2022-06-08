from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = Image
        fields = ["image_url", "image", "timestamp"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("image")

        return representation
