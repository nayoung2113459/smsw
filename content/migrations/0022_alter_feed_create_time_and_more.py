# Generated by Django 4.1 on 2022-08-22 03:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_alter_feed_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 12, 9, 29, 904340)),
        ),
        migrations.AlterField(
            model_name='volunteeritem',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 12, 9, 29, 905568)),
        ),
    ]
