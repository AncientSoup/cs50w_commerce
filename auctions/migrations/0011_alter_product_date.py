# Generated by Django 4.0.1 on 2022-02-09 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_product_category_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 16, 46, 42, 839078)),
        ),
    ]