# Generated by Django 4.0.1 on 2022-02-13 09:56

import datetime
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_alter_list_date_delete_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 9, 56, 25, 928142, tzinfo=utc)),
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
