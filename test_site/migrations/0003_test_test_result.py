# Generated by Django 3.1 on 2020-08-23 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_site', '0002_auto_20200820_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_result',
            field=models.CharField(default='', max_length=20, verbose_name='Результат'),
        ),
    ]
