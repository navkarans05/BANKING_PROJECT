# Generated by Django 3.0.3 on 2020-07-03 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0005_auto_20200702_0144'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='detail',
            new_name='IFSC',
        ),
    ]