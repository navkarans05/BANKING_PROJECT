# Generated by Django 3.0.3 on 2020-07-01 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0002_auto_20200701_2149'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='details',
            new_name='detail',
        ),
    ]