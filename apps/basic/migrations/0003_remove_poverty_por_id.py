# Generated by Django 3.0 on 2020-10-08 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20201007_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poverty',
            name='por_id',
        ),
    ]