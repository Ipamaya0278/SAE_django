# Generated by Django 2.2.26 on 2022-06-13 08:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220613_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='mach',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Machine'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 8, 5, 2, 877489)),
        ),
        migrations.AlterField(
            model_name='review',
            name='mach',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Machine'),
        ),
    ]
