# Generated by Django 4.2.2 on 2023-09-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cancel_reason',
            field=models.CharField(choices=[('Accidently ordered', 'Accidently ordered'), ('No longer needed', 'No longer needed'), ('Delivery address changed', 'Delivery address changed'), ('Damaged product', 'Damaged product')], default='Accidently ordered', max_length=50),
        ),
    ]
