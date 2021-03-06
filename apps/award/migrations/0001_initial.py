# Generated by Django 3.0 on 2020-10-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_project_code', models.CharField(blank=True, max_length=128, null=True, verbose_name='项目编号')),
                ('fund_aca', models.CharField(blank=True, max_length=128, null=True, verbose_name='学院')),
                ('fund_leader', models.CharField(blank=True, max_length=128, null=True, verbose_name='负责人')),
                ('fund_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='项目名称')),
                ('fund_level', models.CharField(blank=True, max_length=128, null=True, verbose_name='学历层次')),
                ('fund_type', models.CharField(blank=True, max_length=128, null=True, verbose_name='学位类型')),
                ('fund_grade', models.CharField(blank=True, max_length=128, null=True, verbose_name='级别')),
                ('fund_money', models.CharField(blank=True, max_length=128, null=True, verbose_name='赞助金额(元)')),
            ],
            options={
                'verbose_name': '专项资金',
                'verbose_name_plural': '专项资金',
            },
        ),
        migrations.CreateModel(
            name='Honor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hon_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='荣誉称号名称')),
                ('hon_year', models.CharField(blank=True, max_length=128, null=True, verbose_name='颁发年份')),
                ('hon_dep', models.CharField(blank=True, max_length=128, null=True, verbose_name='颁发部门')),
            ],
            options={
                'verbose_name': '荣誉称号',
                'verbose_name_plural': '荣誉称号',
            },
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_type', models.CharField(blank=True, max_length=128, null=True, verbose_name='专利类别')),
                ('pat_loc', models.CharField(blank=True, max_length=128, null=True, verbose_name='专利授权国家(地区)')),
                ('pat_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='专利名称')),
                ('pat_owner', models.CharField(blank=True, max_length=128, null=True, verbose_name='专利权人')),
                ('pat_code', models.CharField(blank=True, max_length=128, null=True, verbose_name='专利号')),
                ('pat_date', models.DateField(blank=True, null=True, verbose_name='授权公告日')),
                ('pat_join_count', models.CharField(blank=True, max_length=128, null=True, verbose_name='本单位参与学科数')),
                ('pat_apply', models.CharField(blank=True, max_length=128, null=True, verbose_name='专利转化形式')),
                ('pat_apply_info', models.TextField(blank=True, null=True, verbose_name='转化或应用情况')),
                ('pat_group', models.CharField(blank=True, max_length=128, null=True, verbose_name='专利权人数')),
            ],
            options={
                'verbose_name': '专利',
                'verbose_name_plural': '专利',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pri_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='获奖名称')),
                ('pri_project', models.CharField(blank=True, max_length=128, null=True, verbose_name='获奖项目')),
                ('pri_level', models.CharField(blank=True, max_length=128, null=True, verbose_name='奖励等级')),
                ('pri_unit', models.CharField(blank=True, max_length=128, null=True, verbose_name='颁奖单位')),
                ('pri_date', models.DateField(blank=True, null=True, verbose_name='获奖时间')),
                ('pri_info', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '获奖情况',
                'verbose_name_plural': '获奖情况',
            },
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sch_info', models.TextField(blank=True, null=True, verbose_name='获奖情况和发表论文的情况')),
                ('sch_type', models.CharField(blank=True, max_length=128, null=True, verbose_name='奖/助学金类型')),
                ('sch_level', models.CharField(blank=True, max_length=128, null=True, verbose_name='初评等级')),
                ('sch_is_arrears', models.BooleanField(blank=True, default=False, null=True, verbose_name='是否欠缴学费')),
            ],
            options={
                'verbose_name': '奖/助学金',
                'verbose_name_plural': '奖/助学金',
            },
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ths_subject_code', models.CharField(blank=True, max_length=128, null=True, verbose_name='所属学科代码')),
                ('ths_subject', models.CharField(blank=True, max_length=128, null=True, verbose_name='所属学科名称')),
                ('ths_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='论文题目')),
            ],
            options={
                'verbose_name': '论文',
                'verbose_name_plural': '论文',
            },
        ),
    ]
