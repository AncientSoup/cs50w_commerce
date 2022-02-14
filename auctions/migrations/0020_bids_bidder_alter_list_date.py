# Generated by Django 4.0.1 on 2022-02-12 11:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_list_date_alter_list_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 12, 11, 7, 47, 65691, tzinfo=utc)),
        ),
    ]
