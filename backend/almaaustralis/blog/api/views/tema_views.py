from rest_framework.response import Response
from rest_framework import generics, status

from blog.models import Tema
from blog.api.serializers.tema_serializers import TemaSerializer

class TemaListAPIView(generics.ListAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer