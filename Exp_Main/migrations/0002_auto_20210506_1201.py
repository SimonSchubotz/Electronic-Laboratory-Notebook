# Generated by Django 3.1.3 on 2021-05-06 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp_Main', '0001_squashed_0053_auto_20210427_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exppath',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='exppath',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='exppath',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='exppath',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Born',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 12, 1, 17, 988767), null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Death',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 12, 1, 17, 988767), null=True),
        ),
    ]
