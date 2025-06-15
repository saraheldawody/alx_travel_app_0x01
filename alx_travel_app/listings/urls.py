from rest_framework import routers
from .views import ListingViewSet, BookingViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]