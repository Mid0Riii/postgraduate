# Generated by Django 3.0 on 2020-08-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签管理',
                'verbose_name_plural': '标签管理',
            },
        ),
        migrations.CreateModel(
            name='MyFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='文件名')),
                ('file_body', models.FileField(blank=True, null=True, upload_to='', verbose_name='文件')),
                ('file_tag', models.ManyToManyField(blank=True, to='common.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文件管理',
                'verbose_name_plural': '文件管理',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ann_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='公告标题')),
                ('ann_body', models.TextField(blank=True, null=True, verbose_name='公告正文')),
                ('ann_visibility', models.BooleanField(default=False, verbose_name='是否可见')),
                ('ann_file', models.ManyToManyField(blank=True, to='common.MyFile', verbose_name='关联公告')),
            ],
            options={
                'verbose_name': '公告发布',
                'verbose_name_plural': '公告发布',
            },
        ),
    ]