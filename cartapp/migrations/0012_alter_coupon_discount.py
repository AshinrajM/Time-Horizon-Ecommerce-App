# Generated by Django 4.2.4 on 2023-10-01 15:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0011_alter_coupon_discount_alter_coupon_min_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
