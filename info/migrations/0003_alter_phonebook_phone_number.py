# Generated by Django 3.2 on 2021-06-06 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_phonebook_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonebook',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='phone number invalid', regex='^0[0-9]{2,}[0-9]{7,}$')], verbose_name='شماره تلفن'),
        ),
    ]
