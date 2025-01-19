from rest_framework import serializers
from django.apps import apps
from .models import Lists

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        # model = apps.get_model('lists.Lists')
        model = Lists  # Use the correct model here    
        fields = '__all__'