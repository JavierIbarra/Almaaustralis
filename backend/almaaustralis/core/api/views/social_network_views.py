from rest_framework import generics, status
from core.models import SocialNetworks

from core.api.serializers.social_networks_serializer import SocialNetworksSerializer

class SocialNetworksListAPIView(generics.ListAPIView):
    queryset = SocialNetworks.objects.filter(active=True)
    serializer_class = SocialNetworksSerializer
