# Generated by Django 3.0 on 2020-10-07 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('award', '0001_initial'),
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='ths_stu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='sch_stu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='prize',
            name='pri_stu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='patent',
            name='pat_stu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='honor',
            name='hon_stu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='fund',
            name='fund_stu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic.Student', verbose_name='学生'),
        ),
    ]
