from blog.models import Tema
from rest_framework import serializers


class TemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tema
        exclude = ('created', 'updated')