from rest_framework import viewsets
from rest_framework import permissions

from realestate import models
from realestate import serializers


class ListingViewSet(viewsets.ModelViewSet):
    queryset = models.Listing.objects.all().order_by('-pk')
    serializer_class = serializers.ListingSerializer
    permission_classes = [permissions.IsAuthenticated]
