# Generated by Django 3.1.3 on 2021-05-16 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp_Main', '0005_auto_20210516_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquid',
            name='Born',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 16, 17, 44, 44, 773681), null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Death',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 16, 17, 44, 44, 773681), null=True),
        ),
    ]
