from rest_framework import generics, status
from core.models import Carousel

from core.api.serializers.carousel_serializers import CarouselSerializer

class CarouselListAPIView(generics.ListAPIView):
    queryset = Carousel.objects.filter(active=True)
    serializer_class = CarouselSerializer
