from core.models import SocialNetworks
from rest_framework import serializers


class SocialNetworksSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialNetworks
        exclude = ('id','active')