# Generated by Django 4.2.4 on 2023-10-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0007_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
