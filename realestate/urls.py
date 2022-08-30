from rest_framework import routers

from realestate import api

router = routers.DefaultRouter()
router.register(r'listing', api.ListingViewSet)
