from django.db import models

class List(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.IntegerField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
