# Generated by Django 5.1 on 2025-01-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('budget', models.IntegerField()),
                ('is_open', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
