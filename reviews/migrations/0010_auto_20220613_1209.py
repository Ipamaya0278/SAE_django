# Generated by Django 2.2.26 on 2022-06-13 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20220613_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='personnel',
            new_name='personne',
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 12, 9, 38, 945930)),
        ),
    ]
