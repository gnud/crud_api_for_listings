from django.db import models


class Listing(models.Model):
    property_address = models.CharField(max_length=255)
    listing_price = models.IntegerField()

    class Meta:
        verbose_name = "Listing"
        verbose_name_plural = "Listings"

    def __str__(self):
        pass
