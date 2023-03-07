# Generated by Django 3.1.3 on 2023-03-06 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp_Sub', '0032_auto_20230226_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gas',
            name='Born',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 21, 3, 19, 271869), null=True),
        ),
        migrations.AlterField(
            model_name='gas',
            name='Death',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 21, 3, 19, 271869), null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Born',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 21, 3, 19, 270869), null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Death',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 21, 3, 19, 270869), null=True),
        ),
    ]
