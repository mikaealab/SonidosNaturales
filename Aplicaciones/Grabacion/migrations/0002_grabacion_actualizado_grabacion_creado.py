# Generated by Django 5.2 on 2025-07-22 04:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grabacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grabacion',
            name='actualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='grabacion',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
