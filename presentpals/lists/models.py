from django.db import models
from django.contrib.auth import get_user_model

class List(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_lists', 
    )

    @property
    def total_cost(self):
        """Calculate the total cost of items for this list."""
        total = 0
        for recipient in self.recipients.all():
            total += recipient.items.aggregate(total_cost=models.Sum('cost'))['total_cost'] or 0
        return total
