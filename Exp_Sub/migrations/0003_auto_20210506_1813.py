# Generated by Django 3.1.3 on 2021-05-06 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp_Sub', '0002_auto_20210506_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gas',
            name='Born',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 18, 13, 39, 868736), null=True),
        ),
        migrations.AlterField(
            model_name='gas',
            name='Death',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 18, 13, 39, 868736), null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Born',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 18, 13, 39, 867736), null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Death',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 18, 13, 39, 867736), null=True),
        ),
    ]
