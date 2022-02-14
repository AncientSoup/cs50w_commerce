# Generated by Django 4.0.1 on 2022-02-13 09:54

import datetime
from decimal import Decimal
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_alter_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='biddedprice',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.01'), max_digits=32),
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 9, 54, 41, 391065, tzinfo=utc)),
        ),
    ]
