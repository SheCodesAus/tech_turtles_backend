from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_rename_recipients_item_recipient_alter_item_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='delivery_status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('na', 'Not Applicable')], default='na', max_length=15),
        ),
        migrations.AddField(
            model_name='item',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('incomplete', 'Incomplete'), ('complete', 'Complete')], default='incomplete', max_length=15),
        ),
    ]
