from rest_framework import generics, status
from product.models import Category

from product.api.serializers.category_serializers import CategorySerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
