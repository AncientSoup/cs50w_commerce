# Generated by Django 4.0.1 on 2022-02-14 05:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_listdump_alter_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='listdump',
            name='winner',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 5, 39, 12, 253169, tzinfo=utc)),
        ),
    ]
