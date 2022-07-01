from django.urls import path
from core.api.views.carousel_views import CarouselListAPIView
from core.api.views.social_network_views import SocialNetworksListAPIView
from core.api.views.text_info_views import TextInfoListAPIView


urlpatterns = [
    path('carousel/', CarouselListAPIView.as_view(), name='sliders'),
    path('socialNetwork/', SocialNetworksListAPIView.as_view(), name='social_network'),
    path('textInfo/', TextInfoListAPIView.as_view(), name='text_info'),
]
