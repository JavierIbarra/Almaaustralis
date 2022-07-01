from rest_framework import generics, status
from core.models import TextInfo

from core.api.serializers.text_info_serializers import TextInfoSerializer

class TextInfoListAPIView(generics.ListAPIView):
    queryset = TextInfo.objects.all()
    serializer_class = TextInfoSerializer
