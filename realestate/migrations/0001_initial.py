# Generated by Django 4.1 on 2022-08-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_address', models.CharField(max_length=255)),
                ('listing_price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
            },
        ),
    ]
