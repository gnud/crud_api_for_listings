from django.core.management.base import BaseCommand

from faker import Faker

from realestate import models

MAX_RECORDS = 10

fake = Faker()


class Command(BaseCommand):
    help = 'Spawns a new data into the database'

    def handle(self, *args, **options):

        for i in range(MAX_RECORDS):
            try:
                models.Listing.objects.create(
                    property_address=fake.address(),
                    listing_price=fake.random.randint(10000, 90000)
                )
            except Exception as e:
                # Not handling specific Exception for demo purposes
                self.stdout.write(self.style.ERROR(f'Item with record {i} failed to be inserted.'))

        self.stdout.write(self.style.SUCCESS(f'Successfully filled databases with {MAX_RECORDS} more records.'))
