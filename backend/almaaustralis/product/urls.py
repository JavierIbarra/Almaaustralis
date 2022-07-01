from django.urls import path
from product.api.views.product_views import ProductListAPIView 
from product.api.views.category_views import CategoryListAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product_list'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
]
