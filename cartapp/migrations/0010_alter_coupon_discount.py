# Generated by Django 4.2.4 on 2023-10-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0009_alter_coupon_min_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
