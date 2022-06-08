from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser

from .models import Image
from .serializers import ImageSerializer


class UploadImage(CreateAPIView):

    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)
    queryset = Image.objects.all()
