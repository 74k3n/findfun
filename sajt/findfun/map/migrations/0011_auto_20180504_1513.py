# Generated by Django 2.0.4 on 2018-05-04 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_auto_20180504_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 4, 15, 13, 49, 560779)),
        ),
    ]
