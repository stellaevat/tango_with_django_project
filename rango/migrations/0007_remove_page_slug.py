# Generated by Django 2.2.26 on 2022-01-27 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20220127_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
