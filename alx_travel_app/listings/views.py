from rest_framework import viewsets, permissions
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only owners (host or booking user) to edit/delete."""
    def has_object_permission(self, request, view, obj):
        # Read permissions allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only to the respective owner
        if hasattr(obj, 'host'):
            return obj.host == request.user
        if hasattr(obj, 'user'):
            return obj.user == request.user
        return False

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)