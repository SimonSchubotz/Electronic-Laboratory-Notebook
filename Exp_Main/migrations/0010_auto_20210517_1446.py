# Generated by Django 3.1.3 on 2021-05-17 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp_Main', '0009_auto_20210516_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquid',
            name='Born',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 17, 14, 46, 26, 431146), null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Death',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 17, 14, 46, 26, 431648), null=True),
        ),
    ]
