# Generated by Django 5.1 on 2025-01-31 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_alter_list_budget_alter_list_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
