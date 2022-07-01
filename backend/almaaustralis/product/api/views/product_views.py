from rest_framework import generics, status
from product.models import Product

from product.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
