# Generated by Django 3.1.5 on 2023-04-16 18:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_center', '0005_auto_20230416_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='phone',
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_phone',
            field=models.CharField(default='0000000000', max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
