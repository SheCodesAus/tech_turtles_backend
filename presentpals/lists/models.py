from django.db import models
from django.contrib.auth import get_user_model

class List(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    budget = models.PositiveIntegerField()
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_lists', 
    )
