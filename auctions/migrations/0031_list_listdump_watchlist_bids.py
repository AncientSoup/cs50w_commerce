# Generated by Django 4.0.1 on 2022-02-14 09:01

import datetime
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_remove_bids_bidder_remove_bids_item_delete_listdump_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(default=None, max_length=64)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('image', models.URLField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.01'), max_digits=32)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('category', models.TextField(default=None, max_length=72)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 2, 14, 9, 1, 37, 21453, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='ListDump',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('lister', models.CharField(default=None, max_length=64)),
                ('winner', models.CharField(default=None, max_length=64)),
                ('prodtitle', models.CharField(blank=True, max_length=128, null=True)),
                ('image', models.URLField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.01'), max_digits=32)),
                ('category', models.TextField(default=None, max_length=72)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.list')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('biddedprice', models.DecimalField(decimal_places=2, default=Decimal('0.01'), max_digits=32)),
                ('bidder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.list')),
            ],
        ),
    ]