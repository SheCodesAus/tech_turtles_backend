from django.db import models
from recipients.models import Recipient

STATUS = [
    ('incomplete', 'Incomplete'),
    ('in_progress', 'In Progress'),
    ('complete', 'Complete')
]
class Item(models.Model):
    name = models.CharField(max_length=200)
    cost = models.PositiveIntegerField()
    where_to_buy = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=15,
        choices=STATUS,
        default='incomplete',
    )
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(
        'recipients.Recipient',
        on_delete=models.CASCADE,
        related_name='items'
    )
