# Generated by Django 5.1 on 2025-01-21 10:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipients', '0002_recipient_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='unique_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
