# Generated by Django 4.2.4 on 2023-09-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0004_alter_payment_amount_paid_alter_payment_payment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Ready to Deliver', 'Ready to Deliver'), ('Cancelled', 'Cancelled')], default='Confirmed', max_length=20),
        ),
    ]
