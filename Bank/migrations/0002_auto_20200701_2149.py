# Generated by Django 3.0.3 on 2020-07-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='bank_id',
            field=models.IntegerField(),
        ),
    ]
