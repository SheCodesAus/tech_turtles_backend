from django.db import models

STATUS = [
    ('incomplete', 'Incomplete'),
    ('in_progress', 'In Progress'),
    ('complete', 'Complete')
]
class Item(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField()
    where_to_buy = models.TextField(blank=True)
    notes = models.TextField()
    status = models.CharField(
        max_length=15,
        choices=STATUS,
        default='incomplete',
    )
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
