from rest_framework import serializers
from django.apps import apps

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model('items.Item')
        fields = '__all__'