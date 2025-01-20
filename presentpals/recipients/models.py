from django.db import models

class Recipient(models.Model):
    name = models.CharField(max_length=200)
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
