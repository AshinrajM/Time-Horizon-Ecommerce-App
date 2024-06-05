# Generated by Django 4.2.4 on 2023-10-01 09:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0008_coupon_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='min_amount',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
