# Generated by Django 2.2.4 on 2019-10-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsV1', '0003_auto_20191011_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persondetails',
            name='gender',
        ),
    ]