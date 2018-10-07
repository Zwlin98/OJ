# Generated by Django 2.1.1 on 2018-09-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='i_d',
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(blank=True, verbose_name='题目描述'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='题目编号'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input_decscription',
            field=models.TextField(blank=True, verbose_name='输入描述'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output_decscription',
            field=models.TextField(blank=True, verbose_name='输出描述'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='sample_input',
            field=models.TextField(blank=True, verbose_name='样例输入'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='sample_output',
            field=models.TextField(blank=True, verbose_name='样例输出'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='题目标题'),
        ),
    ]
