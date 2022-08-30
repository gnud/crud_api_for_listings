from rest_framework import serializers

from realestate import models


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Listing
        fields = [
            'pk',
            'property_address',
            'listing_price',
        ]
