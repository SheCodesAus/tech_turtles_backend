from django.db import models
from django.contrib.auth import get_user_model

class List(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.IntegerField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_lists', 
    )
