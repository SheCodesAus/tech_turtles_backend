from django.db import models
from lists.models import List
import uuid

class Recipient(models.Model):
    name = models.CharField(max_length=200)
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    list = models.ForeignKey(
        'lists.List',
        on_delete=models.CASCADE,
        related_name='recipients'
    )
    unique_code = models.UUIDField(
        unique=True,
        editable=False,
        default = uuid.uuid4
    )

    @property
    def total_items(self):
        """Calculate the total count of items for this recipient."""
        return self.items.count()

    def __str__(self):
        return self.name