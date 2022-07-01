from core.models import TextInfo
from rest_framework import serializers


class TextInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextInfo
        fields = '__all__'