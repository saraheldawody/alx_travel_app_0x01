from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField(source='host.username')

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price', 'host', 'created_at', 'updated_at']
        read_only_fields = ['id', 'host', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    listing_detail = ListingSerializer(source='listing', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'listing_detail', 'user', 'start_date', 'end_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'listing_detail']