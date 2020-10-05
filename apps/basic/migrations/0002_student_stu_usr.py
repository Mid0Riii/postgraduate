# Generated by Django 3.0 on 2020-10-05 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_usr',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='关联用户'),
            preserve_default=False,
        ),
    ]
