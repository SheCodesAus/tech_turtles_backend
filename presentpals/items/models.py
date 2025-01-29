from django.db import models
from recipients.models import Recipient

PRIORITY = [
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low'),
]

DELIVERY_STATUS = [
    ('pending', 'Pending'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('na', 'Not Applicable'),
]

STATUS = [
    ('incomplete', 'Incomplete'),
    ('complete', 'Complete')
]
class Item(models.Model):
    name = models.CharField(max_length=200)
    cost = models.PositiveIntegerField()
    where_to_buy = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    priority = models.IntegerField(
        choices=PRIORITY,
        default=2,
        blank=True,
    )
    delivery_status = models.CharField(
        max_length=15,
        choices=DELIVERY_STATUS,
        default='na',
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS,
        default='incomplete',
    )
    due_date = models.DateField(null=True, blank=True)
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(
        'recipients.Recipient',
        on_delete=models.CASCADE,
        related_name='items'
    )
