# Generated by Django 5.1 on 2025-01-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_item_delivery_status_item_due_date_item_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
