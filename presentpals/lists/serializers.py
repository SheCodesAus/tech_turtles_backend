from rest_framework import serializers
from django.apps import apps

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('lists.List')
        fields = '__all__'